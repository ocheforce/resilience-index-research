# The Resilience Index

## Scientific Architecture — Submission Copy

**Submission Copy — October 2026**

### Resilience Index — Scientific Architecture (v1)

#### 1. What “Resilience” Means Here

Resilience is defined along two related but distinct meanings:

**Reserve (Meaning A):** A person’s current biological/cognitive capacity, measured at a single point in time.

**Bounce-back (Meaning B):** How well and how quickly a person recovers after a stressor (illness, deployment, injury), measured through repeated readings over time.

The product is designed to capture both, using the same underlying architecture:
- A first-time user receives a Meaning-A style result compared with a healthy reference standard.
- A returning user receives their current result compared with the healthy reference plus a second, separate comparison against their own personal baseline/trend — allowing the system to naturally accumulate toward a Meaning-B (bounce-back) picture as more data points are collected.

Resilience is treated as a predictor, not an outcome. Longevity and well-being (healthspan) are the outcomes resilience is intended to explain — tracked separately, never folded into the resilience score itself, to avoid circular measurement.

#### 2. Domains

v1 domains, selected for strong existing evidence base and low-cost/no-license data collection, buildable solo:

| Domain | Rationale |
|---|---|
| Clinical/physiological | Captures inflammatory, metabolic, organ-function, and cardiovascular status — the core “reserve” layer with the deepest existing evidence base. |
| Cognitive | Directly tracks cognitive decline, the product’s named priority; independent of physical/clinical status. |

Planned expansion roadmap (Phase 2/3, contingent on grant funding/partnerships):
- Microbiome/resistome — captures resilience to infection and antibiotic resistance, not well detected by clinical/cognitive markers alone.
- Physical/functional (grip strength, gait speed) — directly relevant to military fitness-for-duty use case.
- Psychological/stress (e.g., cortisol patterns) — relevant to bounce-back/recovery dynamics specifically.

#### 3. Variables per Domain

**Clinical/physiological**
- CRP (C-reactive protein): inflammation; higher = worse; fingerstick point-of-care device.
- HbA1c (fixed — not “or lipid panel”): metabolic health; higher = worse; fingerstick point-of-care device.
- HRV (heart rate variability): cardiovascular/autonomic function; bounce-back marker; higher = better (v1); recovery-dynamics version planned for continuous-use refinement; wearable/chest-strap device, non-invasive.

eGFR was removed from v1 because it requires a venous blood draw and there is no mature non-invasive substitute. Salivary creatinine/urea shows real correlation with serum levels across multiple studies, but is still described in its literature as requiring further validation before clinical implementation, is evaluated mostly in diagnosed CKD populations rather than healthy people, and lacks an established “salivary eGFR” equation. It remains a candidate for v2 once salivary kidney-function biomarkers mature further.

Clinical domain is therefore 3 variables (CRP, HbA1c, HRV), not 4.

**Cognitive**
- Trail Making Test (TMT): processing speed + executive function; higher time = worse; free, validated, published norms.
- Digit Span (forward + backward): short-term memory + working memory; higher = better; free, part of WAIS lineage, published norms.

#### 4. Normalization

1. Collect raw variable values.
2. Log-transform CRP before further processing to correct its right-skewed distribution. Other variables will be checked empirically via histogram once pilot data exists, not assumed symmetric by default.
3. Compare each value to a healthy-reference distribution rather than simple age-matched peer norms. Reference populations are sourced from published international norms (NHANES for CRP/HbA1c, Nunan et al. for HRV, Tombaugh/WAIS norms for TMT/Digit Span), with the pilot’s pooled baseline data compared alongside as a population-fit check. The limitation that no Nigerian/West African-normed reference exists is disclosed in the pilot protocol.
4. Calculate a z-score for each variable against that healthy reference.
5. Flip the sign on higher-is-worse variables (CRP, HbA1c, TMT) so all variables point in a consistent “higher = more resilient” direction.
6. Leave sign as-is on higher-is-better variables (HRV, Digit Span).
7. Comparison display, per visit:
   - First-time user: result shown against the healthy-reference standard only.
   - Returning user: healthy-reference comparison plus a separate personal-baseline trend comparison, shown as two parallel results (not blended into one number) for v1.
8. Outlier flag for non-linear-relationship variables (v1 safeguard): for HbA1c and HRV, where evidence shows reverse-J/U-shaped or confound-sensitive relationships at the extremes, an extreme-tail value triggers a warning marker rather than being scored as a simple linear “good” z-score.

#### 5. Combining Domains

Within-domain combination is the simple average of normalized, direction-corrected variable z-scores.

- Clinical domain score = average of CRP, HbA1c, HRV z-scores.
- Cognitive domain score = average of TMT, Digit Span z-scores.
- Cross-domain combination = equal weighting (50/50) average of clinical and cognitive domain scores for v1.

Equal weighting is an explicit starting assumption, not a validated finding. A 60/40 clinical/cognitive weighting hypothesis is tested through sensitivity analysis.

The pilot’s primary analysis is run under both weightings and results reported honestly under whichever the data better supports, because 50/50 is itself an active, currently-unproven claim that the two domains matter equally.

#### 6. Evidence Table

The evidence policy is to include foundational and long-follow-up longitudinal studies regardless of age where long follow-up is required to demonstrate mortality/longevity relationships. Reference ranges and cutoff values will be sourced from the last 5–10 years to reflect current population baselines. Every citation is independently traceable (author/journal/year), not sourced from an unverified or AI-generated summary alone.

| Variable | Claimed relationship | Evidence type | Strength | Notes / caveats |
|---|---|---|---|---|
| CRP | Higher CRP → higher long-term all-cause and cardiovascular mortality risk | Prospective longitudinal cohort, replicated across independent populations (PREVEND/Framingham; CHARLS; Taiwan HALST) | Strong | Hospital-mortality studies in acutely ill patients answer a different question than general-population resilience and are not used as primary support. |
| HbA1c | Higher HbA1c → worse metabolic health/mortality; very low HbA1c → elevated risk mainly in diabetic/frail populations | Longitudinal cohort (Lancet Diabetes & Endocrinology, UK cohort) + meta-analysis of 6 population cohorts (28,681 participants) | Strong for high-HbA1c direction; moderate/confound-dependent for low-end risk | v1 keeps simple higher = worse flip; very-low readings are flagged for review because of possible nutrition/anemia confounding. |
| eGFR | Lower eGFR → higher mortality risk; possible reverse-J pattern | Prospective longitudinal cohorts, replicated across independent populations | Strong for low-eGFR direction; moderate/debated for high-eGFR upturn | Removed from v1 because of venous-blood-draw requirement and lack of a mature non-invasive substitute; retained as a v2 reference. |
| HRV | Lower HRV → higher all-cause mortality risk; relationship with age is non-linear | Longitudinal cohort with long follow-up plus cross-sectional norms literature | Strong for core mortality direction | v1 keeps higher = better for snapshot mode and prioritizes personal-trend comparison because of large interindividual variability. |
| Trail Making Test | Worse/slower TMT-B → cognitive decline/dementia risk; also associated with broader physical decline/mortality | Longitudinal cohorts and independent replicated studies | Strong | Confounded by education/IQ and physical function; not a pure cognition-only signal. |
| Digit Span | Impaired digit span associated with cognitive decline | Longitudinal clinical-population cohorts | Moderate | Directionally supported but inconsistent; strengthens the cognitive domain by covering a different memory/working-memory subdomain than TMT. |

A cross-cutting pattern in the evidence review is that HbA1c and HRV show non-linear or confound-sensitive relationships, particularly at extreme low values. This should be revisited when moving beyond simple linear z-score normalization toward a validated v2.

#### 7. What Can Legitimately Be Predicted vs. Merely Associated

An association is a relationship observed in existing data. A prediction is a claim validated on data the model has not seen, ideally using a held-out or prospective sample.

Current evidence supports association only, not prediction. The five remaining v1 variables (CRP, HbA1c, HRV, TMT, Digit Span) have credible published associations with resilience-relevant outcomes such as mortality, cognitive decline, and frailty. This justifies inclusion but does not validate this specific Resilience Index for its intended users.

To legitimately claim prediction, the score must be built on a real pilot dataset, tested on withheld or separate prospective data, shown to forecast real outcomes, and ideally replicated in an independent population.

Until that validation exists, public materials should use association language such as “informed by,” “associated with,” and “based on established biomarkers of,” rather than claiming that the score predicts longevity or decline.

A falsifiability check should be built in early by defining in advance what result would show that the index is not working.

## Pilot Validation Framework

### A. Research Question

Does the resilience score — measured before, immediately after, and during recovery from a real physiological/psychological stressor — detect a measurable drop and track recovery back toward individual baseline?

Does failure to recover within the expected window associate with worse near-term outcomes?

### B. Primary Hypothesis

Among athlete participants, resilience scores that fail to return to within a defined range of individual baseline by day 7–10 post-stressor will be associated with a measurable decline in standardized time-trial performance and self-reported readiness-to-train, compared to participants whose scores do recover.

Evidence supporting the schedule includes evidence that CRP peaks around 24 hours after intense exercise and resolves over subsequent days, while HRV recovery is intensity-dependent. Published sports-science studies also support the use of standardized performance testing and subjective readiness measures for recovery assessment.

### C. Secondary Hypotheses

1. **Cognitive independence:** Does the cognitive-domain deficit area predict performance decline after controlling for the clinical-domain deficit area?
2. **Clinical independence:** Does the clinical-domain deficit area predict performance decline after controlling for the cognitive-domain deficit area?

The purpose is to determine whether each domain contributes information beyond the other, rather than merely asking whether each domain works alone.

### D. Study Population

Primary track: approximately 100 mixed-sport athletes (soccer, running, volleyball, tennis, skating). Each sport’s natural competition/event serves as the stressor. Sport is tracked as a covariate in one combined analysis rather than five separate underpowered studies.

Exploratory tracks include medical professional friends/nurses/hospital staff and elderly villagers as smaller descriptive sub-studies, not independently powered to confirm the primary hypothesis.

Athletes are selected because competition provides accessible stressor timing and observable performance outcomes. The niche population is also a resource-driven pilot choice, not a claim that the product is intended only for athletes. The athlete pilot is a proving ground, not the target market.

### E. Sample Size

The target of approximately 100 completers is supported by two independent justifications:
1. A literature-anchored correlation-based power calculation using a moderate effect anchor around r≈0.30 gives approximately 85 participants for 80% power, with dropout-adjusted recruitment of 120–150.
2. Accepted pilot-study sample-size conventions (Julious 2005; Whitehead et al. 2016) place 100 above published rule-of-thumb minimums.

A statistician remains valuable for a future larger confirmatory study once this pilot generates real effect-size data.

### F. Measurement Schedule

Four touchpoints per participant:
1. Baseline — approximately 5 days pre-stressor, with an inclusion check for no illness, unusually hard training session, or major life stressor in the prior 48 hours.
2. Acute — immediately/within hours after the event.
3. Peak — approximately 24–48 hours after the event.
4. Recovery check — day 7–10 window, with exact day recorded.

Approximately 400 data-collection sessions are expected across 100 athletes.

### G. Outcomes

The primary continuous outcome is individual resilience-deficit area: the area between the person's resilience-score curve and personal baseline across baseline→acute→peak→recovery-check using trapezoidal approximation. It captures both depth of dip and speed of recovery; smaller area indicates better recovery.

A secondary binary “recovered by day 7–10” flag uses a frozen pilot default of within ±0.3 z of baseline, with the limitation that this threshold should ideally be refined using reliability data before any published claim.

Performance-side outcomes include percentage change in standardized time-trial result and readiness-to-train questionnaire score at day 7–10.

### H. Statistical Analysis

Primary analysis: linear regression assessing the association between resilience-deficit area and subsequent percentage change in sport-specific performance, with sport as a categorical covariate. Report effect estimate, 95% confidence interval, and p-value together.

Differentiation comparator framework:
- Model A vs D: Resilience Index vs HRV alone.
- Model B/C vs D: composite vs conventional biomarkers/individual components.
- Clinical vs cognitive domain: through the secondary hypotheses.
- Model E vs F: personal-baseline-normalized vs population-normalized score.
- Exploratory RI vs WHOOP/Oura where participants already have data; descriptive only because the subset is unlikely to be adequately powered.

If Model D fails to outperform HRV alone or the individual components, that is a genuine finding that the multidomain construct adds little.

### I. Missing Data

For a missed internal touchpoint with readings available on both sides, linear interpolation is applied identically to every participant.

A missing edge touchpoint uses only available touchpoints for the variable’s deficit-area calculation and is flagged. More than one missing touchpoint for a variable is classified as a dropout for that variable rather than further imputed.

Every dropout and reason is recorded. Injury/illness-related dropout is treated as potentially informative missingness. The primary analysis uses participants with the prespecified required measurements, with sensitivity analysis testing plausible assumptions about missing outcomes.

### J. Sensitivity Analysis

| Sensitivity check | Primary assumption | Alternative tested |
|---|---|---|
| Weighting | 50% clinical / 50% cognitive | 60% clinical / 40% cognitive |
| Relationship shape | Linear | Evidence-based non-linear model |
| Missing data | Prespecified complete/usable-data analysis | Alternative assumptions about missing outcomes |
| Incidental clinical findings | All participants included | Participants with flagged clinically significant readings excluded |

The overarching question is whether a larger resilience-deficit area remains associated with greater subsequent performance decline under reasonable alternative assumptions.

This pilot validates whether the score can detect and track a single stress-recovery cycle. It does not, on its own, validate repeated-stressor prediction over long periods; that broader claim requires later longitudinal data.

### K. External Validation

1. Cross-population validation in health workers/nurses to test generalization beyond athletes.
2. Elder track to test healthy-reference/personal-baseline design over longer horizons.
3. Independent replication by a different research team, contingent on later funding/partnerships.

### L. Falsification Criteria

The Resilience Index will be considered unsupported in its current formulation if:
1. Resilience-deficit area demonstrates no practically meaningful association with subsequent performance change.
2. The association becomes trivial or reverses after sport adjustment.
3. The observed association is not robust to prespecified sensitivity analyses.
4. A consistent association in the opposite direction is observed.
5. The composite Resilience Index (Model D) fails to explain meaningfully more variance in performance change than HRV alone (Model A).

A concrete effect-size threshold for “practically meaningful” must be defined before analysis; statistical significance alone is not sufficient.

Models E/F are diagnostic rather than falsification conditions. If population normalization outperforms personal-baseline normalization, that is evidence for revisiting the score architecture rather than evidence against the overall construct.

## Longer-Term Product and Infrastructure Roadmap

Continuous tracking via wearable-compatible devices; usable as both a one-time check and ongoing tracking.

Future data infrastructure may include privacy-preserving and distributed technologies. These are separate from the scientific validation architecture and will be evaluated only after scientific evidence supports further development.

Target adopters include doctors for patient health tracking, military fitness-for-duty applications, and other longevity/well-being use cases.

Regulated-use consideration: clinical decision-support and military fitness-for-duty determinations may require regulatory clearance before real-world deployment. That compliance workstream is separate from the science and will be revisited once the evidence base is developed.