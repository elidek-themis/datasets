# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
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

# This work contains adaptations of the revised CrowS-Pairs dataset,
# used under under a Creative Commons Attribution-ShareAlike 4.0 International License.
# Modifications include adding two additional splits. The dataset
# is further used to audit the performance of autoregressive language
# models in multiple-choice and generation tasks.

import csv
import json
from pathlib import Path
from typing import Any
import pandas as pd
import datasets
from .utils import get_differences


import csv
import json
import os
import pandas as pd

import datasets

_CITATION = """\
@inproceedings{neveol2022french,
  title={French CrowS-Pairs: Extending a challenge dataset for measuring social bias in masked language models to a language other than English},
  author={N{\'e}v{\'e}ol, Aur{\'e}lie and Dupont, Yoann and Bezan{\c{c}}on, Julien and Fort, Kar{\"e}n},
  booktitle={ACL 2022-60th Annual Meeting of the Association for Computational Linguistics},
  year={2022}
}
"""

_DESCRIPTION = """\
This is a revised version of CrowS-Pairs that measures stereotypes in language modelling in both English and French.
"""

_HOMEPAGE = "https://gitlab.inria.fr/french-crows-pairs/acl-2022-paper-data-and-code/-/tree/main"

_LICENSE = "French CrowS-Pairs is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. It is created using material developed by the authors of the Crows-Pairs corpus (Nangia et al. 2020)"

_URLS = {
    "english": "https://gitlab.inria.fr/french-crows-pairs/acl-2022-paper-data-and-code/-/raw/main/data/crows_pairs_EN_revised+210.csv",
    "french": "https://gitlab.inria.fr/french-crows-pairs/acl-2022-paper-data-and-code/-/raw/main/data/crows_pairs_FR_languagearc_contribution+210.csv",
}


class CrowsPairsConfig(datasets.BuilderConfig):
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

    VERSION = datasets.Version("1.2.0")

    BUILDER_CONFIGS = [
        CrowsPairsConfig(
            name="english",
            mask_token="<MASK>",
            min_mask_size=50,
            version=VERSION,
            description="English CrowS-Pairs",
        ),
        CrowsPairsConfig(
            name="french",
            mask_token="<MASK>",
            min_mask_size=50,
            version=VERSION,
            description="French CrowS-Pairs",
        ),
    ]

    DEFAULT_CONFIG_NAME = "english"

    def _info(self):
        features = datasets.Features(
            {
                "template": datasets.Value("string"),
                "sent_more": datasets.Value("string"),
                "sent_less": datasets.Value("string"),
                "stereo_antistereo": datasets.Value("string"),
                "bias_type": datasets.Value("string"),
            }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        urls = _URLS[self.config.name]
        data_file = dl_manager.download_and_extract(urls)

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={"filepath": data_file, "split": "test"},
            ),
            datasets.SplitGenerator(
                name="common_prefix",
                gen_kwargs={"filepath": data_file, "split": "common_prefix"},
            ),
            datasets.SplitGenerator(
                name="mask",
                gen_kwargs={"filepath": data_file, "split": "mask"},
            ),
        ]

    def _generate_test_split(self, df):
        for key, row in enumerate(df.to_dict(orient="records")):
            yield key, {"template": ""} | row

    def _generate_common_prefix_split(self, df):
        for key, row in enumerate(df.to_dict(orient="records")):
            affix = get_differences(sent_1=row["sent_more"], sent_2=row["sent_less"])
            yield (
                key,
                {
                    "template": affix.prefix,
                    "sent_more": affix.infix_1 + " " + affix.suffix,
                    "sent_less": affix.infix_2 + " " + affix.suffix,
                    "stereo_antistereo": row["stereo_antistereo"],
                    "bias_type": row["bias_type"],
                },
            )

    def _generate_mask_split(self, df):
        def skip_condition(affix, min_mask_size):
            is_min_len = any(
                len(infix.split()) > min_mask_size
                for infix in (affix.infix_1, affix.infix_2)
            )
            is_empty = not all((affix.infix_1, affix.infix_2))
            return is_min_len or is_empty

        mask = self.config.mask_token
        min_mask_size = self.config.min_mask_size

        for key, row in enumerate(df.to_dict(orient="records")):
            affix = get_differences(sent_1=row["sent_more"], sent_2=row["sent_less"])
            if skip_condition(affix, min_mask_size):
                continue  # noqa: E701
            yield (
                key,
                {
                    "template": affix.to_template(mask_token=mask)["template"],
                    "sent_more": affix.infix_1,
                    "sent_less": affix.infix_2,
                    "stereo_antistereo": row["stereo_antistereo"],
                    "bias_type": row["bias_type"],
                },
            )

    def _generate_examples(self, filepath: str, split: str):
        df = pd.read_csv(filepath, sep="\t", index_col=0)

        if split == "test":
            return self._generate_test_split(df=df)
        elif split == "common_prefix":
            return self._generate_common_prefix_split(df=df)
        elif split == "mask":
            return self._generate_mask_split(df=df)
