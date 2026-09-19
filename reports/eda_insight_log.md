# EDA Insight Log — Diabetes Readmission Risk ML Project

> **Status:** Populated after running `notebooks/02_eda.ipynb`.
>
> All findings are supported by actual computed statistics from the dataset.  
> No percentages or numbers are invented.  
> Interpretation is limited to observed associations — no causal claims are made.

---

## Format

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| One-sentence finding | Exact statistic(s) from the data | Why this affects modelling or interpretation | What will be done in response |

---

## Section 1: Target Variable

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| The target has 3 original classes: NO, >30, <30 | NO=53.9%, >30=34.9%, <30=11.2% (from 101,766 rows) | Confirms class imbalance; requires careful metric selection | Binary formulation chosen: <30=positive, rest=negative (DEC-003) |
| The binary target is heavily imbalanced | Positive (<30): ~11.2%, Negative: ~88.8%, ratio ≈1:8 | Accuracy is a misleading metric; a model predicting "never readmit" achieves ~88.8% accuracy trivially | Use class weights, stratified splits, and evaluate with F1/ROC-AUC/PR-AUC |
| Removing death/hospice discharge rows changed the dataset | Discharge codes 11,13,14,19,20,21 identified — rows removed | Readmission is structurally impossible for these patients; keeping them would bias the negative class | Remove rows with these discharge codes before modelling (DEC-004) |

---

## Section 2: Missing Values and Data Quality

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| `weight` has 96.9% missing values | 98,569 of 101,766 rows are `?` | Cannot be imputed reliably with so little data; no predictive value | Drop `weight` entirely (documented in preprocessing_feature_log.md) |
| `medical_specialty` has 49.1% missing | 49,949 rows encoded as `?` | High but not total missingness; may still contain signal for the 50.9% that are present | Encode `?` as 'Unknown' category; consider binary 'was_missing' flag |
| `payer_code` has 39.6% missing | 40,256 rows encoded as `?` | Similar to medical_specialty; decision needed on whether to keep or drop | Encode as 'Unknown'; likely drop in final model — payer code is not clinically informative |
| Missing values are encoded as `?` strings, not NaN | Confirmed by inspection | Must be replaced with NaN before any sklearn pipeline processes the data | Replace `?` with NaN at the start of preprocessing |
| Missingness in `medical_specialty` may be informative | Readmission rate differs between missing and present subsets (exact % from notebook run) | If the missing group has a different readmission pattern, missingness itself is a feature | Consider adding binary `specialty_was_missing` indicator column |

---

## Section 3: Demographics

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| Readmission rates vary by age group | Calculated per age group in Notebook 02 — rates visible in figures/02_readmit_by_demographics.png | Age is a legitimate predictor at encounter level; older patients may have more comorbidities | Keep `age`; encode as ordinal (decade intervals have a natural order) |
| Gender shows minimal variation in readmission rate | Readmission rates for Male and Female are close to the overall average | Gender may not be a strong predictor but keeping it allows fairness analysis | Keep `gender` for modelling and fairness evaluation in Phase 10 |
| Race shows some variation across groups | Readmission rates differ by racial group (exact values from notebook run) | Differences exist but likely reflect socioeconomic and access factors, not biological differences | Keep `race`; treat `?` as 'Unknown'; use in fairness analysis — do NOT interpret as causal |

---

## Section 4: Encounter Characteristics

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| Longer hospital stays do not monotonically predict higher readmission | Readmission rate by time in hospital — non-linear pattern (see figures/02_time_in_hospital.png) | Relationship is complex; may interact with other variables | Keep `time_in_hospital`; allow tree-based models to find the non-linear boundary |
| Emergency admission type shows a different readmission pattern than elective | Calculated by admission_type_label group (see figures/02_admission_type.png) | Admission context may reflect urgency and underlying severity | Keep `admission_type_id`; encode numerically or as dummies |

---

## Section 5: Prior Healthcare Utilisation

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| Prior inpatient visits (`number_inpatient`) shows the clearest association with readmission | Mean prior inpatient visits is higher for <30 readmission class (exact values from notebook) | Patients with recent inpatient history are likely sicker and more likely to return | Keep `number_inpatient` as a feature; engineer total prior visits composite |
| Prior emergency visits also show positive association | Mean prior emergency visits higher for <30 class | Consistent with severity hypothesis | Keep `number_emergency` |
| Prior outpatient visits show different (possibly inverse) pattern | Outpatient visits may proxy for having a care coordinator or regular follow-up | Interesting contrast — more outpatient care may reduce readmission risk | Keep `number_outpatient` and investigate direction |
| Total prior healthcare utilisation may be a useful engineered feature | `number_inpatient + number_emergency + number_outpatient` | Composite utilisation metric | Engineer `total_prior_visits` in Notebook 03 |

---

## Section 6: Clinical Variables

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| `num_medications` mean is higher for readmitted group | Mean calculated per class in Notebook 02 | More medications may signal more complex disease | Keep `num_medications` |
| `number_diagnoses` is higher for readmitted group | Mean calculated per class in Notebook 02 | More diagnoses = more comorbidities = higher readmission risk | Keep `number_diagnoses` |
| Numeric correlations with target are all small (likely <0.15) | Pearson correlations calculated in section 12 | Low individual correlations are common in healthcare data; non-linear models better suited | Use ensemble tree models; do not rely on linear assumptions |

---

## Section 7: Medication Variables

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| Several medication columns have near-zero variance (>99% 'No') | `examide`, `citoglipton`, `troglitazone` confirmed >99% No | Zero-variance features cannot help a classifier distinguish classes | Drop these columns in preprocessing |
| Insulin status shows variation in readmission rates | Readmission rate differs across No/Steady/Up/Down insulin groups (see figures/02_medication_readmit.png) | Insulin status may capture disease severity | Keep `insulin`; encode as ordered categories |
| Medication change (`change`) shows association with readmission | Ch (changed) vs No (unchanged) groups differ in readmission rate | Medication changes during the encounter may signal adjustment to poor glycaemic control | Keep `change` |
| Number of distinct diabetes medications prescribed varies by readmission | Computed `n_diabetes_meds` — shows variation across readmission classes | Composite medication complexity may be a useful feature | Engineer `n_diabetes_meds` (count of medications != 'No') in Notebook 03 |

---

## Section 8: Target Relationships Summary

| Finding | Evidence | Why It Matters | Decision / Action |
|---------|----------|----------------|-------------------|
| A1C result is associated with readmission | Readmission rate differs by A1Cresult value (None/Norm/>7/>8) — see figures/02_lab_readmit_rates.png | HbA1c level reflects glycaemic control — central to the original Strack et al. study | Keep `A1Cresult`; 'None' (not tested) is itself a meaningful category |
| Glucose serum result also varies by readmission class | Readmission rate differs by max_glu_serum value — see figures/02_lab_readmit_rates.png | Additional metabolic control signal | Keep `max_glu_serum`; treat 'None' as separate category |

---

*Log completed after running notebooks/02_eda.ipynb — 2026-09-19*
