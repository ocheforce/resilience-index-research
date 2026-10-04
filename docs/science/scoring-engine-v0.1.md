# Scoring Engine v0.1

## Purpose

This module turns the prespecified pilot scoring rules into deterministic, inspectable research code. It is not a clinical decision engine.

## Implemented rules

1. Reference-normalized z-scores require explicitly verified reference parameters.
2. CRP uses the frozen ln(CRP + 1) transformation before z-scoring.
3. Higher-is-worse variables can be direction-corrected by sign reversal.
4. Clinical_z and Cognitive_z are simple means of their component z-scores.
5. RI_5050 = 0.5 Clinical_z + 0.5 Cognitive_z.
6. RI_6040 = 0.6 Clinical_z + 0.4 Cognitive_z.
7. Deficit(t) = max(0, RI_baseline - RI(t)).
8. Deficit area uses trapezoidal integration over actual day offsets.
9. Recovery is within ±0.3 z units of baseline unless the frozen protocol is amended.
10. Exactly one internal missing touchpoint can be linearly interpolated; edge missingness is not silently imputed.

## Reference safety

Candidate reference values from the reference registry are not embedded in the code. A reference must be marked verified before scoring can use it. This prevents incomplete literature evidence from becoming an accidental production parameter.

## Validation boundary

Unit tests verify computational behavior using synthetic values. They do not validate the biological construct, reference distributions, device equivalence, or clinical utility. Those questions require empirical study.