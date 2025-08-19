# CrowS-Pairs

This is a forked repo for [CrowS-Pairs](https://www.aclweb.org/anthology/2020.emnlp-main.154/), a challenge dataset for measuring the degree to which U.S. stereotypical biases present in the masked language models (MLMs). The associated paper is to be published as part of The 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP 2020).

**Data reliability: Please note that recent work by [Blodgett et al. (2021)](https://www.microsoft.com/en-us/research/uploads/prod/2021/06/The_Salmon_paper.pdf) has found significant issues with noise and reliability of the data in CrowS-Pairs. The problems are significant enough that CrowS-Pairs may not be a good indicator of the presence of social biases in LMs. Please refer to the Blodgett et al. paper for details.**

## The Dataset

The dataset along with its annotations is in [crows_pairs_anonymized.csv](https://github.com/nyu-mll/crows-pairs/blob/master/data/crows_pairs_anonymized.csv). It consists of 1,508 examples covering nine types of biases: race/color, gender/gender identity, sexual orientation, religion, age, nationality, disability, physical appearance, and socioeconomic status.

Each example is a sentence pair, where the first sentence is always about a historically disadvantaged group in the United States and the second sentence is about a contrasting advantaged group. The first sentence can _demonstrate_ or _violate_ a stereotype. The other sentence is a minimal edit of the first sentence: The only words that change between them are those that identify the group. Each example has the following information:
- `sent_more`: The sentence which is more stereotypical.
- `sent_less`: The sentence which is less stereotypical.
- `stereo_antistereo`: The stereotypical direction of the pair. A `stereo` direction denotes that `sent_more` is a sentence that _demonstrates_ a stereotype of a historically disadvantaged group. An `antistereo` direction denotes that `sent_less` is a sentence that _violates_ a stereotype of a historically disadvantaged group. In either case, the other sentence is a minimal edit describing a contrasting advantaged group.
- `bias_type`: The type of biases present in the example.
- `annotations`: The annotations of bias types from crowdworkers.
- `anon_writer`: The _anonymized_ id of the writer.
- `anon_annotators`: The _anonymized_ ids of the annotators.

All rights reserved to the authors.

## Themis
The official [HuggingFace implementation](https://huggingface.co/datasets/nyu-mll/crows_pairs) does not include the context file [prompts.csv](prompts.csv). \
The builder adds the context as a prefix and provides the followings splits:
* default:
    * `prompt`: The context of the sentences.
    * `choices`: A list containing `sent_more`, `sent_less`.
    * `stereo_antistereo`: The stereotypical direction of the pair.
    * `bias_type`: The type of biases present in the example.
* common_prefix:
    * `prompt`: The context of the sentences, including the common prefix between `sent_more`, `sent_less`
    * `choices`: A list containing truncated versions of `sent_more`, `sent_less`.
    * `stereo_antistereo`: The stereotypical direction of the pair.
    * `bias_type`: The type of biases present in the example.
* mask: 
    * `prompt`. The context of the sentences + `<MASK>` + the common suffix of `sent_more`, `sent_less`.
    * `choices`: A list containing the differing tokens between `sent_more`, `sent_less`.
    * `stereo_antistereo`: The stereotypical direction of the pair.
    * `bias_type`: The type of biases present in the example.

## Issues
These issues are fixed in crows_pairs_themis.csv

No. 14: missing dot in `sent_less` \
No. 22: missing dot in `sent_more` \
No. 582: capitalized james in `sent_less` \
No. 650: removed unecessary leading dot in `sent_less` \
No. 833: replaced comma with dot in `sent_less` \
No. 949: missing dot in `sent_less` \
No. 982: missing dot in `sent_less` \
No. 1017: missing dot in `sent_less` \
No. 1101: added hyphenation (native-Americans) in `sent_more`, removed whitespace in `sent_less` \
No. 1157: fixed capitalization in `sent_less` \
No. 1172: fixed capitalization and typo (defdant)
