# Model Evaluation Log — Diabetes Readmission Risk ML Project

> **Note on Imbalance:** The positive class (<30 days readmission) only accounts for ~11% of the dataset. Therefore, accuracy is highly misleading. Models are evaluated based on Recall, Precision, and ROC-AUC.

---

## Evaluation Metrics Summary

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Notes |
|-------|----------|-----------|--------|----------|---------|-------|
| **Dummy (Baseline)** | 0.8881 | 0.0000 | 0.0000 | 0.0000 | 0.5000 | Guesses '0' every time. Shows why accuracy is a bad metric. |
| **Logistic Regression** | 0.6566 | 0.1716 | 0.5406 | 0.2605 | 0.6501 | Used `class_weight='balanced'`. Identified 54% of actual readmissions. |
| **Random Forest** | 0.6453 | 0.1733 | 0.5754 | 0.2663 | 0.6589 | Used `class_weight='balanced'` and `max_depth=10`. Highest recall (57.5%) and AUC. |

---

## Detailed Model Decisions

### 1. Dummy Classifier (Baseline)
- **Strategy:** `most_frequent`
- **Purpose:** To establish a floor for model performance. Because 89% of patients are not readmitted within 30 days, the model achieves 88.8% accuracy simply by ignoring the minority class completely. 
- **Result:** Fails to detect a single readmission (Recall = 0.00).

### 2. Logistic Regression
- **Hyperparameters:** `class_weight='balanced'`, `max_iter=1000`
- **Performance Trade-off:** By forcing the model to care about the minority class, accuracy drops from 88% to 65%. However, it successfully identifies 54% of patients who actually return within 30 days. Precision is low (17%), meaning there are many false positives.
- **Selection:** Selected as the primary model to interpret in Phase 7 due to its high transparency (coefficients) which is crucial in healthcare settings.

### 3. Random Forest Classifier
- **Hyperparameters:** `class_weight='balanced'`, `n_estimators=100`, `max_depth=10`
- **Performance Trade-off:** Performs slightly better than Logistic Regression on all metrics (Recall 57.5%, ROC-AUC 0.6589). Restricting `max_depth` prevented severe overfitting on the training data.
- **Comparison:** While the ROC-AUC is slightly higher than LR, Random Forest is harder to explain to clinicians. Logistic Regression was chosen for the final saving step because the performance gap is minimal, but the interpretability gap is large.

---

## ROC Curve Comparison
The ROC curves for both active models show they perform significantly better than the random guessing baseline, with Random Forest (AUC 0.659) slightly edging out Logistic Regression (AUC 0.650). Both are typical baseline performance figures for clinical datasets relying mostly on administrative/demographic features without deep biomarker data.

*Log updated after running Notebook 04 - 2026-09-19*
