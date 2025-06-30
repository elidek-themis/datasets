import pandas as pd
import re

def tokenize_with_punct(text):
    """
    Tokenize text into words, contractions, and punctuation separately.
    Contractions like "don't", "couldn't" are single tokens.
    """
    # Regex explanation:
    # \w+('\w+)? matches words with optional apostrophe contractions: e.g. don't, couldn't
    # |[^\w\s] matches any single punctuation char (not word or space)
    return re.findall(r"\w+(?:'\w+)?|[^\w\s]", text)

def reconstruct_text(tokens):
    text = ""
    for i, token in enumerate(tokens):
        if i == 0:
            text += token
        else:
            # Treat <MASK> as a special word token
            if token == "<MASK>":
                text += " " + token
            elif re.match(r"[^\w\s]", token):
                # punctuation → no space before it
                text += token
            else:
                # regular word → space before it
                text += " " + token
    return text

def is_word(token):
    """Return True if token is a word or contraction (e.g., don't), False otherwise."""
    return bool(re.match(r"\w+(?:'\w+)?$", token))

def extract_prefix_and_continuations(s1, s2):
    tokens1 = tokenize_with_punct(s1)
    tokens2 = tokenize_with_punct(s2)

    # Extract word tokens positions for comparison
    words1 = [t for t in tokens1 if is_word(t)]
    words2 = [t for t in tokens2 if is_word(t)]

    # Find common prefix on word tokens only
    common_word_count = 0
    for w1, w2 in zip(words1, words2):
        if w1 == w2:
            common_word_count += 1
        else:
            break

    # Split tokens so that prefix includes all tokens up to common_word_count-th word token
    def split_tokens(tokens, word_count):
        count = 0
        for i, t in enumerate(tokens):
            if is_word(t):
                count += 1
            if count == word_count:
                # Include punctuation after last matched word token
                return tokens[:i+1], tokens[i+1:]
        return tokens, []

    prefix_tokens1, cont_tokens1 = split_tokens(tokens1, common_word_count)
    _, cont_tokens2 = split_tokens(tokens2, common_word_count)

    prefix = reconstruct_text(prefix_tokens1)
    cont1 = reconstruct_text(cont_tokens1)
    cont2 = reconstruct_text(cont_tokens2)

    return prefix.strip(), cont1.strip(), cont2.strip()

def extract_masked_and_tokens(s1, s2):
    tokens1 = tokenize_with_punct(s1)
    tokens2 = tokenize_with_punct(s2)

    # Get indices of word tokens in tokens1
    word_indices1 = [i for i, t in enumerate(tokens1) if is_word(t)]
    word_indices2 = [i for i, t in enumerate(tokens2) if is_word(t)]

    # Loop over word tokens only
    for idx1, idx2 in zip(word_indices1, word_indices2):
        if tokens1[idx1] != tokens2[idx2]:
            masked_tokens = tokens1.copy()
            masked_tokens[idx1] = '<MASK>'
            masked = reconstruct_text(masked_tokens)
            return masked, tokens1[idx1], tokens2[idx2]

    # No differing word found
    return s1, '', ''

# === Example usage for CSV processing ===
crows_df = pd.read_csv('data/crows_pairs_anonymized.csv')
prompts_df = pd.read_csv('data/prompts.csv')

assert len(crows_df) == len(prompts_df), "Mismatch in number of rows between the two CSVs"

continuation_rows = []
for i, (stereo, antistereo, prompt) in enumerate(zip(crows_df['sent_more'], crows_df['sent_less'], prompts_df['prompt'])):

    prefix, cont1, cont2 = extract_prefix_and_continuations(stereo, antistereo)
    input_text = f"{prompt} {prefix}".strip()
    continuation_rows.append({
        "input": input_text,
        "stereotype_continuation": cont1,
        "antistereotype_continuation": cont2,
        "stereo_antistereo": crows_df['stereo_antistereo'].iloc[i],
        "bias_type": crows_df['bias_type'].iloc[i],
        "annotations": crows_df['annotations'].iloc[i],
        "anon_writer": crows_df['anon_writer'].iloc[i],
        "anon_annotators": crows_df['anon_annotators'].iloc[i],
    })

continuation_df = pd.DataFrame(continuation_rows)
continuation_df.to_csv('data/continuations.csv', index=False)
print("Continuation-style output written to data/continuations.csv")

masked_rows = []
for i, (stereo, antistereo, prompt) in enumerate(zip(crows_df['sent_more'], crows_df['sent_less'], prompts_df['prompt'])):

    input_text, token1, token2 = extract_masked_and_tokens(stereo, antistereo)
    input_text = f"{prompt} {input_text}".strip()
    masked_rows.append({
        "input": input_text,
        "stereotype_token": token1,
        "antistereotype_token": token2,
        "stereo_antistereo": crows_df['stereo_antistereo'].iloc[i],
        "bias_type": crows_df['bias_type'].iloc[i],
        "annotations": crows_df['annotations'].iloc[i],
        "anon_writer": crows_df['anon_writer'].iloc[i],
        "anon_annotators": crows_df['anon_annotators'].iloc[i],
    })

masked_df = pd.DataFrame(masked_rows)
masked_df.to_csv('data/masked.csv', index=False)
print("Masked-style output written to data/masked.csv")
