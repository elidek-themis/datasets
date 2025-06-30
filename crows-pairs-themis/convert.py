import pandas as pd
import difflib
import os

def extract_prefix_and_continuations(s1, s2):
    tokens1 = s1.strip().split()
    tokens2 = s2.strip().split()
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


# Read input files
crows_df = pd.read_csv('data/crows_pairs_anonymized.csv')
prompts_df = pd.read_csv('data/prompts.csv')

# Sanity check
assert len(crows_df) == len(prompts_df), "Mismatch in number of rows between the two CSVs"

# Output rows
output_rows = []

for i, (stereo, antistereo, prompt) in enumerate(zip(crows_df['sent_more'], crows_df['sent_less'], prompts_df['prompt'])):
    prefix, cont1, cont2 = extract_prefix_and_continuations(stereo, antistereo)
    combined_prompt = f"{prompt.strip()} {prefix}"  # make sure spacing is clean
    output_rows.append({
        "combined_prompt": combined_prompt,
        "stereotype_continuation": cont1,
        "antistereotype_continuation": cont2,
        "stereo_antistereo": crows_df['stereo_antistereo'].iloc[i],
        "bias_type": crows_df['bias_type'].iloc[i],
        "annotations": crows_df['annotations'].iloc[i],
        "anon_writer": crows_df['anon_writer'].iloc[i],
        "anon_annotators": crows_df['anon_annotators'].iloc[i],
    })

# Write to new CSV
output_df = pd.DataFrame(output_rows)
output_df.to_csv('data/transformed_prompts.csv', index=False)

print("Output written to data/transformed_prompts.csv")
