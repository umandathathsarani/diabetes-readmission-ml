<div align="center">

# Healthcare Diabetes Readmission Risk Prediction

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

*An end-to-end Machine Learning project identifying hospital patients at high risk of 30-day readmission.*

</div>

---

## 📌 Project Overview

This is an individual project developed under the **Guided Data Track** for the IT3091 Machine Learning assignment. 

The goal of this project is to build a predictive model that identifies diabetic patients who are at a high risk of returning to the hospital within 30 days of their initial discharge. By flagging high-risk patients early, hospitals can intervene with targeted care plans, ultimately improving patient health and reducing hospital costs.

**Dataset:** [Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes-130-us-hospitals-for-years-1999-2008) (UCI Machine Learning Repository).

---

## 🚀 Workflow & Notebooks

The project is structured into five sequential Jupyter Notebooks, documenting the entire machine learning pipeline from raw data to model interpretation.

| Phase | Notebook | What it does |
|-------|----------|--------------|
| **1. Data Understanding** | [`01_data_understanding.ipynb`](notebooks/01_data_understanding.ipynb) | Investigates the dataset structure, confirms the unit of analysis (encounters vs patients), and maps missing values. |
| **2. Exploratory Data Analysis** | [`02_eda.ipynb`](notebooks/02_eda.ipynb) | Visualizes relationships between clinical variables and readmission rates. Discovers that prior hospital visits are strong predictors. |
| **3. Preprocessing** | [`03_preprocessing_feature_engineering.ipynb`](notebooks/03_preprocessing_feature_engineering.ipynb) | Cleans data, engineers new features (`total_prior_visits`), and builds a leak-free `sklearn` pipeline with a patient-aware `GroupShuffleSplit`. |
| **4. Model Training** | [`04_model_training.ipynb`](notebooks/04_model_training.ipynb) | Addresses the severe 1:8 class imbalance using `class_weight='balanced'`. Trains Baseline, Logistic Regression, and Random Forest models. |
| **5. Interpretability** | [`05_model_interpretability.ipynb`](notebooks/05_model_interpretability.ipynb) | Extracts coefficients from the Logistic Regression model to explain exactly *why* certain patients are flagged as high risk (white-box approach). |

---

## 📊 Key Findings & Results

Because only ~11% of encounters result in a 30-day readmission, accuracy was a misleading metric (a dummy model guessing "no readmission" achieves 88.8% accuracy but catches zero actual cases). 

Instead, the models were optimized and evaluated on **Recall** (catching the actual readmissions) and **ROC-AUC**:

- **Dummy (Baseline):** 0% Recall | 0.500 ROC-AUC
- **Logistic Regression:** 54% Recall | 0.650 ROC-AUC
- **Random Forest:** 57% Recall | 0.658 ROC-AUC

**Interpretability:**
The model aligns closely with clinical reality. The strongest factors increasing a patient's risk of readmission are:
1. High number of prior inpatient visits.
2. Discharge to a rehabilitation or nursing facility (indicating incomplete recovery).
3. High number of active diabetes medications (indicating clinical complexity).

---

## 📁 Repository Structure

```text
├── data/
│   ├── raw/                 # Original dataset (diabetic_data.csv)
│   └── processed/           # Processed Numpy arrays (ignored in git)
├── models/                  # Saved .pkl models (Logistic Regression)
├── notebooks/               # 01 through 05 (.ipynb files)
├── reports/                 
│   ├── figures/             # Exported charts and ROC curves
│   └── *_log.md             # Decision logs explaining every data choice
└── README.md                # You are here!
```

---
*Created by Umanda Thathsarani for IT3091 Machine Learning.*
