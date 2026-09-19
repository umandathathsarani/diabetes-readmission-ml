# Data Dictionary — Diabetes Readmission Risk ML Project

> **Status:** Skeleton created in Phase 1. To be populated after dataset inspection in Notebook 01.
>
> All variable descriptions are derived from:
> - The UCI ML Repository dataset documentation
> - Direct dataset inspection
> - The original research paper: Strack et al. (2014), "Impact of HbA1c Measurement on Hospital Readmission Rates"
>
> No medical meanings are invented for coded variables.

---

## Dataset

**Diabetes 130-US Hospitals for Years 1999–2008**
Source: UCI Machine Learning Repository
URL: https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008

---

## Unit of Analysis

> TODO: Confirm after dataset inspection in Notebook 01.
>
> Preliminary note: Each row is believed to represent a **patient encounter (hospital visit)**, not a unique patient. Multiple encounters from the same patient may exist. This must be confirmed and documented.

---

## Variable Reference

> TODO: Complete after running `notebooks/01_data_understanding.ipynb`.

### Format

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| variable_name | Description | categorical / numerical / binary | identifier / demographic / clinical / target / excluded | Yes / No / % | Additional notes |

---

### Identifiers

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| encounter_id | TODO | TODO | identifier | TODO | TODO |
| patient_nbr | TODO | TODO | identifier | TODO | TODO |

---

### Demographics

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| race | TODO | TODO | demographic | TODO | TODO |
| gender | TODO | TODO | demographic | TODO | TODO |
| age | TODO | TODO | demographic | TODO | TODO |

---

### Admission and Discharge

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| admission_type_id | TODO | TODO | encounter | TODO | TODO |
| discharge_disposition_id | TODO | TODO | encounter | TODO | TODO |
| admission_source_id | TODO | TODO | encounter | TODO | TODO |
| time_in_hospital | TODO | TODO | encounter | TODO | TODO |

---

### Clinical / Record Variables

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| num_lab_procedures | TODO | TODO | clinical | TODO | TODO |
| num_procedures | TODO | TODO | clinical | TODO | TODO |
| num_medications | TODO | TODO | clinical | TODO | TODO |
| number_outpatient | TODO | TODO | clinical | TODO | TODO |
| number_emergency | TODO | TODO | clinical | TODO | TODO |
| number_inpatient | TODO | TODO | clinical | TODO | TODO |
| number_diagnoses | TODO | TODO | clinical | TODO | TODO |

---

### Diagnosis Variables

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| diag_1 | TODO | TODO | clinical | TODO | TODO |
| diag_2 | TODO | TODO | clinical | TODO | TODO |
| diag_3 | TODO | TODO | clinical | TODO | TODO |

---

### Medication Variables

> TODO: List all medication columns after dataset inspection. Approximately 23 medication-related binary columns are expected.

---

### Target Variable

| Variable | Meaning | Type | Role | Missing Values | Notes |
|----------|---------|------|------|----------------|-------|
| readmitted | TODO | categorical | **target** | TODO | Values: `<30`, `>30`, `NO` — transformation documented in decision_log.md |

---

## Code Mappings

Code-to-label mappings (from `IDs_mapping.csv` or dataset documentation) will be documented here after inspection.

### admission_type_id

> TODO

### discharge_disposition_id

> TODO

### admission_source_id

> TODO

---

## Reference

Strack, B., DeShazo, J. P., Gennings, C., Olmo, J. L., Ventura, S., Cios, K. J., & Clore, J. N. (2014). Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records. *BioMed Research International*, 2014. https://doi.org/10.1155/2014/781670
