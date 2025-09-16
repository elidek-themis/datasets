#### Counterfactual Inputs Datasets (CFI)

| Dataset | Size | Bias Type | Metric |URL | Reference
| --- | --- | --- | --- | --- | --- |
| **CrowS-Pairs** | 1,508 | age, disability, gender, nationality, physical appearance, race, religion, sexual orientation, socioeconomic status | Pseudo-log-likelihood |[Link](https://github.com/nyu-mll/crows-pairs/) |  Nikita Nangia et al. [CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models](https://arxiv.org/abs/2010.00133). 2020. arXiv: 2010.00133 [cs.CL]|
| **StereoSet** | 16,995 | gender, race, profession, religion | lms, ss, iCAT |[Link1](https://github.com/McGill-NLP/bias-bench), [Link2](https://github.com/moinnadeem/stereoset) | Moin Nadeem, Anna Bethke, and Siva Reddy. [StereoSet: Measuring stereotypical bias in pretrained language models](https://arxiv.org/abs/2004.09456.). 2020. arXiv: 2004.09456 [cs.CL].|
| **WinoQueer** | 45,540 | sexual orientation | Modified pseudo-log-likelihood | [Link](https://github.com/katyfelkner/winoqueer) | Virginia K. Felkner et al. WinoQueer: [A Community-in-the-Loop Benchmark for Anti-LGBTQ+ Bias in Large Language Models](https://arxiv.org/abs/2306.15087). 2024. arXiv: 2306.15087 [cs.CL].|
| **RedditBias** | 11,873 | gender, race, religion, sexual orientation | Pseudo-log-likelihood |[Link](	https://github.com/umanlp/RedditBias)| Soumya Barikeri et al. [RedditBias: A Real-World Resource for Bias Evaluation and Debiasing of Conversational Language Models](https://arxiv.org/abs/2106.03521). 2021. arXiv: 2106.03521 [cs.CL].|
| **Equity Evaluation Corpus (EEC)** | 4,320 | gender, religion | Pseudo-log-likelihood |[Link](http://saifmohammad.com/WebPages/Biases-SA.html)| Svetlana Kiritchenko and Saif M. Mohammad. [Examining Gender and Race Bias in Two Hundred Sentiment Analysis Systems](https://arxiv.org/abs/1805.04508). 2018. arXiv: 1805.04508 [cs.CL].|

#### Counterfactual Inputs Datasets (CoRef)

| Dataset | Size | Bias Type | Metric | URL | Reference
| --- | --- | --- | --- | --- | --- |
| **WinoGender** | 720 | gender | Accuracy | [Link](https://github.com/rudinger/winogender-schemas)| Rachel Rudinger et al. [Gender Bias in Coreference Resolution](https://arxiv.org/abs/1804.09301). 2018. arXiv: 1804 . 09301 [cs.CL].|
| **WinoBias** | 3,160 | gender | Accuracy | [Link](https://github.com/uclanlp/corefBias/tree/master/WinoBias/wino) | Jieyu Zhao et al. [Gender Bias in Coreference Resolution: Evaluation and Debiasing Methods](https://arxiv.org/abs/1804.06876). 2018. arXiv: 1804.06876 [cs.CL].|
| **WinoBias+** | 1,367 | gender | Accuracy |[Link](https://github.com/vnmssnhv/NeuTralRewriter) | Eva Vanmassenhove, Chris Emmery, and Dimitar Shterionov. [NeuTral Rewriter: A Rule-Based and Neural Approach to Automatic Rewriting into Gender-Neutral Alternatives](https://arxiv.org/abs/2109.06105). 2021. arXiv: 2109.06105 [cs.CL].|
| **GAP** | 8,908 | gender | OverallF1, Bias Score (FemF1 / MascF1) |[Link](https://github.com/google-research-datasets/gap-coreference) | Kellie Webster et al. [Mind the GAP: A Balanced Corpus of Gendered Ambiguous Pronouns](https://arxiv.org/abs/1810.05201). 2018. arXiv: 1810.05201 [cs.CL].|

#### Generative

| Dataset | Size | Bias Type | Metric | URL | Reference
| --- | --- | --- | --- | --- | --- |
| **BBQ** | 58,492 | age, disability, gender, nationality, physical appearance, race, religion, sexual orientation, socioeconomic status | Accuracy, sDIS, sAMB |[Link](https://github.com/nyu-mll/BBQ)| Alicia Parrish et al. [BBQ: A Hand-Built Bias Benchmark for Question Answering](https://arxiv.org/abs/2110.08193). 2022. arXiv: 2110.08193 [cs.CL].|
| **UnQover** | 10,000 | gender, nationality, religion, sexual orientation | Bias Score, Comparative Bias Score, Subject-Attribute Bias, Model Bias Intensity, Count-Based Metric |	[Link](https://github.com/allenai/unqover)| Tao Li et al. [UnQovering Stereotyping Biases via Underspecified Questions](https://arxiv.org/abs/2010.02428). 2020. arXiv: 2010.02428 [cs.CL].|
| **HONEST** | 420 | gender | HONEST score |[Link](https://github.com/MilaNLProc/honest)| Debora Nozza, Federico Bianchi, and Dirk Hovy. [HONEST: Measuring Hurtful Sentence Completion in Language Models](https://aclanthology.org/2021.naacl-main.191/). In: Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. Ed. by Kristina Toutanova et al. Online: Association for Computational Linguistics, June 2021, pp. 2398–2406. doi: 10.18653 / v1 / 2021 . naacl-main. 191.|
