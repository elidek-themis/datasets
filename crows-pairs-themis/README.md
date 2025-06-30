Transformed CrowS-Pairs dataset into a combined prompt with the original prompt with the common prefix of the stereo and anti stereo contiinuations plus the two continuations.

Data taken from https://github.com/nyu-mll/crows-pairs

## The Dataset

The dataset along with its annotations is in [crows_pairs_anonymized.csv](https://github.com/nyu-mll/crows-pairs/blob/master/data/crows_pairs_anonymized.csv). It consists of 1,508 examples covering nine types of biases: race/color, gender/gender identity, sexual orientation, religion, age, nationality, disability, p>

Each example is a sentence pair, where the first sentence is always about a historically disadvantaged group in the United States and the second sentence is about a contrasting advantaged group. The first sentence can _demonstrate_ or _violate_ a stereotype. The other sentence is a minimal edit of the first sentence>
- `combined_prompt`: The context input and the common prefix.
- `stereotype_continuation`: The stereotypical continuation.
- `antistereotype_continuation`: The anti-stereotypical continuation.
- `stereo_antistereo`: The stereotypical direction of the pair. A `stereo` direction denotes that `sent_more` is a sentence that _demonstrates_ a stereotype of a historically disadvantaged group. An `antistereo` direction denotes that `sent_less` is a sentence that _violates_ a stereotype of a historically disadvant>
- `bias_type`: The type of biases present in the example.
- `annotations`: The annotations of bias types from crowdworkers.
- `anon_writer`: The _anonymized_ id of the writer.
- `anon_annotators`: The _anonymized_ ids of the annotators.
