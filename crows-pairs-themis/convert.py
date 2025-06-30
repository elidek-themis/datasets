import pandas as pd
import re
import os

def tokenize(text):
    """Tokenize text into words and punctuation separately."""
    return re.findall(r"\w+|[^\w\s]", text)

def extract_prefix_and_continuations(s1, s2):
    tokens1 = tokenize(s1)
    tokens2 = tokenize(s2)
    common_tokens = []
    for t1, t2 in zip(tokens1, tokens2):
        if t1 == t2:
            common_tokens.append(t1)
        else:
            break
    prefix = " ".join(common_tokens).strip()
    cont1 = " ".join(tokens1[len(common_tokens):]).strip()
    cont2 = " ".join(tokens2[len(common_tokens):]).strip()
    return prefix, cont1, cont2

def extract_masked_and_tokens(s1, s2):
    tokens1 = tokenize(s1)
    tokens2 = tokenize(s2)

    # Find the first word token where they differ (skip punct differences)
    for i, (t1, t2) in enumerate(zip(tokens1, tokens2)):
        if t1 != t2 and re.match(r"\w+", t1) and re.match(r"\w+", t2):
            masked_tokens = tokens1.copy()
            masked_tokens[i] = '<MASK>'
            masked = " ".join(masked_tokens)
            return masked, t1, t2
    # No differing word found
    return s1, '', ''

# === Read input files ===
crows_df = pd.read_csv('data/crows_pairs_anonymized.csv')
prompts_df = pd.read_csv('data/prompts.csv')

assert len(crows_df) == len(prompts_df), "Mismatch in number of rows between the two CSVs"

# === CONTINUATION-STYLE OUTPUT ===
continuation_rows = []

for i, (stereo, antistereo, prompt) in enumerate(zip(crows_df['sent_more'], crows_df['sent_less'], prompts_df['prompt'])):
    prefix, cont1, cont2 = extract_prefix_and_continuations(stereo, antistereo)
    combined_prompt = f"{prompt.strip()} {prefix}".strip()
    continuation_rows.append({
        "input": combined_prompt,
        "stereotype_continuation": cont1,
        "antistereotype_continuation": cont2,
        "stereo_antistereo": crows_df['stereo_antistereo'].iloc[i],
        "bias_type": crows_df['bias_type'].iloc[i],
        "annotations": crows_df['annotations'].iloc[i],
        "anon_writer": crows_df['anon_writer'].iloc[i],
        "anon_annotators": crows_df['anon_annotators'].iloc[i],
    })

continuation_df = pd.DataFrame(continuation_rows)
continuation_df.to_csv('data/continuations_original.csv', index=False)
print("Continuation-style output written to data/continuations_original.csv")

# === MASKED-STYLE OUTPUT ===
masked_rows = []

for i, (stereo, antistereo) in enumerate(zip(crows_df['sent_more'], crows_df['sent_less'])):
    masked_input, token1, token2 = extract_masked_and_tokens(stereo, antistereo)
    masked_rows.append({
        "masked_input": masked_input,
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
