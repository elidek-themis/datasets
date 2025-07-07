# Copyright 2020 The HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This work contains adaptations of the original CrowS-Pairs dataset,
# used under Apache License 2.0. Modifications include adding the prompt
# along with the stereotype and anti-stereotype sentences. The dataset
# is further used to audit the performance of autoregressive language
# models in multiple-choice and generation tasks.
"""CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models"""

import csv
import json
from pathlib import Path
from typing import Any
import pandas as pd
import datasets

from .utils import get_differences

_CITATION = """\
@inproceedings{nangia2020crows,
    title = "{CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models}",
    author = "Nangia, Nikita  and
      Vania, Clara  and
      Bhalerao, Rasika  and
      Bowman, Samuel R.",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics"
}
"""
# ruff: noqa: E501
_DESCRIPTION = """\
CrowS-Pairs, a challenge dataset for measuring the degree to which U.S. stereotypical biases present in the masked language models (MLMs).
"""

_URL = ["https://raw.githubusercontent.com/nyu-mll/crows-pairs/master/data/crows_pairs_anonymized.csv"]

_BIAS_TYPES = [
    "race-color",
    "socioeconomic",
    "gender",
    "disability",
    "nationality",
    "sexual-orientation",
    "physical-appearance",
    "religion",
    "age",
]

_STEREOTYPICAL_DIRECTIONS = ["stereo", "antistereo"]

class CrowsPairsThemisConfig(datasets.BuilderConfig):
    def __init__(
        self,
        mask_token: str,
        min_mask_size: int,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.mask_token = mask_token
        self.min_mask_size = min_mask_size

class CrowsPairsPrompts(datasets.GeneratorBasedBuilder):
    "CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models"

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="crows_pairs",
            version=datasets.Version("1.0.0", ""),
        ),
        CrowsPairsThemisConfig(
            name="themis",
            mask_token="<MASK>",
            min_mask_size=50,
            version=datasets.Version("2.0.0", "")
        ),
    ]

    DEFAULT_CONFIG_NAME = "themis"

    def _info(self):
        if self.config.name == "crows_pairs":
            return datasets.DatasetInfo(
                description=_DESCRIPTION,
                features=datasets.Features(
                    {
                        "id": datasets.Value("int32"),
                        "sent_more": datasets.Value("string"),
                        "sent_less": datasets.Value("string"),
                        "stereo_antistereo": datasets.ClassLabel(names=_STEREOTYPICAL_DIRECTIONS),
                        "bias_type": datasets.ClassLabel(names=_BIAS_TYPES),
                        "annotations": datasets.Sequence(datasets.Sequence(datasets.ClassLabel(names=_BIAS_TYPES))),
                        "anon_writer": datasets.Value("string"),
                        "anon_annotators": datasets.Sequence(datasets.Value("string")),
                    },
                ),
                supervised_keys=None,
                citation=_CITATION,
                homepage="https://github.com/nyu-mll/crows-pairs",
            )
            
        if self.config.name == "themis":
            return datasets.DatasetInfo(
                description=_DESCRIPTION,
                features=datasets.Features(
                    {
                        "prompt": datasets.Value("string"),
                        # "sent_more": datasets.Value("string"),
                        # "sent_less": datasets.Value("string"),
                        "choices": datasets.Sequence(datasets.Value("string")),
                        "stereo_antistereo": datasets.Value("string"),
                        "bias_type": datasets.Value("string"),
                    }
                ),
                citation=_CITATION,
            )        

    def _split_generators(self, dl_manager):
        if self.config.name == "crows_pairs":
            filepath = dl_manager.download(_URL)
            return [
                datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": filepath}),
            ] 
        elif self.config.name == "themis":            
            filepaths = [Path("data") / "crows_pairs_themis.csv", Path("data") / "prompts.csv"]
            data_files = dl_manager.download_and_extract(filepaths)
            
            return [
                datasets.SplitGenerator(
                    name="default",
                    gen_kwargs={"filepaths": data_files, "split": "default"},
                ),
                datasets.SplitGenerator(
                    name="common_prefix",
                    gen_kwargs={"filepaths": data_files, "split": "common_prefix"},
                ),
                datasets.SplitGenerator(
                    name="mask",
                    gen_kwargs={"filepaths": data_files, "split": "mask"},
                ),
            ]

    
    def _generate_test_split(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            rows = csv.DictReader(f)
            for i, row in enumerate(rows):
                row["annotations"] = json.loads(row["annotations"].replace("'", '"'))
                row["anon_annotators"] = json.loads(row["anon_annotators"].replace("'", '"'))
                row["id"] = int(row.pop(""))
                yield i, row
                
    
    def _generate_default_split(self, df):
        for key, row in enumerate(df.to_dict(orient="records")):
            choices = [row["sent_more"], row["sent_less"]]
            yield (
                key,
                {
                    # "sent_more": row["sent_more"],
                    # "sent_less": row["sent_less"],
                    "prompt": row["prompt"],
                    "choices": choices,
                    "stereo_antistereo": row["stereo_antistereo"],
                    "bias_type": row["bias_type"],
                },
            )
            
    
    def _generate_common_prefix_split(self, df):
        for key, row in enumerate(df.to_dict(orient="records")):
            affix = get_differences(sent_1=row["sent_more"], sent_2=row["sent_less"])
            yield (
                key,
                {
                    # "sent_more": row["sent_more"],
                    # "sent_less": row["sent_less"],
                    "prompt": row["prompt"] + " " + affix.prefix,
                    "choices": (affix.infix_1 + affix.suffix, affix.infix_2 + affix.suffix),
                    "stereo_antistereo": row["stereo_antistereo"],
                    "bias_type": row["bias_type"],
                },
            )
            
    
    def _generate_mask_split(self, df):
        def skip_condition(affix):
            return any(len(infix.split()) > min_mask_size for infix in (affix.infix_1, affix.infix_2))
        
        mask = self.config.mask_token
        min_mask_size = self.config.min_mask_size
        
        for key, row in enumerate(df.to_dict(orient="records")):
            affix = get_differences(sent_1=row["sent_more"], sent_2=row["sent_less"])    
            if skip_condition(affix): continue  # noqa: E701
            yield (
                key,
                {
                    # "sent_more": row["sent_more"],
                    # "sent_less": row["sent_less"],
                    "prompt": row["prompt"] + " " + affix.to_template(mask_token=mask)["template"],
                    "choices": (affix.infix_1, affix.infix_2),
                    "stereo_antistereo": row["stereo_antistereo"],
                    "bias_type": row["bias_type"],
                },
            )             
            
    
    def _generate_examples(self, **kwargs):
        if self.config.name == "crows_pairs":
            filepath = kwargs.pop("filepath", None)
            return self._generate_test_split(filepath)
        
        elif self.config.name == "themis":
            filepaths = kwargs.pop("filepaths", None)
            split = kwargs.pop("split", None)
            
            cols = ["sent_more", "sent_less", "stereo_antistereo", "bias_type"]

            data_path, prompts_path = filepaths

            df = pd.read_csv(data_path, usecols=cols)
            prompts = pd.read_csv(prompts_path)["prompt"]
            df = pd.concat([df, prompts], axis=1)
            
            if split == "default":
                return self._generate_default_split(df)
            elif split == "common_prefix":
                return self._generate_common_prefix_split(df)
            elif split == "mask":
                return self._generate_mask_split(df)

