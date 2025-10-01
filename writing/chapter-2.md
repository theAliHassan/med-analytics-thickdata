# Chapter 2 Results: Baseline Experiments with ResNet-18

This chapter presents the baseline experiments conducted on three MedMNIST datasets: **ChestMNIST**, **PneumoniaMNIST**, and **BreastMNIST**. The objective was to establish a performance baseline using a standard convolutional neural network (CNN), and to highlight the **strengths and limitations** of this approach when applied to small-scale, imbalanced medical datasets.

---

## 1. Model Setup

- **Architecture**: ResNet-18  
- **Initialization**: Pretrained on ImageNet (`weights="IMAGENET1K_V1"`)  
- **Input Preprocessing**:
  - Original grayscale images duplicated to 3 channels for compatibility.
  - Normalized to mean=0.5, std=0.5 per channel.
- **Loss Functions**:
  - `BCEWithLogitsLoss` for multi-label classification (ChestMNIST).
  - `CrossEntropyLoss` for binary classification (PneumoniaMNIST, BreastMNIST).
- **Optimizer**: Adam, learning rate = 1e-3  
- **Device**: Apple Silicon MPS (Metal GPU) with mixed precision (`torch.amp.autocast`)  
- **Epochs**: 20 per dataset  
- **Seeded training** for reproducibility  
- **Outputs saved**:
  - Models (`*.pth`)
  - Metrics (`*.csv`)
  - Training curves, confusion matrices, ROC and PR plots (`*.png`)

---

## 2. Results by Dataset

### 2.1 ChestMNIST (Multi-label, 14 classes)

- **Metrics**:
  - Macro F1: ~0.046
  - Micro F1: ~0.085
  - Macro ROC-AUC: ~0.75
  - Micro ROC-AUC: ~0.83

- **Observations**:
  - ROC curves indicate that some classes achieve moderate separability, while others perform poorly.
  - Extremely low F1 scores reflect severe **class imbalance** and difficulty in detecting positives.
  - Accuracy was **not tracked**, as it is not meaningful in a multi-label setting.

- **Figures**:
  - Class balance: `results/chestmnist_class_balance.csv`
  - Training curves: `results/chestmnist_training_curves.png`
  - ROC curves: `results/chestmnist_roc_curves.png`

- **Discussion**:
  - The baseline ResNet-18 captures some signal, achieving reasonable AUC, but fails to produce balanced predictions.
  - This highlights a limitation of standard CNN baselines in **multi-label medical tasks**.

---

### 2.2 PneumoniaMNIST (Binary classification)

- **Metrics**:
  - Accuracy: 100% (train & val)
  - Sensitivity / Specificity: Undefined (all predictions collapsed to one class)
  - ROC-AUC, PR-AUC: Not computable (warnings raised)

- **Observations**:
  - Training and validation accuracy saturate instantly at 100%.
  - Confusion matrix shows the model predicts only one class → trivial solution.
  - ROC/PR curves degenerate due to lack of class separation.

- **Figures**:
  - Samples: `results/pneumoniamnist_samples.png`
  - Class balance: `results/pneumoniamnist_class_balance.csv`
  - Training curves: `results/pneumoniamnist_training_curves.png`
  - Confusion matrix: `results/pneumoniamnist_confusion_matrix.png`
  - ROC curve: `results/pneumoniamnist_roc_curve.png`
  - PR curve: `results/pneumoniamnist_pr_curve.png`

- **Discussion**:
  - The dataset is **tiny and imbalanced**, making it unsuitable for evaluating strong CNNs without augmentation or resampling.
  - Reported accuracy is misleading, exposing a critical limitation of baselines.

---

### 2.3 BreastMNIST (Binary classification)

- **Metrics**:
  - Accuracy: 100% (train & val)
  - Sensitivity / Specificity: Undefined (model predicts one class only)
  - ROC-AUC, PR-AUC: Not computable

- **Observations**:
  - Similar collapse as PneumoniaMNIST → perfect accuracy but no generalization.
  - Curves confirm trivial predictions.

- **Figures**:
  - Samples: `prototyping/week-03/results/breastmnist_samples.png`
  - Class balance: `prototyping/week-03/results/breastmnist_class_balance.csv`
  - Training curves: `prototyping/week-03/results/breastmnist_training_curves.png`
  - Confusion matrix: `prototyping/week-03/results/breastmnist_confusion_matrix.png`
  - ROC curve: `prototyping/week-03/results/breastmnist_roc_curve.png`
  - PR curve: `prototyping/week-03/results/breastmnist_pr_curve.png`

- **Discussion**:
  - Small dataset size and skew make ResNet-18 unsuitable without strong regularization.
  - Model performance is **illusory**: 100% accuracy is a result of memorization, not learning.

---

## 3. Key Problems Encountered

1. **Overfitting**:  
   - PneumoniaMNIST and BreastMNIST overfit within a few epochs, reaching perfect accuracy without meaningful discrimination.

2. **Class Imbalance**:  
   - Both binary datasets heavily skewed, collapsing the model into majority-class prediction.

3. **Evaluation Issues**:  
   - Metrics such as F1, ROC-AUC, and PR-AUC raised `UndefinedMetricWarning` when only one class was predicted.  
   - These warnings signal that metrics are meaningless in those cases.

4. **Multi-label Challenges**:  
   - ChestMNIST results show that CNN baselines struggle to balance predictions across multiple co-occurring diseases.

---

## 4. Limitations and Implications

- Standard CNN baselines (even pretrained) are **insufficient** for small, imbalanced medical datasets.  
- **Binary datasets**: Strong risk of misleading "perfect" accuracy due to data collapse.  
- **Multi-label dataset**: Baseline performance highlights need for **specialized methods** (data augmentation, resampling, thick-data heuristics).  

These limitations motivate the work in **Chapter 3**, where we will investigate approaches to overcome these issues.

---

---

## 5. VGG-16 Baseline Results

We extended the baseline experiments with **VGG-16** (pretrained on ImageNet).  
Due to the heavy computational cost of this model on 224×224 inputs, we trained it for **5 epochs** per dataset instead of 20.  

### 5.1 ChestMNIST (Multi-label, 14 classes)

- **Metrics**:
  - Train Loss decreased from ~0.27 -> ~0.18
  - Val Loss plateaued around 0.181
  - Accuracy: N/A (not meaningful for multi-label tasks)

- **Observations**:
  - Training stabilized quickly, but validation loss plateaued early.
  - Like ResNet-18, VGG-16 captured partial signal but failed to achieve balanced predictions due to extreme class imbalance.

- **Discussion**:
  - VGG-16 did not substantially improve over ResNet-18.
  - Both models show that baseline CNNs struggle with multi-label medical imaging.

---

### 5.2 PneumoniaMNIST (Binary classification)

- **Metrics**:
  - Accuracy: 100% (train & val)
  - Sensitivity / Specificity: Undefined (model predicts one class only)
  - ROC-AUC, PR-AUC: Not computable
  - Loss: `nan` throughout training

- **Observations**:
  - Model collapsed instantly to trivial all-one-class predictions.
  - Loss instability suggests numerical issues on the small, imbalanced dataset.

- **Discussion**:
  - Same collapse as ResNet-18.
  - Larger CNN capacity does not help with tiny binary medical datasets.

---

### 5.3 BreastMNIST (Binary classification)

- **Metrics**:
  - Accuracy: 100% (train & val)
  - Sensitivity / Specificity: Undefined
  - ROC-AUC, PR-AUC: Not computable
  - Loss: `nan` throughout training

- **Observations**:
  - Trivial collapse identical to PneumoniaMNIST.
  - Model overfits instantly to majority class.

- **Discussion**:
  - Confirms that toy binary datasets provide misleading "perfect" performance, regardless of CNN depth.

---

## 6. Interim Summary (ResNet-18 vs VGG-16)

- On **tiny binary datasets** (Pneumonia, Breast), both CNNs collapse to trivial predictions → metrics are meaningless.  
- On **multi-label ChestMNIST**, both CNNs achieve moderate ROC-AUC but fail to improve F1 due to severe imbalance.  
- VGG-16’s higher capacity does **not overcome the limitations** observed with ResNet-18.  
- These results emphasize the need to move beyond toy datasets and test baselines on **real-world medical imaging benchmarks** (ChestX-ray14, CheXpert) before introducing advanced methods in Chapter 3.
