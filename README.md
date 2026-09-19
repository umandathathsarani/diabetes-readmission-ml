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

The project is structured into five sequential Jupyter Notebooks, documenting the entire machine learning pipeline from raw data to model interpretation. All decisions are documented extensively in the `reports/` directory.

| Phase | Notebook | Description & Key Steps |
|-------|----------|--------------|
| **1. Data Understanding** | [`01_data_understanding.ipynb`](notebooks/01_data_understanding.ipynb) | Investigates the dataset structure, confirms the unit of analysis (encounters vs patients), maps missing values, and establishes the binary target (`<30` vs `>30/NO`). |
| **2. Exploratory Data Analysis** | [`02_eda.ipynb`](notebooks/02_eda.ipynb) | Visualizes relationships between clinical variables and readmission rates. Discovers that prior hospital visits are strong predictors, and identifies variables with near-zero variance. |
| **3. Preprocessing** | [`03_preprocessing_feature_engineering.ipynb`](notebooks/03_preprocessing_feature_engineering.ipynb) | Cleans data, engineers new features (`total_prior_visits`, `n_diabetes_meds`), groups high-cardinality ICD-9 codes, and builds a leak-free `sklearn` ColumnTransformer pipeline with a patient-aware `GroupShuffleSplit`. |
| **4. Model Training** | [`04_model_training.ipynb`](notebooks/04_model_training.ipynb) | Addresses the severe 1:8 class imbalance using `class_weight='balanced'`. Trains Baseline (Dummy), Logistic Regression, and Random Forest models, evaluated on Recall and ROC-AUC. |
| **5. Interpretability** | [`05_model_interpretability.ipynb`](notebooks/05_model_interpretability.ipynb) | Extracts coefficients from the Logistic Regression model to explain exactly *why* certain patients are flagged as high risk (white-box clinical approach). |

---

## 📊 Key Findings & Results

### The Class Imbalance Problem
Only ~11% of hospital encounters result in a 30-day readmission. Accuracy is a highly misleading metric here—a dummy model guessing "no readmission" achieves 88.8% accuracy but catches zero actual cases. 

Instead, the models were optimized and evaluated on **Recall** (the percentage of actual readmissions successfully caught by the model) and **ROC-AUC**:

| Model | Accuracy | Recall | ROC-AUC | Notes |
|-------|----------|--------|---------|-------|
| **Dummy (Baseline)** | 88.8% | 0.0% | 0.500 | Guesses negative every time. |
| **Logistic Regression** | 65.6% | **54.0%** | **0.650** | Strong recall, highly interpretable. |
| **Random Forest** | 64.5% | **57.5%** | **0.658** | Best recall, but harder to explain. |

### Model Interpretability (Clinical Insights)
The Logistic Regression model was chosen as the final model due to its transparency. The strongest factors increasing a patient's risk of readmission aligned perfectly with clinical reality:
1. **High prior utilization:** A high number of previous inpatient visits (`number_inpatient`) or total prior visits (`total_prior_visits`).
2. **Incomplete recovery:** Discharge to a rehabilitation facility or skilled nursing facility (SNF).
3. **Clinical complexity:** A high number of active diabetes medications or emergency room visits.

Conversely, patients discharged directly to their homes, or admitted for scheduled general surgeries, had significantly lower risks of returning.

---

## 💻 Setup & Execution Instructions

**Note on Execution Flow: This project is entirely notebook-driven. While a `src/` directory is included to demonstrate an understanding of production software architecture, the actual data pipeline and models are executed exclusively via the Jupyter Notebooks.**

To run this project locally and reproduce the findings:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/umandathathsarani/diabetes-readmission-ml.git
   cd diabetes-readmission-ml
   ```

2. **Set up the environment:**
   Ensure you have Python 3.9+ installed. Install the required dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter joblib
   ```

3. **Download the Data:**
   - Download the dataset from the [UCI Repository](https://archive.ics.uci.edu/dataset/296/diabetes-130-us-hospitals-for-years-1999-2008).
   - Place the `diabetic_data.csv` and `IDS_mapping.csv` files inside the `data/raw/` directory.

4. **Run the Notebooks:**
   Start the Jupyter server:
   ```bash
   jupyter notebook
   ```
   Open and run the notebooks in the `notebooks/` directory in sequential order (01 through 05).

---

## 📁 Repository Structure

```text
diabetes-readmission-ml/
├── data/
│   ├── raw/                 # Original dataset (must be downloaded manually)
│   └── processed/           # Processed Numpy arrays (ignored in git to save space)
├── models/                  # Saved .pkl models (e.g., Logistic Regression)
├── notebooks/               
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── 05_model_interpretability.ipynb
├── reports/                 
│   ├── figures/             # Exported charts (ROC curves, feature importance)
│   └── *_log.md             # Detailed logs explaining every data and modeling decision
├── src/                     # Source code for modular, production-ready scripts
│   ├── data/                # Scripts to fetch or generate data
│   ├── evaluation/          # Scripts to evaluate models
│   ├── features/            # Scripts to turn raw data into features
│   ├── models/              # Scripts to train models
│   └── preprocessing/       # Scripts to clean data
└── README.md                # Project documentation
```

### Future Deployment Plan (The `src/` Directory)
This project follows professional **Software Engineering for Machine Learning** best practices. While the project is currently evaluated via Jupyter Notebooks, the foundation for a production deployment has been laid in the `src/` directory.

In a real-world scenario, raw Jupyter notebooks are not run in production. Instead, the notebook logic is refactored into modular, reusable Python scripts (which I have started in `src/`). This allows the model to be deployed via an API or run as a scheduled cron job using code like:

```python
from src.data.load_data import load_raw_data
from src.preprocessing.clean_data import basic_cleaning
from src.features.build_features import make_features

df = load_raw_data()
df, patient_ids = basic_cleaning(df)
df_features = make_features(df)
```

---
*Created by Umanda Thathsarani for IT3091 Machine Learning.*
