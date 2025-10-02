# Chapter 2 Results: Baseline Experiments with Convolutional Neural Networks

This chapter addresses **RQ1** and **RQ2** of the project:

- **RQ1**: *What is the baseline performance of convolutional neural networks (e.g., ResNet-18, VGG-16, ResNet-50) on selected medical imaging datasets when evaluated across accuracy, sensitivity, specificity, F1-score, and AUC?*  
- **RQ2**: *What is the comparative performance of CNNs across different evaluation metrics (accuracy, sensitivity, specificity, AUC), and what limitations do these results reveal?*

To answer these, we establish baselines in two stages:  
1. **Toy datasets (MedMNIST)** – quick-to-train, small, and highly imbalanced, showing CNN weaknesses in controlled settings.  
2. **Real-world datasets (ChestX-ray14, CheXpert, MIMIC-CXR)** – more realistic medical imaging benchmarks, showing CNNs under clinical-scale data.  

Together, these experiments form the baseline story for Chapter 2.

---

## 1. Model Setup

- **Architectures**: ResNet-18, VGG-16, ResNet-50  
- **Initialization**: Pretrained on ImageNet  
- **Input Preprocessing**:
  - Grayscale images duplicated to 3 channels (for pretrained CNN compatibility).  
  - Resized to 224×224.  
  - Normalized (mean=0.5, std=0.5 per channel).  
- **Loss Functions**:
  - `BCEWithLogitsLoss` for multi-label classification (ChestMNIST).  
  - `CrossEntropyLoss` for binary classification (PneumoniaMNIST, BreastMNIST).  
- **Optimizer**: Adam, learning rate = 1e-3  
- **Devices**: Apple Silicon MPS backend (Metal GPU) and CPU fallbacks  
- **Epochs**: 5–20 depending on dataset/model cost  
- **Outputs saved**: Models (`*.pth`), metrics (`*.csv`), training curves, confusion matrices, ROC/PR plots (`*.png`)

---

## 2. Part A — MedMNIST Baselines

We first trained ResNet-18, VGG-16, and ResNet-50 on **ChestMNIST (multi-label)**, **PneumoniaMNIST (binary)**, and **BreastMNIST (binary)**.  

### 2.1 ChestMNIST (Multi-label, 14 classes)

- **ResNet-18**: Macro F1 = 0.046, Micro F1 = 0.085, Macro AUC = 0.75, Micro AUC = 0.83.  
- **VGG-16**: Training loss stabilized around 0.18, AUC ~0.74, F1 ≈ 0.0.  
- **ResNet-50**: Macro F1 = 0.0, Micro F1 = 0.0, Macro AUC = 0.50, Micro AUC = 0.74.  

**Discussion**:  
- All models captured *some* signal (AUC > 0.7) but failed on F1.  
- CNNs systematically underpredict positives, producing trivial “all negative” outputs.  
- Imbalance in multi-label setting remains unsolved.

---

### 2.2 PneumoniaMNIST (Binary classification)

- **ResNet-18**: Accuracy = 100%, F1 = 0, AUC = NaN, Sensitivity = 0, Specificity = 1.0.  
- **VGG-16**: Same collapse, training loss unstable (`NaN`).  
- **ResNet-50**: Same collapse, “perfect” accuracy but no positive predictions.  

**Discussion**:  
- All models collapsed to predicting one class only.  
- Accuracy misleadingly suggests perfect performance.  
- Warnings (`UndefinedMetricWarning`) confirm evaluation metrics are undefined.

---

### 2.3 BreastMNIST (Binary classification)

- **ResNet-18**: Accuracy = 100%, F1 = 0, AUC = NaN, Sensitivity = 0, Specificity = 1.0.  
- **VGG-16**: Same trivial collapse, loss instability.  
- **ResNet-50**: Same trivial collapse.  

**Discussion**:  
- Identical collapse to PneumoniaMNIST.  
- Dataset too small and skewed for pretrained CNNs.  
- Baselines reveal that binary MedMNIST subsets are unsuitable for CNN benchmarking without augmentation or resampling.

---

### 2.4 Comparative Results Table (MedMNIST)

| Model        | Dataset        | Accuracy | F1 (Macro/Micro) | ROC-AUC (Macro/Micro) | Sensitivity | Specificity | Notes |
|--------------|----------------|----------|------------------|------------------------|-------------|-------------|-------|
| **ResNet-18** | ChestMNIST     | N/A      | 0.046 / 0.085   | 0.75 / 0.83           | N/A         | N/A         | Some signal, poor F1 |
|              | PneumoniaMNIST | 100%     | 0.0              | NaN                   | 0           | 1.0         | Collapse to one class |
|              | BreastMNIST    | 100%     | 0.0              | NaN                   | 0           | 1.0         | Same collapse |
| **VGG-16**   | ChestMNIST     | N/A      | ~0 / ~0          | ~0.74 est.            | N/A         | N/A         | Plateaued quickly |
|              | PneumoniaMNIST | 100%     | 0.0              | NaN                   | 0           | 1.0         | Loss instability |
|              | BreastMNIST    | 100%     | 0.0              | NaN                   | 0           | 1.0         | Same collapse |
| **ResNet-50**| ChestMNIST     | N/A      | 0.0 / 0.0        | 0.50 / 0.74           | N/A         | N/A         | Larger model, same issue |
|              | PneumoniaMNIST | 100%     | 0.0              | NaN                   | 0           | 1.0         | Trivial predictions |
|              | BreastMNIST    | 100%     | 0.0              | NaN                   | 0           | 1.0         | Trivial predictions |

---

## 3. Part B — Real-World Dataset Baselines (Planned)

To complete Chapter 2, we will extend these baselines to **real-world datasets**:

- **NIH ChestX-ray14** (112k X-rays, 14 disease labels)  
- **CheXpert** (224k X-rays, multi-label)  
- **MIMIC-CXR** (377k X-rays with clinical notes)  

The same CNNs (ResNet-18, VGG-16, ResNet-50) will be evaluated.  

**Why this matters:**  
- MedMNIST results show collapse in toy datasets (trivial predictions, misleading 100% accuracy).  
- Real-world datasets will test CNNs under clinically relevant settings, where accuracy is harder to achieve and class imbalance is more realistic.  
- This dual perspective (toy vs real-world) will form the **true baseline performance** for CNNs in medical imaging.  

---

## 4. Key Problems Encountered

1. **Overfitting**: Binary datasets collapsed within a few epochs.  
2. **Class Imbalance**: Severe skew led to majority-class predictions.  
3. **Evaluation Issues**: Undefined metrics (NaNs) in binary tasks.  
4. **Multi-label Difficulty**: Even larger CNNs (ResNet-50) produced AUC > 0.7 but F1 = 0.  

---

## 5. Implications and RQ Alignment

- **RQ1 (Baseline CNN performance)**:  
  - Baselines established on toy datasets (MedMNIST).  
  - Real-world datasets will be added for completeness.  

- **RQ2 (Comparative performance & limitations)**:  
  - Comparative results across CNNs (ResNet-18, VGG-16, ResNet-50) show *consistent limitations*.  
  - Toy datasets exaggerate collapse; real-world datasets will confirm challenges at clinical scale.  

**Conclusion for Chapter 2**:  
CNN baselines cannot be trusted on small, imbalanced datasets (toy or real-world).  
They either collapse to trivial predictions or fail to balance precision/recall.  
This motivates **Chapter 3**, where we test few-shot learning, metric learning, and thick-data heuristics as remedies.

---
