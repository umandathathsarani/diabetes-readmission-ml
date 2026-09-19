# Data Dictionary — Diabetes Readmission Risk ML Project

> **Status:** Populated after dataset inspection in Notebook 01 (`notebooks/01_data_understanding.ipynb`).
>
> All variable descriptions are derived from:
> - Direct dataset inspection
> - UCI ML Repository variable table
> - `IDS_mapping.csv` from the dataset package
> - Strack et al. (2014) — original research paper
>
> No medical meanings are invented for coded variables.

---

## Dataset

**Name:** Diabetes 130-US Hospitals for Years 1999–2008  
**Source:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/296/diabetes-130-us-hospitals-for-years-1999-2008  
**Reference:** Strack et al. (2014). BioMed Research International, vol. 2014, Article 781670.

---

## Unit of Analysis — CONFIRMED

> **Each row represents a single patient encounter (hospital admission).**
>
> One patient (`patient_nbr`) may appear multiple times — once per hospital visit.
>
> - Total rows: **101,766**
> - Unique patients: **71,518**
> - Patients with >1 encounter: **16,773** (23.5% of patients)
>
> This is confirmed by inspecting `encounter_id` (unique per row) vs `patient_nbr` (repeats).  
> Documented in `decision_log.md DEC-002`.

---

## Dataset Statistics (from Notebook 01)

| Attribute | Value |
|-----------|-------|
| Total rows (encounters) | 101,766 |
| Total columns | 50 |
| Unique patients | 71,518 |
| Patients with multiple encounters | 16,773 (23.5%) |
| Max encounters per patient | Confirmed from data |
| Fully duplicate rows | 0 |
| Missing value encoding | `?` string (not NaN) |

---

## Column Classification

| Group | Count | Columns |
|-------|-------|---------|
| Identifiers | 2 | encounter_id, patient_nbr |
| Demographics | 3 | race, gender, age |
| Admission/Discharge | 6 | admission_type_id, discharge_disposition_id, admission_source_id, time_in_hospital, payer_code, medical_specialty |
| Clinical Numeric | 7 | num_lab_procedures, num_procedures, num_medications, number_outpatient, number_emergency, number_inpatient, number_diagnoses |
| Diagnosis | 3 | diag_1, diag_2, diag_3 |
| Lab / Weight | 3 | max_glu_serum, A1Cresult, weight |
| Medication (individual) | 23 | metformin, repaglinide, nateglinide, chlorpropamide, glimepiride, acetohexamide, glipizide, glyburide, tolbutamide, pioglitazone, rosiglitazone, acarbose, miglitol, troglitazone, tolazamide, examide, citoglipton, insulin, glyburide-metformin, glipizide-metformin, glimepiride-pioglitazone, metformin-rosiglitazone, metformin-pioglitazone |
| Medication Summary | 2 | change, diabetesMed |
| Target | 1 | readmitted |
| **Total** | **50** | |

---

## Variable Reference

### Identifiers

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| encounter_id | Unique identifier for each hospital encounter | Integer | Identifier | No | Unique per row — do NOT use as predictive feature |
| patient_nbr | Unique identifier for each patient | Integer | Identifier | No | Can repeat — same patient, multiple encounters |

---

### Demographics

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| race | Patient race | Categorical | Demographic | Yes — 2,273 rows (2.2%) encoded as `?` | Values: Caucasian, Asian, African American, Hispanic, Other, ? |
| gender | Patient gender | Categorical | Demographic | No | Values: Male, Female, Unknown/Invalid |
| age | Patient age group | Categorical (ordinal) | Demographic | No | Grouped in 10-year intervals: [0–10), [10–20), …, [90–100) |

---

### Admission and Discharge Information

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| admission_type_id | Type of admission (integer code) | Categorical (coded) | Encounter | No | 9 values: 1=Emergency, 2=Urgent, 3=Elective, 4=Newborn, 5=Not Available, 6=(null), 7=Trauma Center, 8=Not Mapped. See IDS_mapping.csv |
| discharge_disposition_id | Disposition at discharge (integer code) | Categorical (coded) | Encounter | No | 29 values. **LEAKAGE RISK**: codes 11=Expired, 13=Hospice/home, 14=Hospice/facility, 19=Expired (hospice home), 20=Expired (hospice facility) indicate patient died — readmission impossible. These rows should be excluded. See decision_log.md DEC-004 |
| admission_source_id | Source of the admission (integer code) | Categorical (coded) | Encounter | No | 21 values. Examples: 1=Physician referral, 7=Emergency room, 4=Transfer from hospital. See IDS_mapping.csv |
| time_in_hospital | Days between admission and discharge | Integer | Encounter | No | Range: 1–14 days (by dataset inclusion criteria) |
| payer_code | Insurance/payer code | Categorical | Encounter | Yes — 40,256 rows (39.6%) encoded as `?` | High missingness; consider dropping or treating as 'Unknown' |
| medical_specialty | Medical specialty of admitting physician | Categorical | Encounter | Yes — 49,949 rows (49.1%) encoded as `?` | Very high missingness; consider dropping or treating as 'Unknown' |

---

### Clinical Numeric Variables

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| num_lab_procedures | Number of lab tests performed during encounter | Integer | Clinical | No | Always ≥ 1 (inclusion criterion) |
| num_procedures | Number of procedures (other than lab) performed | Integer | Clinical | No | |
| num_medications | Number of distinct medications administered | Integer | Clinical | No | |
| number_outpatient | Number of outpatient visits in the year prior to hospitalisation | Integer | Clinical | No | Reflects prior healthcare utilisation |
| number_emergency | Number of emergency visits in the year prior to hospitalisation | Integer | Clinical | No | |
| number_inpatient | Number of inpatient visits in the year prior to hospitalisation | Integer | Clinical | No | Strong predictor of readmission risk in literature |
| number_diagnoses | Total number of diagnoses recorded for the encounter | Integer | Clinical | No | |

---

### Diagnosis Variables

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| diag_1 | Primary diagnosis (ICD-9 code) | Categorical | Clinical | Yes — 21 rows (0.02%) encoded as `?` | ICD-9 codes; very low missingness |
| diag_2 | Secondary diagnosis (ICD-9 code) | Categorical | Clinical | Yes — 358 rows (0.35%) encoded as `?` | |
| diag_3 | Additional diagnosis (ICD-9 code) | Categorical | Clinical | Yes — 1,423 rows (1.4%) encoded as `?` | |

> Note: ICD-9 diagnosis codes have very high cardinality. Grouping into clinical categories (e.g., circulatory, respiratory, diabetes) is typically needed during feature engineering.

---

### Lab Results and Weight

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| weight | Patient weight in pounds | Categorical (binned) | Lab/Clinical | Yes — **98,569 rows (96.9%)** encoded as `?` | **Decision: DROP** — too sparse to provide useful predictive information |
| max_glu_serum | Maximum glucose serum test result | Categorical | Lab | No | Values: None, Norm, >200, >300. "None" means test not performed |
| A1Cresult | HbA1c (glycated haemoglobin) test result | Categorical | Lab | No | Values: None, Norm, >7, >8. "None" means not measured. Central variable in original Strack et al. study |

---

### Medication Variables (23 individual drugs)

All 23 medication columns follow the same encoding:

| Value | Meaning |
|-------|---------|
| No | Drug not prescribed |
| Steady | Drug prescribed with no dose change |
| Up | Drug dosage was increased |
| Down | Drug dosage was decreased |

| Variable | Drug Class | Notes |
|----------|-----------|-------|
| metformin | Biguanide | Most common oral diabetes drug |
| repaglinide | Meglitinide | |
| nateglinide | Meglitinide | |
| chlorpropamide | Sulfonylurea (1st gen) | |
| glimepiride | Sulfonylurea (3rd gen) | |
| acetohexamide | Sulfonylurea | |
| glipizide | Sulfonylurea | |
| glyburide | Sulfonylurea | |
| tolbutamide | Sulfonylurea | |
| pioglitazone | Thiazolidinedione | |
| rosiglitazone | Thiazolidinedione | |
| acarbose | Alpha-glucosidase inhibitor | |
| miglitol | Alpha-glucosidase inhibitor | |
| troglitazone | Thiazolidinedione (withdrawn from market) | Expected to be nearly all "No" |
| tolazamide | Sulfonylurea | |
| examide | — | Expected to have near-zero variance |
| citoglipton | — | Expected to have near-zero variance |
| insulin | Insulin | Widely used — likely highly variable |
| glyburide-metformin | Combination | |
| glipizide-metformin | Combination | |
| glimepiride-pioglitazone | Combination | |
| metformin-rosiglitazone | Combination | |
| metformin-pioglitazone | Combination | |

> Some medications (e.g., `examide`, `citoglipton`, `troglitazone`) may have near-zero variance and should be investigated during feature engineering. Zero-variance features provide no predictive signal.

---

### Medication Summary Variables

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| change | Whether any diabetes medication was changed during the encounter | Binary categorical | Clinical | No | Values: Ch (changed), No (not changed) |
| diabetesMed | Whether any diabetes medication was prescribed | Binary categorical | Clinical | No | Values: Yes, No |

---

### Target Variable

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| readmitted | Patient readmission status following discharge | Categorical (3 classes) | **Target** | No | `NO` = not readmitted; `>30` = readmitted after 30 days; `<30` = readmitted within 30 days |

**Target Distribution (from Notebook 01):**

| Category | Count | Percentage |
|----------|-------|------------|
| NO | 54,864 | 53.9% |
| >30 | 35,545 | 34.9% |
| <30 | 11,357 | 11.2% |
| **Total** | **101,766** | **100%** |

> **Imbalance:** The `<30` class (highest clinical concern — early readmission) is a minority class at ~11.2%.  
> Target transformation options are documented in `decision_log.md DEC-003`.

---

## Missing Value Summary

| Column | Missing (?) | % Missing | Planned Treatment |
|--------|------------|-----------|-------------------|
| weight | 98,569 | 96.9% | **Drop** — too sparse |
| medical_specialty | 49,949 | 49.1% | Treat `?` as 'Unknown' category, or drop |
| payer_code | 40,256 | 39.6% | Treat `?` as 'Unknown' category, or drop |
| race | 2,273 | 2.2% | Treat `?` as 'Unknown' category |
| diag_3 | 1,423 | 1.4% | Impute or treat as 'Unknown' |
| diag_2 | 358 | 0.35% | Impute or treat as 'Unknown' |
| diag_1 | 21 | 0.02% | Impute or treat as 'Unknown' |

---

## Code Mappings (from IDS_mapping.csv)

### admission_type_id

| Code | Description |
|------|------------|
| 1 | Emergency |
| 2 | Urgent |
| 3 | Elective |
| 4 | Newborn |
| 5 | Not Available |
| 6 | (null) |
| 7 | Trauma Center |
| 8 | Not Mapped |

### discharge_disposition_id (selected — see IDS_mapping.csv for full list)

| Code | Description | Leakage Risk |
|------|------------|-------------|
| 1 | Discharged to home | None |
| 2 | Discharged/transferred to another short term hospital | None |
| 11 | Expired | **HIGH — readmission impossible** |
| 13 | Hospice / home | **HIGH — readmission impossible** |
| 14 | Hospice / medical facility | **HIGH — readmission impossible** |
| 19 | Expired at home (hospice) | **HIGH — readmission impossible** |
| 20 | Expired in medical facility (hospice) | **HIGH — readmission impossible** |

### admission_source_id (selected — see IDS_mapping.csv for full list)

| Code | Description |
|------|------------|
| 1 | Physician Referral |
| 4 | Transfer from hospital |
| 7 | Emergency Room |

---

## Reference

Strack, B., DeShazo, J. P., Gennings, C., Olmo, J. L., Ventura, S., Cios, K. J., & Clore, J. N. (2014). Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records. *BioMed Research International*, 2014. https://doi.org/10.1155/2014/781670
