# Decision Log — Diabetes Readmission Risk ML Project

> **Purpose:** Every significant analytical, modelling, and engineering decision is documented here.
>
> Each entry follows the standard format below. This log is a living document — decisions are added throughout all project phases.
>
> **Rule:** No decision is made silently. If a decision affects the model, data, or interpretation, it must appear here.

---

## Decision Log Format

Each entry uses this structure:

```
## DEC-NNN — [Short Decision Title]

### Decision
What was decided.

### Options Considered
- Option A
- Option B
- Option C

### Selected Option
Which option was chosen.

### Reason
Why this option was selected.

### Evidence
What data or analysis supports this decision.

### Trade-offs
What is gained and what is given up with this choice.

### Date
YYYY-MM-DD
```

---

## DEC-001 — Primary Decision Lens

### Decision
The primary analytical lens is **Readmission Risk**.

### Options Considered
- Readmission Risk
- Length of Stay Prediction
- Medication Adherence Analysis
- Diagnosis-based clustering

### Selected Option
Readmission Risk

### Reason
The readmission lens is most directly relevant to hospital planning, resource allocation, and decision-support. Readmission events are a meaningful and measurable clinical and operational outcome. The dataset includes a direct readmission outcome variable.

### Evidence
Dataset contains `readmitted` column with values `<30`, `>30`, `NO`.

### Trade-offs
Readmission risk is a population-level signal. Individual predictions carry uncertainty. The model identifies associations, not causes, and cannot account for factors not recorded in the dataset.

### Date
2026-09-19

---

## DEC-002 — Unit of Analysis

### Decision
The unit of analysis is the **patient encounter (hospital admission)**.

Each row in `diabetic_data.csv` represents one encounter, identified by a unique `encounter_id`. One patient (`patient_nbr`) can appear multiple times.

### Options Considered
- Encounter level (each row = one hospital visit)
- Patient level (one row per patient)

### Selected Option
**Encounter level** — confirmed from dataset inspection.

### Reason
The dataset is structured at the encounter level (`encounter_id` is unique per row). The business question is about predicting readmission following a specific hospital discharge — this is inherently encounter-level. Collapsing to patient level would lose encounter-specific information.

### Evidence
From `notebooks/01_data_understanding.ipynb`:
- Total rows: **101,766**
- Unique `encounter_id` values: **101,766** (one-to-one — no duplicates)
- Unique `patient_nbr` values: **71,518**
- Patients with 2+ encounters: **16,773** (23.5% of patients)

### Trade-offs
**Benefit:** Encounter-level retains all data and is directly relevant to discharge-time decision support.  
**Risk:** 16,773 patients appear in multiple rows. A naive random train/test split may place encounters from the same patient in both sets — this creates information leakage between train and test. A **patient-aware split** (grouped by `patient_nbr`) is required.

### Date
2026-09-19 (confirmed after Notebook 01)

---

## DEC-003 — Target Variable Definition

### Decision
The target will be formulated as a **binary classification** problem:
- **Positive class (1):** Patient readmitted within 30 days (`<30`)
- **Negative class (0):** All other outcomes — readmitted after 30 days (`>30`) or not readmitted (`NO`)

### Options Considered
1. **Multiclass (3-class):** Predict `NO`, `>30`, or `<30` directly
2. **Binary — early readmission:** `<30` (positive) vs `>30` + `NO` (negative)
3. **Binary — any readmission:** `<30` + `>30` (positive) vs `NO` (negative)

### Selected Option
Option 2: **`<30` vs rest**

### Reason
The hospital's primary concern is early readmission (within 30 days), as this:
- Represents the highest clinical and operational cost
- Is the standard clinical readmission quality metric
- Is the explicit target of the original Strack et al. (2014) study
- Is the most actionable — patients flagged before discharge could receive targeted follow-up

`>30` readmissions are clinically distinct; combining them with `NO` into the negative class is more defensible than merging `>30` with `<30`.

### Evidence
From `notebooks/01_data_understanding.ipynb`:

| Category | Count | % |
|----------|-------|---|
| NO | 54,864 | 53.9% |
| >30 | 35,545 | 34.9% |
| <30 | 11,357 | 11.2% |

Under the binary formulation:
- Positive (`<30`): **11,357** (11.2%)
- Negative (`>30` + `NO`): **90,409** (88.8%)

Class imbalance ratio ≈ 1:8 — significant, must be addressed in modelling.

### Trade-offs
**Advantage:** Clinically focused; aligns with standard 30-day readmission metric; simpler evaluation.  
**Limitation:** The formulation discards the distinction between `>30` and `NO`; a patient readmitted on day 31 and a patient never readmitted are treated identically in the negative class. This limitation is documented and stated in `reports/final_findings.md`.

### Original → Binary Transformation
| Original Value | Binary Label | Rationale |
|---------------|-------------|----------|
| `<30` | 1 (positive) | Early readmission — primary target |
| `>30` | 0 (negative) | Not early readmission |
| `NO` | 0 (negative) | Not early readmission |

### Date
2026-09-19 (confirmed after Notebook 01)

---

## DEC-004 — Leakage Analysis

> TODO: Populate after feature inspection in Notebook 01 / Notebook 03.

### Features Under Investigation

| Feature | Leakage Risk | Decision | Reason |
|---------|-------------|----------|--------|
| discharge_disposition_id | **HIGH** | Under investigation | Some discharge codes may encode death or transfer, making readmission impossible — these may act as outcome proxies |
| encounter_id | **HIGH** | Exclude | Unique identifier, no predictive value |
| patient_nbr | **HIGH** | Exclude from features | Patient identifier — may cause data leakage if patient appears in train and test |
| Other features | TODO | TODO | TODO |

---

## DEC-005 — Train / Validation / Test Strategy

> TODO: Confirm after dataset size and patient-encounter structure is verified.

### Considerations
- Dataset size (approximate: >100,000 rows expected)
- Potential for same patient in train and test
- Class imbalance in target

### Options Considered
- Simple random train/test split
- Train / validation / test (three-way)
- Cross-validation
- Group-stratified split (grouped by patient_nbr)

### Selected Option
> TODO

### Reason
> TODO

### Date
> TODO

---

## DEC-006 — Class Imbalance Strategy

> TODO: Confirm after EDA (class distribution).

### Considerations
- `<30` class likely minority class
- Over-representing the majority class risks misleading accuracy
- Resampling methods (SMOTE) must not contaminate validation/test data

### Options Considered
- Class weights (`class_weight='balanced'`)
- SMOTE applied only to training fold
- Threshold adjustment
- No adjustment

### Selected Option
> TODO

### Reason
> TODO

### Date
> TODO

---

## DEC-007 — Feature Engineering Decisions

> TODO: Populate during Notebook 03.

| Feature | Construction | Business Meaning | Leakage Risk | Included |
|---------|-------------|-----------------|-------------|---------|
| TODO | TODO | TODO | TODO | TODO |

---

## DEC-008 — Model Selection

> TODO: Populate during Notebook 04.

---

## DEC-009 — Evaluation Metric Priority

> TODO: Confirm after class distribution is known.

**Preliminary position:** Accuracy alone is insufficient for an imbalanced healthcare classification task. Priority metrics will include Recall (for the readmission-positive class), Precision, F1, and ROC-AUC.

---

## DEC-010 — Threshold Selection

> TODO: Populate during Notebook 05.

---

*Log maintained throughout project. Last updated: 2026-09-19 (Phase 1 initialization)*
