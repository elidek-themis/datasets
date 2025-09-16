from pathlib import Path

import pandas as pd
from datasets import load_dataset

data_path = Path(__file__).resolve().parent
builder_path = data_path / "builder.py"
save_path = data_path / "data"

# default split
default_split = load_dataset(
    path=str(builder_path),
    split="default",
    trust_remote_code=True,
)
default_split = default_split.to_pandas()
default_split.to_csv(save_path / "default_split.csv", index=False)

# mask split
mask_split = load_dataset(
    path=str(builder_path),
    split="mask",
    mask_token="[MASK]",
    trust_remote_code=True,
)
mask_split = mask_split.to_pandas()
mask_split.to_csv(save_path / "mask_split.csv", index=False)


# mask size metrics
def mask_args(x):
    return {
        "path": str(builder_path),
        "split": "mask",
        "min_mask_size": x,
        "trust_remote_code": True,
    }


counts_50 = mask_split.bias_type.value_counts()
counts_10 = load_dataset(**mask_args(10)).to_pandas().bias_type.value_counts()
counts_5 = load_dataset(**mask_args(5)).to_pandas().bias_type.value_counts()
counts_2 = load_dataset(**mask_args(2)).to_pandas().bias_type.value_counts()
counts_1 = load_dataset(**mask_args(1)).to_pandas().bias_type.value_counts()


objs = {"50": counts_50, "10": counts_10, "5": counts_5, "2": counts_2, "1": counts_1}
counts = pd.concat(objs=objs.values(), keys=objs.keys(), axis=1)
counts.loc["Σ"] = counts.sum()

print(counts)
