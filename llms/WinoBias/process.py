from pathlib import Path

from datasets import load_dataset

data_path = Path(__file__).resolve().parent
save_path = data_path / "data"

ds_type_1 = load_dataset("chriskara/wino_bias_cloze", name="type_1", split="test")
ds_type_1.to_pandas().to_csv(save_path / "type_1.csv", index=False)

ds_type_2 = load_dataset("chriskara/wino_bias_cloze", name="type_2", split="test")
ds_type_2.to_pandas().to_csv(save_path / "type_2.csv", index=False)
