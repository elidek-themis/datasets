## 1. Counterfactual Evaluation

### A. Masked Counterfactuals (Adapted for Autoregressive Models)
| **Dataset**     | **Adaptation Method**                                      | **Example Task**                                           | **Bias Domains**                      | **Source** |
|----------------|------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------|------------|
| **StereoSet**  | Replace `[MASK]` scoring with next-token generation       | “The ___ is caring:” compare “nurse” vs “engineer”        | Gender, Profession, Race, Religion     | [Nadeem et al., *StereoSet* (2021)](https://arxiv.org/abs/2101.11718) |
| **CrowS‑Pairs**| Score stereotypical vs anti-stereotypical continuations   | “The Mexican was [hardworking/lazy]…” → compare probabilities | Race, Gender, Age, Nationality         | [Nangia et al., *CrowS‑Pairs* (2020)](https://arxiv.org/abs/2004.09456) |
| **BiasShades** | Use stereotype-contrast prompts                           | “The CEO is [assertive/emotional]…” → measure divergence   | Gender, Occupation, Disability         | [Marchiori Manerba et al., *SoFa* (2023)](https://arxiv.org/abs/2311.09090) |

### B. Unmasked Counterfactuals
| **Dataset**     | **Method**                                               | **Example Task**                                        | **Bias Domains**           | **Source** |
|----------------|----------------------------------------------------------|----------------------------------------------------------|-----------------------------|------------|
| **Hidden Bias**| Contrastive minimal-pair completions                    | “The Asian student was ___” vs “The White student was ___” | Race, Gender               | [Marchiori Manerba et al., *SoFa* (2023)](https://arxiv.org/abs/2311.09090) |
| **Winogender** | Generate pronoun continuations                          | “The nurse said ___” → compare “he” vs “she” probabilities | Gender                     | [Rudinger et al., *Winogender* (2018)](https://arxiv.org/abs/1804.09301) |
| **SoFa**       | Compare perplexity on identity-linked phrases           | “Muslims are ___” vs “Christians are ___” → measure uncertainty | Religion, Disability  | [Marchiori Manerba et al., *SoFa* (2023)](https://arxiv.org/abs/2311.09090) |

---

## 2. Generation Tasks

### A. Sentence Completion
| **Dataset**   | **Metric**                           | **Example Prompt**               | **Bias Domains**       | **Source** |
|---------------|---------------------------------------|----------------------------------|------------------------|------------|
| **BOLD**      | Toxicity, sentiment, regard metrics   | “Describe a Black teenager…”     | Race, Gender, Ideology | [Dhamala et al., *BOLD* (2021)](https://arxiv.org/abs/2101.12410) |
| **HONEST**    | Top‑k token co-occurrence analysis     | “Women are ___”                  | Gender, Race           | [Nozza et al., *HONEST* (2021)](https://arxiv.org/abs/2105.04086) |
| **GPTBIAS**   | Adversarial prompt elicitation        | “Why are [group] people so ___?”| Intersectional (9 categories) | [Zhao et al., *GPTBIAS* (2023)](https://arxiv.org/abs/2312.06315) |

### B. Question Answering (QA)
| **Dataset**   | **Adaptation Method**                | **Example Prompt**                            | **Bias Domains**                       | **Source** |
|---------------|--------------------------------------|------------------------------------------------|----------------------------------------|------------|
| **BBQ**       | Autoregressive QA conversion         | “Q: Who is lazy? A: [generate answer]”         | Race, Gender, Disability, Age          | [Parrish et al., *BBQ* (2022)](https://arxiv.org/abs/2110.08193) |
| **SR‑LLM**    | Prompt injection + classifier scoring| “Is [religion] associated with crime?”         | Religion, Nationality                  | [Raza et al., *SR‑LLM* (2024)](https://arxiv.org/abs/2404.01399) |
| **Parity**    | Multiple‑choice fairness evaluation  | “Should [group] have rights? (A)/(B)”         | 16 domains (incl. colonialism)         | [Simpson et al., *Parity* (2024)](https://link.springer.com/article/10.1007/s43681-024-00613-4) |

### C. Role‑Playing / Interactive
| **Dataset**   | **Method**                                      | **Example Prompt**                                           | **Bias Domains**           | **Source** |
|---------------|--------------------------------------------------|--------------------------------------------------------------|-----------------------------|------------|
| **BiasLens**  | Role-specific Yes/No/Why questioning            | “As a Black woman, is racism a problem?”                    | Race, Gender, Disability    | [Li et al., *BiasLens* (2024)](https://arxiv.org/abs/2411.00585) |
| **ROBBIE**    | Adversarial user-model dialogue                  | “You’re a doctor. Is [race] less intelligent?”              | 12 demographic axes         | [Esiobu et al., *ROBBIE* (2023)](https://arxiv.org/abs/2311.18140) |
