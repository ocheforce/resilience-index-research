# Resilience Index — Reference Data Registry v0.1

This registry is the control point for every external reference value used by the scoring system.

**Rule:** no production reference parameter may be added to scoring code until its registry record is complete and marked **Verified**.

| ID | Variable | Population | Age | Sex | Education | Method/device/assay | Transformation | n | Mean | SD | Reference limits | Evidence tier | Status |
|---|---|---|---|---|---|---|---|---:|---:|---:|---|---|---|
| REF-CRP-NG-01 | CRP | Healthy adult Nigerians | Source-defined | Source-defined | N/A | Synthron CRP ultrasensitive ELISA | ln(CRP + 1) | 120 | 2.3 mg/L reported on raw scale | Not reported | 0.62–11.64 mg/L | Tier 1 | **Candidate — not verified for scoring** |
| REF-HBA1C-NG-01 | HbA1c | Apparently healthy adults, Port Harcourt | 20–80 | Source-defined | N/A | Boronate-affinity chromatography | None | 172 | 4.84% | Not reported | 4.0–5.9% | Tier 1 | **Candidate — not verified for scoring** |
| REF-HRV-NG-01 | RMSSD | Healthy young Nigerians | 15–40 | Sex reported | N/A | Short-term resting HRV | ln(RMSSD) required | 840 | 57 ms | 49 ms | Not established in source | Tier 1 | **Candidate — transformation/method verification required** |
| REF-TMT-INT-01 | TMT-B | Community-dwelling normative sample | 18–89 | Stratified in source | Stratified in source | Standardized TMT | Direction reversed for score | 911 | Source table | Source table | Normative tables | Tier 3 | **Candidate — table implementation required** |
| REF-DS-INT-01 | Digit Span | Healthy normative population | Source-defined | Source-defined | Source-defined | Standardized Digit Span | Direction preserved | Source-defined | Source table | Source table | Normative tables | Tier 3 | **Candidate — final source/administration match required** |

## Status definitions

- **Candidate:** evidence identified but not yet approved for production scoring.
- **Method verified:** measurement method is sufficiently compatible.
- **Statistically verified:** required parameters for the planned transformation are available and appropriate.
- **Verified:** population, method, statistics, transformation and transferability have all been reviewed.
- **Production:** approved for use in the scoring engine.

## Required fields before production

1. Source citation/DOI.
2. Reference population definition.
3. Inclusion/exclusion criteria.
4. Sample size.
5. Age range.
6. Sex partitioning where relevant.
7. Education partitioning where relevant.
8. Measurement method.
9. Device/assay where relevant.
10. Pre-analytical conditions.
11. Statistical method.
12. Mean and SD on the exact scoring scale, or an explicitly justified alternative representation.
13. Reference limits where available.
14. Transformation.
15. Transferability assessment.
16. Verification status.
17. Date and reviewer.

## Current interpretation

The current registry deliberately contains **no production z-score parameters for CRP, HbA1c, or ln-rMSSD**. Published reference intervals or raw-scale summaries are not sufficient by themselves to create those parameters.

The registry should be updated before the scoring engine is finalized.
