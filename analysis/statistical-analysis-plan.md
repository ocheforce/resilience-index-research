# Statistical Analysis Plan

## Purpose

This analysis plan translates the prespecified Resilience Index pilot protocol into a reproducible computational workflow.

The protocol remains the authoritative source for the study design, frozen scoring rules, primary outcome, missing-data rules, sensitivity analyses, and falsification criteria.

## Primary analysis

Primary predictor: **Resilience-deficit area** across the four touchpoints.

Primary outcome: **Percentage change in standardized sport-specific performance from baseline.**

Primary model: **Linear regression of performance change on resilience-deficit area, with sport as a categorical covariate.**

The analysis will be run under both prespecified composite weightings:

- RI_5050 = 0.5 × Clinical_z + 0.5 × Cognitive_z
- RI_6040 = 0.6 × Clinical_z + 0.4 × Cognitive_z

Report effect estimate, 95% confidence interval, and p-value together.

## Scoring pipeline

1. Validate raw data and participant/touchpoint identifiers.
2. Apply below-detection-limit handling.
3. Apply the frozen CRP transformation.
4. Calculate healthy-reference z-scores.
5. Apply direction correction.
6. Calculate clinical and cognitive domain scores.
7. Calculate both composite scores.
8. Calculate touchpoint deficits relative to baseline.
9. Calculate trapezoidal deficit area using actual day offsets.
10. Calculate percentage performance change within participant and sport.

No scoring rule should be learned from outcome data.

## Comparator models

- **Model A:** HRV alone.
- **Model B:** CRP + HbA1c + HRV.
- **Model C:** all individual clinical and cognitive components, unweighted.
- **Model D:** Resilience Index composite deficit area.
- **Model E:** healthy-reference-normalized deficit area.
- **Model F:** personal-baseline-normalized deficit area.

Commercial recovery-platform comparisons are exploratory and only performed where participant-owned data are available with appropriate consent.

## Secondary analyses

- Clinical-domain deficit area adjusted for cognitive-domain deficit area.
- Cognitive-domain deficit area adjusted for clinical-domain deficit area.
- Exploratory per-sport descriptive results.
- SRSS relationship with the physiological/cognitive score.
- RESTQ-Sport baseline/recovery cross-check.
- Descriptive comparison of pilot pooled baseline values with published reference distributions.

## Sensitivity analyses

- 50/50 versus 60/40 weighting.
- Linear versus evidence-based non-linear relationships.
- Alternative assumptions for missing outcomes.
- Exclusion of participants with flagged clinically significant incidental findings.

## Missing data

One internal missing touchpoint is linearly interpolated.

A missing baseline or recovery edge uses an available-timepoint trapezoidal calculation and is flagged.

More than one missing touchpoint for a variable is treated as a dropout for that variable.

Injury/illness-related dropout is treated as potentially informative missingness and addressed in sensitivity analysis.

## Falsification

The current architecture is unsupported if:

1. Deficit area has no practically meaningful association with performance change.
2. The association becomes trivial or reverses after sport adjustment.
3. The finding is not robust to prespecified sensitivity analyses.
4. The association consistently runs in the opposite direction.
5. The composite fails to provide meaningful incremental explanatory value over HRV alone.

The practical effect-size threshold must be specified before the final analysis.

## Reproducibility

All analysis code should:

- use versioned dependencies;
- avoid hidden manual transformations;
- document every derived variable;
- preserve raw data separately from derived analysis data;
- generate figures/tables through scripts or notebooks that can be rerun;
- record analysis version and protocol version;
- distinguish prespecified analyses from exploratory analyses.

No participant-identifying information belongs in the repository.
