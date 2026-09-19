# Model Interpretability Log — Diabetes Readmission Risk ML Project

> **Status:** Populated after running Notebook 05 (`notebooks/05_model_interpretability.ipynb`).
>
> The coefficients below are extracted from the Logistic Regression model, which was trained on standardized numeric features. Therefore, the magnitude of the coefficients directly corresponds to feature importance.

---

## 1. Top Risk Enhancers (Positive Coefficients)
These features *increase* the predicted probability of a patient returning within 30 days.

1. **`number_inpatient`**: By far the strongest predictor. Past hospitalizations strongly indicate future readmissions, reflecting overall patient fragility.
2. **`total_prior_visits`**: Our engineered feature combining inpatient, outpatient, and emergency visits. High healthcare utilization is a known major risk factor.
3. **`discharge_disposition_id_22` / `_3` / `_6`**: Discharge to rehab facilities, SNFs (Skilled Nursing Facilities), or home with home health service. These imply the patient is not fully recovered upon leaving the hospital.
4. **`number_emergency`**: Recent emergency room visits also act as a strong proxy for instability.

## 2. Top Risk Reducers (Negative Coefficients)
These features *decrease* the predicted probability of an early readmission.

1. **`discharge_disposition_id_1`**: Discharged to home. A patient deemed well enough to simply go home without assistance is generally at a lower risk of bouncing back.
2. **`admission_source_id_7`**: Emergency room admission source often has complex interactions, but in this specific model structure, certain scheduled vs emergency patterns emerge.
3. **`medical_specialty_Surgery-General`**: Patients admitted for planned general surgeries (e.g., gallbladder removal) often have a clear, fixable issue. Once fixed, they recover and do not return, unlike chronic disease patients.

## 3. Evaluation of Engineered Features

| Feature | Model Impact | Clinical Interpretation |
|---------|-------------|-------------------------|
| `total_prior_visits` | High Positive (Increases Risk) | Confirms that overall prior healthcare utilization is a critical signal. |
| `n_diabetes_meds` | Moderate Positive (Increases Risk) | Shows that patients requiring multiple concurrent diabetes medications are more clinically complex and at higher risk of complications. |

---

*Log updated after running Notebook 05 - 2026-09-19*
