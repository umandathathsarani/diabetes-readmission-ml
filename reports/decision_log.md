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
> TODO: Confirm after dataset inspection in Notebook 01.

Preliminary: The unit of analysis is expected to be the **patient encounter** (hospital visit), not the unique patient. Multiple encounters from the same patient may exist. This affects how data splitting must be handled.

### Options Considered
- Encounter level
- Patient level

### Selected Option
> TODO: Confirm after dataset inspection.

### Reason
> TODO: Document after confirmation.

### Evidence
> TODO: Verify patient_nbr appears multiple times.

### Trade-offs
Encounter-level prediction is more directly useful for planning individual encounters. However, if patients appear in both training and test sets, the model may benefit from patient-level information leakage.

### Date
2026-09-19 (preliminary — to be confirmed)

---

## DEC-003 — Target Variable Definition

### Decision
> TODO: Define after dataset inspection.

The `readmitted` column has three categories: `<30`, `>30`, and `NO`.

A potential binary formulation is:
- **Positive class:** Readmitted within 30 days (`<30`)
- **Negative class:** Not readmitted within 30 days (`>30` or `NO` combined)

### Options Considered
- Multiclass classification (original 3 classes)
- Binary: `<30` vs. `>30` + `NO`
- Binary: `<30` + `>30` (any readmission) vs. `NO`

### Selected Option
> TODO: Confirm and justify after EDA (class distribution analysis).

### Reason
> TODO: Document based on class distribution and project objective.

### Evidence
> TODO: Class counts from dataset inspection.

### Trade-offs
Binary formulation simplifies evaluation and is more aligned with hospital planning. However, it collapses information about the timing of readmissions beyond 30 days. This limitation must be stated.

### Date
2026-09-19 (preliminary)

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
