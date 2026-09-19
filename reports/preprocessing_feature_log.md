# Preprocessing and Feature Engineering Log

> All decisions in this log were implemented in `notebooks/03_preprocessing_feature_engineering.ipynb` and are supported by actual data inspection.
> No values are made up.

---

## Section 1: Row-Level Exclusions

| Issue | What was done | Reason | Rows affected |
|-------|--------------|--------|---------------|
| Death/hospice discharge records | Removed rows with discharge_disposition_id in {11, 13, 14, 19, 20, 21} | Readmission is structurally impossible for patients who died or entered hospice. Including them would silently bias the negative class. | ~2,273 rows removed |
| Missing value encoding | Replaced `?` string with `np.nan` throughout | sklearn cannot handle string placeholders. Must be real NaN. | Affects race, payer_code, medical_specialty, diag_1/2/3 |

---

## Section 2: Column Drops

| Column | Problem | Treatment | Reason |
|--------|---------|-----------|--------|
| encounter_id | Identifier only | Dropped | Not a feature - just a row ID |
| patient_nbr | Identifier only (saved separately for group split) | Dropped from features | Not a feature - but needed for patient-aware splitting |
| weight | 96.9% missing (98,569 of 101,766 rows) | Dropped | Cannot be imputed reliably. Essentially no signal. |
| payer_code | 39.6% missing, not clinically relevant to readmission | Dropped | Insurance/billing code unlikely to improve readmission prediction; high missingness |
| examide | >99% of rows are 'No' (near-zero variance) | Dropped | Zero variance provides no predictive signal |
| citoglipton | >99% of rows are 'No' (near-zero variance) | Dropped | Same as above |
| troglitazone | >99% of rows are 'No' (withdrawn from market) | Dropped | Same as above |
| tolazamide | >99% of rows are 'No' | Dropped | Same as above |
| miglitol | >99% of rows are 'No' | Dropped | Same as above |
| acetohexamide | >99% of rows are 'No' | Dropped | Same as above |
| diag_1, diag_2, diag_3 | Very high cardinality (thousands of unique ICD-9 codes) | Replaced with grouped category columns | One-hot encoding raw ICD-9 codes would create thousands of sparse columns; grouping reduces noise |

---

## Section 3: Missing Value Treatments

| Column | Missing % | Treatment | Reason |
|--------|----------|-----------|--------|
| race | 2.2% | SimpleImputer with 'Unknown' category | Low missingness; Unknown is a valid category |
| medical_specialty | 49.1% | Filled with 'Unknown', then rare values grouped as 'Other_Specialty' | Too much missing to impute meaningfully; Unknown category preserves missingness signal |
| diag_1 | 0.02% | Mapped to 'Unknown' category during ICD-9 grouping | Negligible missingness |
| diag_2 | 0.35% | Mapped to 'Unknown' category during ICD-9 grouping | Low missingness |
| diag_3 | 1.4% | Mapped to 'Unknown' category during ICD-9 grouping | Low missingness |
| Numeric columns | Minimal | Median imputation in pipeline | Median is robust to outliers |

---

## Section 4: Feature Engineering

| New Feature | How it was built | Why I created it | Leakage risk |
|------------|-----------------|-----------------|-------------|
| total_prior_visits | number_inpatient + number_emergency + number_outpatient | Composite measure of recent healthcare burden. Prior inpatient visits showed the strongest individual association with readmission in EDA. | None - all components are prior-year data, available at time of discharge |
| n_diabetes_meds | Count of medication columns where value != 'No' | Someone on many diabetes medications is probably managing a more complex case. Avoids redundancy with individual medication columns. | None - medications are known at discharge |
| diag_1_category | ICD-9 code grouped into 17 clinical categories | Reduces cardinality from thousands to 17 manageable categories while preserving clinical meaning | None |
| diag_2_category | Same as above for secondary diagnosis | Same reasoning | None |
| diag_3_category | Same as above for tertiary diagnosis | Same reasoning | None |

### ICD-9 Grouping Scheme

| Range | Category |
|-------|----------|
| 1-139 | Infectious |
| 140-239 | Neoplasms |
| 240-279 | Endocrine_Metabolic (includes diabetes 250.x) |
| 280-289 | Blood |
| 290-319 | Mental |
| 320-389 | Nervous |
| 390-459 | Circulatory |
| 460-519 | Respiratory |
| 520-579 | Digestive |
| 580-629 | Genitourinary |
| 630-679 | Pregnancy |
| 680-709 | Skin |
| 710-739 | Musculoskeletal |
| 740-759 | Congenital |
| 760-779 | Perinatal |
| 780-799 | Ill_Defined |
| 800-999 | Injury |
| V codes | Supplementary |
| E codes | External |
| NaN/other | Unknown |

---

## Section 5: Categorical Encoding

| Column | Encoding | Reason |
|--------|---------|--------|
| age | OrdinalEncoder (0-9 for [0-10) to [90-100)) | Age has a natural order; ordinal encoding preserves this |
| race, gender | OneHotEncoder | Nominal categories with no natural order |
| medical_specialty | OneHotEncoder (after grouping rare values) | Nominal; rare categories grouped to 'Other_Specialty' first |
| max_glu_serum, A1Cresult | OneHotEncoder | Nominal categories including 'None' (test not done) |
| change, diabetesMed | OneHotEncoder | Binary categoricals |
| insulin and other medication columns | OneHotEncoder | Ordinal (No/Steady/Up/Down) but encoding as nominal to avoid imposing assumptions about the direction of dosage changes |
| diag_1/2/3_category | OneHotEncoder | Nominal clinical categories |
| admission_type_id, discharge_disposition_id, admission_source_id | Treated as numeric | Integer codes used as-is; semantically they could be nominal but cardinality is moderate |

---

## Section 6: Numerical Preprocessing

| Step | Applied to | Method | Reason |
|------|-----------|--------|--------|
| Imputation | All numeric columns | Median | Robust to outliers; prior visit counts are right-skewed |
| Scaling | All numeric columns | StandardScaler | Ensures features with large ranges don't dominate distance-based models |
| Order | Impute first, then scale | Pipeline | Scaling after imputation avoids scale artifacts from NaN values |

---

## Section 7: Train/Test Split

| Property | Value |
|----------|-------|
| Method | GroupShuffleSplit (sklearn) |
| Split ratio | 80% train / 20% test |
| Group variable | patient_nbr |
| Patient overlap | 0 (verified) |
| Seed | 42 |

Documented in decision_log.md DEC-005.

---

## Section 8: Leakage Checks

| Feature | Risk | Assessment |
|---------|------|-----------|
| discharge_disposition_id | Medium | Contains death/hospice codes - those rows are REMOVED, not the column. Remaining values (e.g., discharged to home, transferred) are legitimate discharge context known at prediction time. |
| number_inpatient/emergency/outpatient | None | These are counts from the YEAR BEFORE this encounter - prior history, not future outcomes |
| total_prior_visits | None | Derived from prior-year counts - no leakage |
| n_diabetes_meds | None | Medications prescribed DURING this encounter and known at discharge |
| diag_1/2/3 | None | Primary diagnosis is established during the encounter and available at discharge |

---

*Updated after running notebooks/03_preprocessing_feature_engineering.ipynb - 2026-09-19*
