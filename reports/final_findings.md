# Final Findings — Diabetes Readmission Risk ML Project

> **Status:** Created in Phase 1 as a placeholder. Content will be populated progressively as phases are completed.
>
> **Rule:** No results, metrics, or conclusions are written until they are actually computed.

---

## Overview

> TODO: Write after model evaluation is complete.

---

## Problem Framing Canvas

| Attribute | Detail |
|-----------|--------|
| **Stakeholder** | Hospital planning / healthcare decision-support stakeholders |
| **Decision need** | Understand and identify readmission risk patterns |
| **Primary lens** | Readmission Risk |
| **Unit of analysis** | TODO: Confirm after dataset inspection |
| **Prediction target** | TODO: Define after EDA |
| **Inputs** | Historical patient and encounter information available at prediction point |
| **Output** | Readmission-risk classification (and optionally, predicted probability) |
| **Potential value** | Resource planning, risk prioritisation, follow-up planning, investigation of high-risk groups |

> **Important:** "Potential value" does not mean demonstrated clinical impact. This requires prospective clinical validation not performed in this project.

---

## Workflow

```
Business Problem
     ↓
Primary Decision Lens (Readmission Risk)
     ↓
Target Definition (documented in decision_log.md DEC-003)
     ↓
Data Understanding (Notebook 01)
     ↓
Data Quality Assessment (Notebook 01)
     ↓
Exploratory Data Analysis (Notebook 02)
     ↓
Data Cleaning (Notebook 03)
     ↓
Feature Engineering (Notebook 03)
     ↓
Train / Validation / Test Strategy (decision_log.md DEC-005)
     ↓
Preprocessing Pipeline (Notebook 03)
     ↓
Baseline Model (Notebook 04)
     ↓
Alternative Classification Models (Notebook 04)
     ↓
Model Evaluation (Notebook 05)
     ↓
Error Analysis (Notebook 05)
     ↓
Feature Interpretation (Notebook 05)
     ↓
Healthcare / Business Interpretation (below)
     ↓
Recommendation (below)
     ↓
Limitations (below)
     ↓
Responsible AI Considerations (below)
```

---

## Model Comparison

> TODO: Populate after Notebook 05.

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | PR-AUC | Notes |
|-------|----------|-----------|--------|----|---------|--------|-------|
| Dummy Classifier | TODO | TODO | TODO | TODO | TODO | TODO | Statistical baseline |
| Logistic Regression | TODO | TODO | TODO | TODO | TODO | TODO | |
| Decision Tree | TODO | TODO | TODO | TODO | TODO | TODO | |
| Random Forest | TODO | TODO | TODO | TODO | TODO | TODO | |
| XGBoost | TODO | TODO | TODO | TODO | TODO | TODO | |

*All values from actual computed outputs. No values are fabricated.*

---

## Key Findings

> TODO: Populate after analysis is complete.

---

## Business Interpretation

> TODO: Populate after model evaluation and interpretation are complete.

---

## Recommendation

> TODO: Populate after analysis is complete.

The recommendation will answer: What can the hospital reasonably learn from this analysis?

It will connect:
- Data evidence
- Model performance
- Error analysis
- Feature interpretation
- Responsible AI considerations

---

## Limitations

> TODO: Expand after analysis is complete. Core limitations include:

- Retrospective dataset (1999–2008) — may not generalise to modern settings
- Class imbalance affects metric interpretation
- Missing and coded data introduce uncertainty
- Model identifies associations, not causes
- No prospective clinical validation
- Performance may vary across demographic subgroups
- External factors (socioeconomic, follow-up support) not captured

---

## Responsible AI

> TODO: Populate after fairness analysis in Phase 10.

Core positions:
- This is not a diagnostic tool
- No clinical deployment claims are made
- Fairness/subgroup analysis performed where data permits
- Patient privacy protected throughout
- Human oversight required for any real-world use

---

*Document maintained throughout project. Last updated: 2026-09-19 (Phase 1 initialization)*
