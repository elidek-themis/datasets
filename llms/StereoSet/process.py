import re
from pathlib import Path

from datasets import load_dataset


def process_inter_docs(dataset):
    def process_doc(doc):
        sentences = doc["sentences"]
        choices, labels = sentences["sentence"], sentences["gold_label"]

        # stereo, anti-stereo, unrelated
        choices = [choices[labels.index(i)] for i in (1, 0, 2)]

        return {
            "prompt": doc["context"],
            "choices": choices,
            "bias_type": doc["bias_type"],
            "target": doc["target"],
        }

    return dataset.map(
        process_doc, remove_columns=["id", "sentences", "context"]
    ).select_columns(["prompt", "choices", "bias_type", "target"])


def process_intra_docs(dataset):
    def process_doc(doc):
        prompt = doc["context"]

        blank_idx = prompt.find("BLANK")  # where `BLANK` starts

        sentences = doc["sentences"]
        choices, labels = sentences["sentence"], sentences["gold_label"]

        # stereo, anti-stereo, unrelated
        choices = [choices[labels.index(i)] for i in (1, 0, 2)]
        choices = [
            first_word.group(1)
            for choice in choices
            if (first_word := re.search(r"\b([A-Za-z\-]+)\b", choice[blank_idx:]))
        ]

        return {
            "prompt": prompt,
            "choices": choices,
            "bias_type": doc["bias_type"],
            "target": doc["target"],
        }

    return dataset.map(
        process_doc, remove_columns=["id", "sentences", "context"]
    ).select_columns(["prompt", "choices", "bias_type", "target"])


data_path = Path(__file__).resolve().parent
save_path = data_path / "data"
hf_path = "McGill-NLP/stereoset"

# intersentence
inter_stereo_set = load_dataset(hf_path, name="intersentence", split="validation")
inter_stereo_set = process_inter_docs(inter_stereo_set)
inter_df = inter_stereo_set.to_pandas()
inter_df.to_csv(save_path / "intersentence_stereo_set.csv", index=False)
# intrasentence
intra_stereo_set = load_dataset(hf_path, name="intrasentence", split="validation")
intra_stereo_set = process_intra_docs(intra_stereo_set)
intra_df = intra_stereo_set.to_pandas()
intra_df.to_csv(save_path / "intrasentence_stereo_set.csv", index=False)
