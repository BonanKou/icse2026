# Automating API Documentation from Crowdsourced Knowledge
This repository contains code and data for ICSE 2026 first-cycle submission: Automating API Documentation from Crowdsourced Knowledge.

## Data

- **`main_experiments/`**  
  Contains the complete experimental results of **all 48 APIs** evaluated using **AutoDoc** and the **five baselines**.

- **`retrieval_experiment.json`**  
  Stores the experimental results of the **DPR (Dense Passage Retrieval)** model.
  
- **`ablation_studies/`**  
  Includes results from ablation studies, analyzing the contribution of different components or features to the final performance.

- **`temperature_experiment/`**  
  Contains experiments on different **temperature settings**.

- **`llm_experiment/`**  
  Provides experimental results across different **LLMs** (e.g., GPT-4o, LLaMA, Mistral), comparing their performance on API documentation generation.

---

## Code

The `code/` folder provides the full implementation of **AutoDoc** and **five baseline methods**, including our proposed **SISE implementation**. 

