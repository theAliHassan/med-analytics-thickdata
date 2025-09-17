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
