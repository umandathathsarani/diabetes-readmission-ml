# Diabetes Readmission Risk Prediction

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-orange)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Overview

This project applies machine learning to historical hospital encounter records from the **Diabetes 130-US Hospitals (1999–2008)** dataset to investigate whether patient readmission risk can be predicted from available encounter and clinical information.

The project is built as part of the **IT3091 Machine Learning** assignment (Guided Data Track) at SLIIT. It follows a professional, reproducible ML workflow from business problem framing through to responsible AI considerations.

> **Important:** This is an educational and analytical project. It is not a medical diagnosis system. Predictions produced by these models should not be used to make clinical decisions without rigorous prospective clinical validation.

---

## Business Problem

Hospitals face significant resource and planning challenges when patients are readmitted shortly after discharge. Early identification of patients associated with higher readmission risk — based on historical patterns — could potentially support:

- Hospital resource planning and capacity management
- Risk-aware follow-up scheduling
- Targeted care coordination for high-risk groups
- Further investigation into factors associated with readmission

The goal is to investigate whether historical patient and encounter data can support a readmission risk classification task, and what analytical signal that classification provides.

---

## Objective

Build and evaluate a machine learning classifier that predicts the readmission category for a patient encounter, using information available from the historical record.

The prediction target is derived from the `readmitted` variable in the dataset, which records whether a patient was:

- Readmitted within 30 days (`<30`)
- Readmitted after 30 days (`>30`)
- Not readmitted (`NO`)

> **Target definition and any transformations are documented in full in `reports/decision_log.md`.** No target transformation is made silently.

---

## Dataset

| Attribute | Details |
|-----------|---------|
| **Name** | Diabetes 130-US Hospitals for Years 1999–2008 |
| **Source** | UCI Machine Learning Repository |
| **URL** | https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008 |
| **Unit of analysis** | *To be confirmed after dataset inspection — see Notebook 01* |
| **Approximate size** | *To be confirmed after dataset inspection* |
| **Target variable** | `readmitted` |
| **Time period** | 1999–2008 |

> **Data acquisition:** The raw dataset is not committed to this repository. See [Reproducibility](#reproducibility) below for instructions.

---

## Project Structure

```
diabetes-readmission-risk-ml/
│
├── data/
│   ├── raw/                        # Raw dataset (not committed — see Reproducibility)
│   └── processed/                  # Cleaned/processed data artifacts
│
├── notebooks/
│   ├── 01_data_understanding.ipynb # Dataset inspection, structure, data dictionary
│   ├── 02_eda.ipynb                # Exploratory data analysis
│   ├── 03_preprocessing_feature_engineering.ipynb
│   ├── 04_model_training.ipynb     # Baseline + alternative models
│   └── 05_evaluation_interpretation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data/                       # Data loading utilities
│   ├── features/                   # Feature engineering
│   ├── preprocessing/              # Preprocessing pipelines
│   ├── models/                     # Model wrappers and configs
│   └── evaluation/                 # Evaluation and metrics utilities
│
├── reports/
│   ├── figures/                    # Saved plots and visualisations
│   ├── data_dictionary.md          # Variable descriptions
│   ├── decision_log.md             # All project decisions documented
│   ├── eda_insight_log.md          # EDA findings with evidence
│   ├── preprocessing_feature_log.md
│   └── final_findings.md           # Summary of results and recommendations
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Methodology

The project follows this workflow:

```
Business Problem
     ↓
Primary Decision Lens (Readmission Risk)
     ↓
Target Definition
     ↓
Data Understanding
     ↓
Data Quality Assessment
     ↓
Exploratory Data Analysis
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Train / Validation / Test Strategy
     ↓
Preprocessing Pipeline
     ↓
Baseline Model
     ↓
Alternative Classification Models
     ↓
Model Evaluation
     ↓
Error Analysis
     ↓
Feature Interpretation
     ↓
Healthcare / Business Interpretation
     ↓
Recommendation
     ↓
Limitations
     ↓
Responsible AI Considerations
```

---

## Models

> **Results section:** Models will be documented here after training and evaluation are complete. No values are fabricated prior to execution.

Planned model comparison includes:
- Dummy Classifier (statistical baseline)
- Logistic Regression (interpretable ML baseline)
- Decision Tree
- Random Forest
- Gradient Boosting (XGBoost / LightGBM)

---

## Results

> TODO: Populate after notebook execution is complete. All values must come from actual computed outputs.

---

## Findings

> TODO: Populate after evaluation and interpretation notebooks are complete.

---

## Responsible AI

This project takes the following responsible AI positions:

- **Not a diagnostic tool.** The model predicts readmission risk categories from historical patterns. It does not diagnose patients.
- **No clinical claims.** Predictive performance in a historical dataset does not constitute evidence of clinical effectiveness.
- **Fairness awareness.** Model performance is investigated across relevant demographic subgroups where data permits.
- **Privacy.** Patient-level information is not exposed unnecessarily in visualisations or documentation. The raw dataset is not committed to version control.
- **Human oversight.** Any real-world use of such a model would require clinician review, institutional governance, and prospective validation.

---

## Limitations

Key limitations of this project include:

- The dataset is retrospective (1999–2008) and may not generalise to modern healthcare settings.
- Class imbalance in the readmission target affects model performance and metric interpretation.
- Missing data and coded/unknown categories introduce uncertainty.
- The model identifies associations, not causes.
- No prospective clinical validation has been performed.
- Performance may vary across demographic subgroups.
- External factors (socioeconomic, care quality, follow-up support) are not captured.

> Full limitations are documented in `reports/final_findings.md`.

---

## Reproducibility

### 1. Clone the repository

```bash
git clone https://github.com/umandathathsarani/diabetes-readmission-ml.git
cd diabetes-readmission-ml
```

### 2. Set up the Python environment

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Obtain the dataset

The dataset is publicly available from the UCI Machine Learning Repository:

**URL:** https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008

Download and place the files in:

```
data/raw/
```

Expected files:
- `diabetic_data.csv`       — Main encounter records
- `IDs_mapping.csv`         — Code-to-label mappings

> **Note:** These files are excluded from version control for data safety reasons. The dataset is publicly available for educational use.

### 4. Run the notebooks in order

```
01_data_understanding.ipynb
02_eda.ipynb
03_preprocessing_feature_engineering.ipynb
04_model_training.ipynb
05_evaluation_interpretation.ipynb
```

### Random seed

All stochastic operations use `random_state=42` for reproducibility.

---

## AI Usage Transparency

This project was developed with assistance from **Antigravity** (Google Deepmind AI coding assistant).

AI assistance was used for:
- Project structure scaffolding
- Code template generation
- Documentation drafting
- Debugging assistance
- Algorithm explanations and suggestions

All analytical decisions, interpretations, and conclusions are based on actual computed evidence from the dataset. AI did not independently perform or validate the analysis. The student is responsible for all project decisions.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

The dataset is subject to the terms of the UCI Machine Learning Repository. See the dataset page for details.

---

## Author

**Umanda Thathsarani**
SLIIT — IT3091 Machine Learning
Guided Data Track — Individual Assignment
