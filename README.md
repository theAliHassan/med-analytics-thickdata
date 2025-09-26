# Investigation on Using Thick Data Analytics in Medical Paradigm

## 📌 Overview
This MSc project explores how to achieve reliable learning from small, high-quality ("thick") data in medicine, where large labeled datasets are often scarce.  

The work progresses through:  
- **Chapter 2** – Baseline CNN experiments on medical imaging  
- **Chapter 3** – Few-shot learning with domain heuristics  
- **Chapter 4** – Augmentation & ROI-based approaches  
- **Chapter 5** – Conclusions & future work  

---

## 🗂 Repository Structure
- `writing/`  Proposal draft, chapters  
- `prototyping/`  Jupyter notebooks (week-01, week-02, …)  
- `docs/` Timeline, mind maps, notes  
- `papers/` Research papers (to be added)  

---

## 📆 Weekly Progress
- **Week 01:** Repo setup, environment check, initial proposal & timeline  
- **Week 02 (current):** Dataset selection, baseline CNN setup, updated mind map  
- ### Week 03 (current)
- ✅ Environment setup on Apple Silicon (MPS enabled).
- ✅ Saved reproducibility snapshot: [`requirements-week-03.txt`](prototyping/week-03/requirements-week-03.txt).
- ✅ Implemented results-saving pipeline (figures + model checkpoints in [`week-03/results/`](prototyping/week-03/results/)).
- ✅ Downloaded and explored MedMNIST subsets:
  - **ChestMNIST** (multi-label chest X-rays, 14 classes)  
  - **PneumoniaMNIST** (binary chest X-rays: pneumonia vs normal)  
  - **BreastMNIST** (binary ultrasound: benign vs malignant)  
- ✅ Sample visualizations (inline + saved):  
  ![ChestMNIST samples](prototyping/week-03/results/chestmnist_samples.png)  
  ![PneumoniaMNIST samples](prototyping/week-03/results/pneumoniamnist_samples.png)  
  ![BreastMNIST samples](prototyping/week-03/results/breastmnist_samples.png)  
- 🔄 Next: class balance analysis, train/val/test splits, ResNet-18 baseline training.


---

## 📊 Live Artifacts
- **Mind Map (Week 02):** [View here](docs/mindmap/Week-02-MindMap.jpg)  
- **Timeline:** [Online Timeline Link](https://lucid.app/lucidspark/2fad6656-20b7-4f39-a95c-0990db562e5e/edit?view_items=5RZRUojyXmSD%2C5RZRQqoXsTRC%2C5RZR4vbKYD9q%2C5RZRbRlaxj-w%2Coh0R6rOm6Mg0%2C5RZRdNYzQt86%2CX2ZRJQ0Knb8I%2C69ZRS7SA1n7E%2Co~ZR4xZhlQup%2CKa0Rzc64HLAM%2C5RZR59mqLbCg%2Cd-ZRYgiCt_EP%2Cs-ZRtzfBb6Rc%2C7a0RKooJqp19%2Cx~ZRLVxTPDd7&invitationId=inv_921d1c01-e7e2-4348-804a-78b9fd5b8787)  
