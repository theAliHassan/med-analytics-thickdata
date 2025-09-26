# Dataset Choice Strategy

## Overview
This project explores how to achieve reliable learning from small, high-quality ("thick") data in medicine.  
To balance **rapid prototyping** with **clinical credibility**, a two-stage dataset strategy is adopted:

1. **Phase 1 – MedMNIST Subsets (Baseline Prototyping)**  
   - **ChestMNIST** (multi-label chest X-rays, 14 classes).  
   - **PneumoniaMNIST** (binary chest X-rays: pneumonia vs normal).  
   - **BreastMNIST** (binary breast ultrasound: malignant vs benign).  

   These subsets were selected because they:  
   - Represent clinically relevant domains (chest radiology, ultrasound).  
   - Provide standardized, lightweight images (28×28) for rapid CNN prototyping.  
   - Are open-access, reproducible, and well-cited in ML research.  
   - Allow us to explore both **multi-class (ChestMNIST)** and **binary classification (PneumoniaMNIST, BreastMNIST)**.  

   **Limitations:**  
   - Images are downsampled, reducing fidelity.  
   - Small image size may omit subtle diagnostic cues used in real practice.  
   - Performance on these datasets may not reflect true clinical generalization.  

   **Role in Project:**  
   - Serve as **baseline datasets for Chapter 2**.  
   - Allow development of training pipelines, evaluation metrics, and interpretability methods (Grad-CAM).  
   - Explicitly highlight the limitations of CNN baselines, motivating Chapter 3 (few-shot learning + heuristics).  

---

2. **Phase 2 – Standard Datasets from NIH/NIST/TREC (Clinical Extension)**  
   After initial baselines are complete, experiments will be extended to higher-fidelity datasets, such as:  
   - **NIH ChestX-ray14 / NIST Chest X-ray datasets (TREC)**.  
   - **Breast ultrasound datasets curated on TREC/NIST**.  

   These datasets are more clinically realistic, with higher resolution and richer diagnostic information.  

   **Role in Project:**  
   - Validate whether the limitations observed in MedMNIST persist in real-world settings.  
   - Strengthen Chapter 2 results and ensure clinical credibility of conclusions.  

---

## Summary
- **Phase 1 (Week 3–4):** Run baselines on three MedMNIST subsets (ChestMNIST, PneumoniaMNIST, BreastMNIST).  
- **Phase 2 (Week 5+):** Extend to NIH/NIST datasets from TREC for higher-fidelity validation.  
- This progressive strategy balances feasibility, reproducibility, and clinical realism, keeping the project aligned with supervisor expectations.
