# The Resilience Index

## Pilot Validation Protocol — Submission Copy

**Submission Copy — October 2026**

### Protocol status

The protocol is prespecified for the funding application. Any substantive amendment after ethics submission or before data collection will be documented, dated, and approved through the appropriate ethics process.

## 1. Research Objective

Does the resilience score — measured before, immediately after, and during recovery from a real physiological/psychological stressor — detect a measurable drop and track recovery back toward individual baseline? Does failure to recover within the expected window associate with worse near-term outcomes?

## 2. Primary Hypothesis

Among athlete participants, resilience scores that fail to return to within a defined range of individual baseline by day 7–10 post-stressor will be associated with a measurable decline in standardized time-trial performance and self-reported readiness-to-train, compared to participants whose scores do recover.

## 3. Secondary Hypotheses

1. Cognitive independence: Does the cognitive-domain deficit area predict performance decline after controlling for the clinical-domain deficit area?
2. Clinical independence: Does the clinical-domain deficit area predict performance decline after controlling for the cognitive-domain deficit area?

These tests whether each domain adds unique information or whether one is redundant given the other.

## 4. Study Design

Prospective, single-arm observational pilot with no intervention/treatment arm. Participants are observed through a naturally occurring stressor rather than assigned one.

Each participant completes four repeated-measures touchpoints, enabling both a snapshot reserve reading and a recovery-trajectory bounce-back reading.

## 5. Participant Eligibility

### 5a. Inclusion

- Age 18–40.
- Actively competing/training in soccer, running, volleyball, tennis, or skating.
- Identifiable upcoming competition/event serving as the study stressor.
- Able to attend all four measurement touchpoints.
- Willing and able to provide informed consent.

### 5b. Exclusion

- Current injury or acute illness at enrollment.
- Pregnancy.
- Medications known to significantly affect CRP, HbA1c, or HRV independently of the stressor.

### 5c. Chronic conditions

A diagnosed chronic condition known to chronically affect one specific marker does not automatically exclude a participant. The condition is registered at enrollment and the specifically affected marker(s) are excluded from that participant’s clinical-domain deficit-area calculation for the primary analysis. Other markers, the cognitive domain, and performance outcome remain included.

### 5d. Baseline clean window

No illness, unusually hard training session, or major life stressor in the 48 hours before baseline, checked at baseline rather than only at enrollment.

## 6. Recruitment

Recruitment is administered through KoboToolbox using an independent human gatekeeper rather than a form or inbox personally monitored by the principal investigator. Institutional REDCap access may be explored as an upgrade.

Recruitment materials are informative rather than persuasive. They state the study purpose, four measurement touchpoints, fingerstick testing, cognitive testing, standardized sport-specific performance testing, participant results, voluntary participation, withdrawal rights, and the independent recruitment pathway.

Initial recruitment target: 120–150 individuals, aiming for approximately 100 completers.

## 7. Stressor Definition

Each participant’s own sport-specific competition/event serves as the stressor. No artificial standardized test is imposed across sports. Sport is included as a categorical covariate in the combined analysis.

## 8. Measurement Protocol

### 8a. Timepoints

1. Baseline — approximately 5 days pre-stressor, with the 48-hour clean-window check.
2. Acute — immediately/within hours after the event.
3. Peak — approximately 24–48 hours after the event.
4. Recovery check — day 7–10 after the event; exact day recorded.

### 8b. Biological measurements

| Variable | Domain | Direction | Collection |
|---|---|---|---|
| CRP | Clinical | Higher = worse | Fingerstick point-of-care |
| HbA1c | Clinical | Higher = worse | Fingerstick point-of-care |
| Resting ln-rMSSD HRV | Clinical | Higher = better in snapshot mode | Wearable/chest-strap, non-invasive |

eGFR is removed from v1 because it requires venous blood collection and no mature non-invasive substitute was identified. The resulting clinical panel is fixed at CRP, HbA1c, and HRV with no substitutions.

CRP and HRV are expected to change across the recovery window. HbA1c reflects average glycaemic exposure over approximately 8–12 weeks and is therefore retained as a stable reserve/baseline-capacity indicator rather than an acute recovery marker. A flat HbA1c across touchpoints is expected.

### 8c. Cognitive measurements

- TMT-B: processing speed and executive function; higher completion time = worse.
- Digit Span forward + backward: memory/working memory; higher = better.

### 8d. Performance and subjective measurement

| Sport | Standardized test |
|---|---|
| Soccer | Fixed-number shuttle sprints over a marked distance, timed |
| Running | Fixed-distance timed run |
| Volleyball | Vertical jump |
| Tennis | Serve-consistency/speed test |
| Skating | Fixed-distance timed skate |

Performance is never compared across sports or across people. Each participant is compared with their own earlier result in the same sport-specific test.

Primary performance outcome: percentage change from baseline, within-person and within-sport.

Subjective measures:
- Primary, all four touchpoints: Short Recovery and Stress Scale (SRSS).
- Secondary, baseline and day 7–10: RESTQ-Sport.

The time-trial is the external outcome against which the resilience score is evaluated, not a second independent readiness score.

## 9. Data Dictionary

Core fields include:

- participant_id
- timepoint
- sport
- age
- sex
- training_load
- recent_illness_med
- sleep_hours
- crp
- hba1c
- hrv_ln_rmssd
- tmt_b_seconds
- digit_span_score
- time_trial_result
- srss_score
- restq_score
- dropout_flag
- dropout_reason
- chronic_condition_flag
- affected_marker
- incidental_finding_flag

The fixed clinical panel is CRP, HbA1c, and standardized resting ln-rMSSD HRV.

## 10. Resilience-Score Calculation

### Reference population

The frozen z-scoring reference uses published international reference data:
- HbA1c: NHANES III young-adult data.
- CRP: NHANES reference distributions, log-transformed.
- HRV ln-rMSSD: Nunan et al. systematic review.
- TMT-B: established published age-based normative data, including Tombaugh’s normative study.
- Digit Span: WAIS normative data.

None of these sources is specifically normed on Nigerian or West African populations. This is an acknowledged limitation.

The pilot’s pooled baseline distribution is calculated and reported descriptively alongside the published reference but is not substituted as the z-scoring reference, avoiding circularity.

### Exact scoring steps

1. Raw values are collected.
2. Below-detection-limit values are replaced by LOD/2 and flagged with bdl_flag.
3. CRP is transformed as:

z_CRP = (ln(CRP + 1) − μ_ln_CRP_ref) / σ_ln_CRP_ref

4. HbA1c, HRV ln-rMSSD, TMT-B, and Digit Span use:

z_x = (x − μ_x_ref) / σ_x_ref

5. Sign is flipped for higher-is-worse variables: CRP, HbA1c, and TMT-B.
6. HRV and Digit Span retain their direction.
7. Clinical domain:

Clinical_z = mean(z_CRP, z_HbA1c, z_HRV)

8. Cognitive domain:

Cognitive_z = mean(z_TMT, z_DigitSpan)

9. Co-primary composite scores:

RI_5050 = 0.5 × Clinical_z + 0.5 × Cognitive_z

RI_6040 = 0.6 × Clinical_z + 0.4 × Cognitive_z

HbA1c and HRV values crossing validated device/laboratory clinical reference thresholds receive an outlier/clinical flag rather than being treated as simple linear “good” values at extremes.

## 11. Deficit-Area Calculation

The deficit is calculated at four touchpoints using each participant’s actual recorded day offsets.

Per-touchpoint deficit:

Deficit(t) = max(0, RI(baseline) − RI(t))

A recovery overshoot above baseline contributes zero rather than a negative deficit.

Trapezoidal area:

Area = Σ [0.5 × (Deficit(tᵢ) + Deficit(tᵢ₊₁)) × (tᵢ₊₁ − tᵢ)]

The sum is across baseline→acute, acute→peak, and peak→recovery, using actual day offsets.

Smaller area indicates better recovery/resilience.

Secondary recovery flag:

Recovered by day 7–10 = RI(recovery-check) within ±0.3 z of RI(baseline)

The ±0.3 threshold is a fixed pilot default and is not derived from test-retest reliability; refinement against reliability data is required before use in a published claim.

## 12. Statistical Analysis Plan

Primary analysis: linear regression of resilience-deficit area against percentage change in sport-specific performance, with sport as a categorical covariate.

Report effect estimate, 95% confidence interval, and p-value together.

The primary analysis is run under both 50/50 and 60/40 weighting as co-primary analyses.

### Incremental-value models

- Model A: Performance change ← HRV alone.
- Model B: Performance change ← CRP + HbA1c + HRV.
- Model C: Performance change ← CRP + HbA1c + HRV + cognition, with individual components unweighted.
- Model D: Performance change ← Resilience Index composite deficit-area score.

Models are compared for explanatory value, such as adjusted R² or a formal nested-model test.

The central question is whether Model D explains meaningfully more variance than HRV alone or individual components.

### Full differentiation framework

1. RI vs HRV alone — Model A vs D.
2. RI vs conventional biomarkers — Model B/C vs D.
3. Composite vs individual components — Model C vs D.
4. Clinical vs cognitive domain — secondary hypotheses.
5. Personal-baseline vs population-normalized scoring:
   - Model E: healthy-reference-normalized deficit area.
   - Model F: personal-baseline-normalized deficit area.
6. Existing commercial recovery/readiness platforms — exploratory only where participant-owned data are available and consented; not confirmatory.

Per-sport breakdowns are descriptive/exploratory rather than independently confirmatory.

The athlete population is a resource-driven proving ground, not the target market. Broader populations and stressor types are future validation stages.

## 13. Missing-Data Rules

For one missing internal touchpoint, linear interpolation is applied identically to every participant.

For a missing baseline or recovery edge touchpoint, the deficit area uses the available touchpoints and is flagged with partial_curve_flag.

More than one missing touchpoint for a variable is treated as a dropout for that variable; interpolation is not extended across multiple gaps.

Dropouts are recorded with reasons. Injury/illness dropouts are treated as potentially informative missingness. Dropout rates and reasons are reported separately. Primary analysis uses complete/usable cases with sensitivity analysis for plausible missing outcomes.

## 14. Confounders / Covariates

Collected and adjusted for alongside sport:

1. Age.
2. Sex.
3. Training load / fitness level.
4. Recent illness/medication not severe enough to exclude.
5. Sleep around measurement touchpoints.

## 15. Sensitivity Analyses

| Check | Primary assumption | Alternative |
|---|---|---|
| Weighting | 50/50 clinical/cognitive | 60/40 clinical/cognitive |
| Relationship shape | Linear | Evidence-based non-linear model |
| Missing data | Complete-case analysis | Alternative missing-outcome assumptions |
| Incidental clinical findings | All participants included | Exclude flagged clinically significant readings |

## 16. Falsification Criteria

The index is considered unsupported if:

1. Deficit area shows no practically meaningful association with performance change.
2. The association becomes trivial or reverses after sport adjustment.
3. The result is not robust to prespecified sensitivity analyses.
4. A consistent opposite-direction association is observed.
5. Model D fails to explain meaningfully more variance than HRV alone (Model A).

A concrete threshold for “practically meaningful” effect size must be defined before analysis.

Models E/F are diagnostic rather than falsification conditions. If population normalization outperforms personal-baseline normalization, that informs revision of the scoring architecture rather than falsifying the overall construct.

## 17. Ethical / Safety Considerations

### 17a. Consent and recruitment-pressure mitigation

Recruitment through personal networks creates risk of undue influence. Safeguards include a neutral recruitment link, an independent gatekeeper, explicit voluntary-participation language, independent participant contact, generated participant IDs, de-identified analysis, and separate storage of the ID-to-name key.

### 17b. Incidental findings

Pre-defined thresholds use validated device/laboratory clinical reference ranges.

Potentially clinically significant results receive a plain, non-diagnostic notice recommending discussion with a qualified healthcare professional.

Flagged participants remain in the primary analysis. A sensitivity analysis excludes flagged participants to assess whether underlying medical conditions drive the result.

### 17c. Data confidentiality

Row-level de-identified data are accessible only to the direct scoring/statistical analysis team.

Aggregated results are the default for public sharing and external collaboration. A funder/evaluator may review de-identified row-level data when legitimately required, and this exception is disclosed in consent.

### 17d. Withdrawal

Participants may withdraw at any time through the independent recruitment channel without giving a reason. Data already collected are retained unless the participant specifically requests deletion.

### 17e. Formal ethics pathway

Nigeria’s National Health Act Section 34 requires ethics committee review for health research.

For this single-site pilot, the realistic pathway is an existing NHREC-registered Health Research Ethics Committee connected to an appropriate hospital/research institution, subject to formal submission and approval.

Potential backup institutional pathways include NIMR or IHVN.

The finalized budget uses a directly quoted ₦20,000 hospital ethics-review fee.

## 18. Data-Management / Privacy Plan

### 18a. Storage

Preferred: REDCap, contingent on institutional access.

Fallback: KoboToolbox with regular backups to encrypted, access-restricted cloud storage.

Unencrypted local spreadsheets are explicitly avoided.

### 18b. Access

Row-level de-identified data are restricted to the scoring/statistical analysis team. The ID-to-name key is held separately by recruitment/scheduling personnel.

### 18c. Pseudonymization

Each participant receives a generated ID. Scientific analysis uses the ID rather than names.

### 18d. Retention

Data are retained for 5 years after study completion and then securely deleted. This period is disclosed in consent.

### 18e. Relationship to long-term product infrastructure

The pilot uses simple research-grade data management. Blockchain encryption, continuous wearable data, and global product infrastructure are later-stage decisions and are not prerequisites for scientific validation.

## 19. Sample-Size Justification

The pilot uses dual justification.

### Justification 1 — correlation-based calculation

Using Fisher z-transformation, two-tailed α=0.05 and 80% power:

| Assumed r | Required n |
|---|---:|
| 0.20 | ~194 |
| 0.25 | ~123 |
| 0.30 | ~85 |
| 0.35 | ~62 |

A moderate effect of approximately r=0.30 is used as the working anchor. Approximately 85 participants are required at r=0.30, and dropout-adjusted recruitment of 120–150 supports approximately 90–105 completers.

### Justification 2 — pilot-study conventions

Julious (2005) and Whitehead et al. (2016) provide accepted pilot/feasibility sample-size conventions. A target of approximately 100 completers exceeds published rule-of-thumb minimums.

### Honest interpretation

At n=100 completers, the pilot is adequately powered for a moderate effect around r=0.28–0.30 but underpowered for a smaller effect around r=0.20. This limitation will be stated explicitly.

A future confirmatory study should use the observed pilot effect size and a statistician-verified power calculation.

## Protocol status

The protocol is prespecified for the funding application. All 20 protocol items are finalized for the pilot. Any substantive amendment after ethics submission or before data collection will be documented, dated, and approved through the appropriate ethics process.