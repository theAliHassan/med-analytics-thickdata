# Project Proposal: Investigation on Using Thick Data Analytics in Medical Paradigm

## Table of Contents
- [1. Project Definition](#1-project-definition)
  - [Working Title](#working-title)
  - [Core Problem](#core-problem)
  - [High-Level Approach](#high-level-approach)
- [2. Thesis Structure](#2-thesis-structure)
  - [Chapter 2 - Investigate ML Models in Medicine](#chapter-2---investigate-ml-models-in-medicine)
  - [Chapter 3 - Thick Data Analytics in Medicine](#chapter-3---thick-data-analytics-in-medicine)
  - [Chapter 4 - Augmentation & Fine-Tuning](#chapter-4---augmentation--fine-tuning)
- [3. Expected Outcomes](#3-expected-outcomes)
- [4. Fall Timeline – MSc Thesis (Weeks 1–10) ](#4-fall-timeline--msc-thesis-weeks-110)
---

## 1. Project Definition

### Working Title
**Investigation on Using Thick Data Analytics in Medical Paradigm**

### Core Problem
The project addresses the challenge of achieving reliable machine learning from small, high-quality ("thick") medical data, particularly when large labeled datasets are scarce.

### High-Level Approach
The research will be conducted in stages:

1. Establish machine learning baselines in medicine, with an emphasis on imaging using CNNs.  
2. Investigate "thick data analytics" by using few-shot learning methods that incorporate clinical knowledge.  
3. Augment and fine-tune models to quantify performance improvements.  
4. Conclude with findings and outline future work.

---

## 2. Thesis Structure

The proposal is grounded in **Chapter 2 experiments** and outlines plans for **Chapters 3 and 4**.

---

### Chapter 2 - Investigate ML Models in Medicine
This chapter details initial experiments with standard machine learning models.  
- Select a dataset (e.g., chest/COVID imaging).  
- Run CNN baselines.  
- Report on the strengths and limitations of these models.  
- Take a position on their effectiveness.

---

### Chapter 3 - Thick Data Analytics in Medicine
This chapter will focus on few-shot learning approaches.  
- Implement few-shot setups using anchor/positive/negative formulation.  
- Use loss functions such as **triplet loss**.  
- Compare results to the CNN baseline from Chapter 2.  
- Analyze **gains and trade-offs**.

---

### Chapter 4 - Augmentation & Fine-Tuning
This chapter explores strategies to **improve model performance**.  
- Investigate augmentation pipelines, including:
  - YOLO-based augmentation  
  - ROI-based augmentation  
- Apply fine-tuning techniques.  
- Quantify how these methods enhance performance and provide a comprehensive report.

---

# 3. Expected Outcomes
- Demonstration of reliable ML performance on small, high-quality datasets.
- Experimental comparison between CNN baselines, few-shot approaches, and augmentation strategies.
- Recommendations for integrating clinical heuristics into ML workflows.
- Tangible, well-documented open-source repository.

---

# 4. Fall Timeline – MSc Thesis (Weeks 1–10)

| **Week** | **Key Tasks** |
|-----------|---------------|
| **Week 1** | - Create **public GitHub repository** with required structure:<br>  &nbsp;&nbsp;`/writing`, `/prototyping`, `/docs`, `/papers`.<br>- Add `week01/` subfolders to each directory.<br>- Upload **proposal draft** and **baseline plan**.<br>- Add 3–5 **seed papers** on few-shot learning, triplet loss, and CNNs in medicine to `/papers/week01/`.<br>- Push an **environment-check notebook** to `/prototyping/week01/`.<br>- Share links to online **timeline** and **mind map** with supervisor.<br>- Email supervisor to **book first bi-weekly Monday meeting**. |
| **Week 2** | - Obtain dataset (e.g., chest imaging) with supervisor's guidance.<br>- Set up **data loader and preprocessing scripts**.<br>- Perform **exploratory data analysis**: visualize sample images, summarize class distribution.<br>- Document everything in `/prototyping/week02/`. |
| **Week 3** | - Build and train a **baseline CNN** for the medical imaging task.<br>- Record **initial performance metrics**: Accuracy, F1-score, AUC.<br>- Save model checkpoints and logs.<br>- Document in `/prototyping/week03/` with clear narrative and visualizations. |
| **Week 4** | - Analyze baseline CNN results: identify **strengths, weaknesses, limitations**.<br>- Begin **Chapter 2 writing** in `/writing/week04/`.<br>- Prepare tables and plots for proposal.<br>- Push updated code and documentation to GitHub. |
| **Week 5-6** | - Finalize **Chapter 2 CNN baseline experiments**.<br>- Add detailed narrative and citations.<br>- Continue refining data preprocessing and model improvements if needed. |
| **Week 7-8** | - Start **Chapter 3 planning** (few-shot learning strategies).<br>- Draft experimental design and comparison framework.<br>- Explore initial augmentation concepts for Chapter 4. |
| **Week 9-10** | - Compile **proposal document**:<br>  &nbsp;&nbsp;- Chapter 2: Completed CNN experiments and analysis.<br>  &nbsp;&nbsp;- Chapter 3 & 4: Planned methodology and references.<br>- Submit **final proposal**.<br>- Ensure GitHub reflects **weekly progress**: writing, prototyping, and papers folders. |

---

**Notes:**
- **Fall = Proposal (50%)**, **Winter = Prototyping (50%)**.
- Update GitHub **weekly** with clear commits and documentation.
- Bi-weekly Monday meetings (30–60 min) in 8:30 AM – 2:00 PM window.
- Online timeline and mind map must be **maintained and shared**.
