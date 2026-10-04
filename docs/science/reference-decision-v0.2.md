# Reference Standard Decision v0.2

## Outcome

The reference-standard bottleneck is now **decision-locked**, not hidden.

| Variable | Decision | Why |
|---|---|---|
| CRP | Blocked | Nigerian source lacks transformed ln(CRP+1) mean/SD and uses a different assay |
| HbA1c | Blocked | Nigerian source lacks SD; nonparametric interval cannot be silently converted |
| ln-rMSSD | Blocked | Nigerian source reports RMSSD, not ln-rMSSD; method compatibility remains open |
| TMT-B | Normative-table pathway | Strong age/education-stratified international norms; exact administration must match |
| Digit Span | Normative-table pathway | Demographic norms exist, but Nigerian/cultural and administration compatibility remain open |

## Scientific rule

No missing parameter will be estimated merely to make the scoring engine operational.

The project therefore retains a clean distinction between:

**candidate evidence → verified reference → production parameter**

The current scoring engine is correctly blocked from using unverified external parameters.

## Evidence anchors

The Nigerian CRP study reports n=120, raw hs-CRP mean 2.3 mg/L and range 0.62–11.64 mg/L, but does not provide the transformed distribution required by the score.

The Nigerian HbA1c study reports n=172, mean 4.84%, and a nonparametric reference interval of 4.0–5.9%; the source explicitly describes skewness, so the interval should not be reverse-engineered into an SD.

The Nigerian HRV study reports n=840 and RMSSD 57 ± 49 ms, with sex differences and methodological/contextual determinants; it does not provide the required ln-rMSSD distribution.

Tombaugh's TMT norms use 911 adults and stratify by age and education, supporting a normative-table implementation rather than a universal cutoff.

The Brazilian Digit Span study provides adult normative data with education-stratified groups and reports education effects; it remains external candidate evidence rather than a Nigerian norm.

## Next evidence actions

1. Obtain exact CRP distributional statistics or compatible participant-level data, or identify a method-compatible Nigerian dataset.
2. Obtain HbA1c SD/appropriate distributional parameters from the source or a method-compatible dataset.
3. Obtain ln-rMSSD-compatible Nigerian reference data or participant-level RMSSD data plus a defensible transformation pathway.
4. Implement demographic normative tables for TMT-B and Digit Span only after exact administration compatibility is documented.
5. Re-run transferability and sensitivity review before any parameter becomes Verified.

This closes the framework bottleneck without compromising scientific validity.
