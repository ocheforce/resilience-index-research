# Resilience Index — Scientific Reference Standard Framework v0.2

**Status:** Decision-locked framework for pilot preparation  
**Date:** October 2026  
**Project:** Resilience Index — Making recovery capacity measurable

## 1. Purpose

This document defines how Resilience Index selects, documents, verifies, and eventually establishes reference standards for the variables used in the pilot.

The reference framework is intentionally distinct from a clinical diagnostic reference range.

For a first-time assessment, the reference framework answers:

> How does this person's measurement compare with an appropriate healthy reference population?

For repeated assessments, Resilience Index adds a second layer:

> How does this person's current measurement compare with their own established baseline?

The first layer informs **Reserve**. The second layer is central to **Bounce-back** and longitudinal recovery measurement.

## 2. Core principle

There is no single universal "global resilience reference range."

Reference standards must be selected according to:

1. population;
2. age;
3. sex where relevant;
4. education where relevant;
5. measurement method/device/assay;
6. pre-analytical conditions;
7. reference-subject health criteria;
8. statistical method;
9. geographic/cultural context;
10. evidence quality and transferability.

Clinical laboratory reference intervals commonly represent the central 95% of an appropriately defined reference population. CLSI EP28 provides guidance for establishing, verifying, and transferring laboratory reference intervals and emphasizes reference-subject selection, analytical/pre-analytical considerations, and statistical estimation. The guideline identifies 120 reference individuals per partition as the minimum commonly recommended for a direct nonparametric reference-interval study.

## 3. Reference hierarchy

Resilience Index will use the following hierarchy:

### Tier 1 — Population- and method-specific Nigerian reference evidence

Preferred when an adequately characterized Nigerian reference population exists and the measurement method is compatible.

### Tier 2 — African reference evidence

Used when strong Nigerian evidence is unavailable but a sufficiently comparable African population and method exist.

### Tier 3 — High-quality international normative data

Used when local evidence is insufficient, particularly for standardized cognitive instruments with established demographic norms.

### Tier 4 — Project-generated reference cohort

Long-term objective: establish Resilience Index-specific Nigerian reference distributions using a dedicated healthy reference cohort and a standardized measurement protocol.

External reference data will remain explicitly labelled as external; they will not be presented as Nigerian norms.

## 4. Current variable framework

| Variable | Pilot role | Preferred reference strategy | Current evidence status |
|---|---|---|---|
| CRP | Clinical/physiological domain | Nigerian healthy adult reference, method-compatible | Nigerian reference interval identified; mean/SD for transformed z-score still required |
| HbA1c | Clinical/physiological domain | Nigerian healthy adult reference, standardized assay | Nigerian reference interval identified; mean/SD for z-score still required |
| ln-rMSSD | Clinical/physiological domain | Nigerian healthy young-adult, method-compatible reference | Strong Nigerian evidence identified; mean and SD reported |
| TMT-B | Cognitive domain | Age/education-adjusted normative data | Strong international norms; Nigerian healthy norm for this exact application not yet established |
| Digit Span | Cognitive domain | Age/education/sex-adjusted normative data | International demographic norms available; Nigerian healthy norm for this exact application not yet established |

## 5. CRP

### Nigerian evidence

A study of 120 healthy adult Nigerians reported hs-CRP values from 0.62 to 11.64 mg/L, with median 1.3 mg/L and mean 2.3 mg/L. The assay used was the Synthron CRP ultrasensitive ELISA method. The study population had a mean BMI of approximately 18.6 kg/m².

This evidence is useful but not automatically transferable to the Resilience Index pilot because:

- the sample was relatively small;
- the population had unusually low mean BMI;
- the assay/method must be compared with the pilot's point-of-care method;
- CRP is sensitive to inflammatory state and other biological/contextual factors;
- the published interval alone does not provide the transformed mean and SD required by the current Resilience Index z-score formula.

### Current scoring position

The protocol specifies:

\`CRP_z = [ln(CRP + 1) - μ_ref] / σ_ref\`

Therefore, the final implementation must have a defensible reference mean (μ_ref) and SD (σ_ref) on the transformed scale.

**Do not derive μ_ref or σ_ref from the published lower and upper limits unless the source provides sufficient statistical information and the derivation is explicitly justified.**

### Required next action

Obtain the underlying CRP distribution or sufficient summary statistics from the primary Nigerian study, or identify a better method-compatible Nigerian dataset.

## 6. HbA1c

### Nigerian evidence

A Port Harcourt study included 172 apparently healthy adults aged 20–80 years. HbA1c was measured using a boronate-affinity chromatographic method. After outlier handling, the reported mean was 4.84% and the reference interval was 4.0–5.9%.

This is important evidence that a Nigerian reference interval can differ from a manufacturer's non-local interval; the authors reported a manufacturer interval of 4.0–6.5%.

### Limitation for Resilience Index

The published study provides a mean and reference interval, but the current Resilience Index z-score implementation requires a reference SD.

The reference interval cannot automatically be converted to an SD unless distributional assumptions are made. Such an assumption should not be silently embedded in the scoring engine.

### Current scoring position

Use the Nigerian study as a candidate reference source, but **do not finalize μ_ref/σ_ref for the scoring engine until the required distributional parameters and assay compatibility are verified.**

HbA1c diagnostic thresholds must not be substituted for a healthy reference distribution.

## 7. HRV / ln-rMSSD

### Nigerian evidence

A study of 840 healthy young Nigerians aged 15–40 years reported:

- RMSSD mean ± SD: **57 ± 49 ms**
- male RMSSD: **63.6 ms**
- female RMSSD: **50.9 ms**

The study also found significant sex differences and emphasized that HRV interpretation depends on age, sex, context, analysis method, and recording duration.

### Implication for Resilience Index

This is the strongest current local candidate for the HRV reference population because its age range substantially overlaps the pilot's 18–40-year target.

However, the protocol uses **ln-rMSSD**, while the published study reports RMSSD.

The final reference implementation therefore needs either:

1. participant-level data from the Nigerian study, allowing direct transformation to ln(RMSSD); or
2. sufficiently detailed distributional information to justify a transformation; or
3. a method-compatible published ln-rMSSD distribution.

A raw RMSSD mean and SD should **not** simply be logged and treated as the mean and SD of ln-rMSSD.

### Measurement compatibility requirement

Before adopting this reference, verify:

- recording duration;
- resting posture;
- breathing/control conditions;
- ECG vs chest strap/wearable acquisition;
- artifact correction;
- RMSSD calculation method;
- preprocessing;
- timing of measurement.

## 8. TMT-B

TMT-B should not be represented as one universal normal interval.

Tombaugh's normative study included 911 community-dwelling adults aged 18–89 years and demonstrated that performance varied with age and education. The published norms were therefore stratified by age and education.

For Resilience Index, TMT-B should consequently use **demographically appropriate normative values**, not one fixed Nigerian-independent cutoff.

The pilot's primary outcome remains within-person change. The reference score is a normalization layer and does not constitute a diagnosis.

### Current limitation

A validated Nigerian healthy reference set for the exact TMT-B administration and target population has not yet been established for this project.

## 9. Digit Span

Digit Span also requires demographic consideration.

Published normative work demonstrates associations between Digit Span performance and age, education, and sex, with norms commonly stratified by these characteristics.

For Resilience Index, the preferred approach is therefore:

- age-adjusted;
- education-adjusted;
- sex-aware where supported by the selected normative source;
- standardized administration.

### Current limitation

The project does not currently have a sufficiently strong Nigerian healthy reference dataset for the exact Digit Span administration to replace established international norms.

A Nigerian dataset should be prioritized for future validation rather than forcing a weak local norm into the pilot.

## 10. What "global standard" means in this project

The project will not use a single global reference range.

Instead, "global" refers to **high-quality international normative evidence appropriate to the measurement**, especially where:

- a validated instrument has established normative methods;
- demographic stratification is available;
- local evidence is absent or insufficient;
- measurement administration is compatible.

This distinction prevents the project from presenting Western-derived norms as universal biological truths.

## 11. Reference data registry

Before a reference value enters production scoring code, the project should maintain a registry containing:

- variable name;
- domain;
- unit;
- transformation;
- reference population;
- country/region;
- age range;
- sex;
- education where relevant;
- sample size;
- inclusion/exclusion criteria;
- measurement method;
- device/assay;
- collection conditions;
- statistical method;
- mean;
- SD;
- reference limits;
- source DOI/URL;
- evidence tier;
- transferability assessment;
- verification status;
- date reviewed.

No production reference value should exist without a registry record.

## 12. Verification before use

Each candidate reference must pass:

### Population verification
Is the reference population sufficiently similar to the intended Resilience Index population?

### Method verification
Was the measurement generated using the same or demonstrably comparable method?

### Demographic verification
Are age, sex, education, and other relevant factors accounted for?

### Statistical verification
Are the required parameters available for the planned transformation and z-score?

### Biological verification
Are known physiological determinants or exclusions addressed?

### Transferability verification
If the source is outside Nigeria, is there sufficient justification for transfer?

### Sensitivity analysis
Would conclusions materially change under a credible alternative reference?

## 13. Long-term Nigerian reference cohort

A future dedicated Resilience Index reference study should recruit a healthy Nigerian reference cohort using a standardized protocol.

The objective would not merely be to obtain "normal ranges." It would be to establish **measurement-specific, population-aware distributions** for:

- CRP;
- HbA1c;
- ln-rMSSD;
- TMT-B;
- Digit Span.

For laboratory variables, the study should follow recognized reference-interval methodology, including careful reference-subject selection, pre-analytical standardization, analytical quality control, outlier handling, partition assessment, and appropriate statistical estimation.

For cognitive measures, the reference cohort should explicitly capture age and education and evaluate other relevant demographic effects.

## 14. What is fixed vs what remains open

### Fixed for the pilot

- healthy-reference normalization is the conceptual first layer;
- personal-baseline normalization is a separate longitudinal layer;
- CRP uses ln(CRP + 1) before standardization;
- higher-worse variables are direction-corrected;
- clinical and cognitive domains are combined using the protocol's 50/50 primary weighting, with 60/40 sensitivity analysis;
- reference sources and limitations will be disclosed.

### Not yet fixed

- final μ_ref and σ_ref for CRP;
- final μ_ref and σ_ref for HbA1c;
- transformed ln-rMSSD reference parameters;
- final TMT-B normative source/table implementation;
- final Digit Span normative source/table implementation;
- method-equivalence verification for every pilot assay/device;
- whether any variable requires demographic partitioning in the production score.

These should not be guessed.

## 15. Scientific position

The Resilience Index does not claim that an individual is "resilient" or "not resilient" because a single measurement falls inside or outside a population reference interval.

The reference layer establishes a **standardized starting point**.

The scientific construct of resilience is primarily tested through the **trajectory following a stressor**:

\`Baseline → Stressor → Response → Recovery\`

Therefore:

> Population reference = context for Reserve.

> Personal baseline + longitudinal trajectory = foundation for Bounce-back.

> Recovery trajectory = the core empirical test of the Resilience Index construct.

## 16. Primary sources identified for the current framework

1. Clinical and Laboratory Standards Institute. EP28 — Defining, Establishing, and Verifying Reference Intervals in the Clinical Laboratory.
2. Igila AF, Ojule AC. Reference Interval of Glycated Hemoglobin in Adults in Port Harcourt, Nigeria. Asian Journal of Medicine and Health. 2019.
3. Heart Rate Variability in Healthy Young Adult Nigerians. PubMed PMID 39340793.
4. Distribution of plasma C-reactive protein measured by high-sensitivity assay in healthy Nigerian adults.
5. Tombaugh TN. Trail Making Test A and B: Normative data stratified by age and education. Archives of Clinical Neuropsychology. 2004;19(2):203–214.
6. Published demographic normative studies for Digit Span, to be selected based on administration compatibility and target age/education range.

## 17. Decision-locked variable disposition

### CRP — NOT PRODUCTION-READY
The Nigerian study is retained as Tier 1 candidate evidence. It reports raw-scale mean/range but does not provide the transformed ln(CRP+1) mean and SD required by the scoring specification. The assay also differs from the planned point-of-care method. No CRP reference parameters enter production scoring until compatible transformed parameters are obtained.

### HbA1c — NOT PRODUCTION-READY
The Nigerian Port Harcourt study is retained as Tier 1 candidate evidence. Its nonparametric reference interval and raw-scale mean do not provide the SD required by the current z-score implementation. The study's boronate-affinity method must also be compared with the pilot assay. No SD will be inferred from the reference interval.

### ln-rMSSD — NOT PRODUCTION-READY
The Nigerian HRV study is strong Tier 1 candidate evidence (n=840; age 15–40), but it reports RMSSD, not ln-rMSSD. The raw mean and SD cannot be transformed by simply taking logarithms. Recording and acquisition compatibility must also be established.

### TMT-B — REFERENCE-TABLE PATH
Tombaugh's 911-person normative dataset is retained as Tier 3 candidate evidence because it explicitly stratifies by age and education. The project should implement the published normative table rather than collapse it into one universal mean/SD. The exact administration must be matched before production use. The source confirms age and education effects. citeturn0search0turn0search2

### Digit Span — REFERENCE-TABLE PATH
The Brazilian adult normative study provides age/education-stratified data for adults 19–75 and demonstrates education effects, but it is not Nigerian and should remain Tier 3 candidate evidence. It may support a sensitivity/reference-table pathway only after exact administration and cultural/linguistic compatibility are assessed. citeturn0search5turn0search6

### Pilot reference decision
The project will not promote any of the five current candidates to production merely to complete the score. The scoring engine remains deliberately blocked until the reference evidence satisfies the registry gate.

## 18. Decision rule

**No reference value enters the scoring engine merely because it is published.**

It enters only after:

\`Source identified → population assessed → method assessed → required statistics verified → transformation verified → transferability assessed → reference registered → sensitivity plan documented\`

This framework is therefore a prerequisite to finalizing the production scoring engine.
