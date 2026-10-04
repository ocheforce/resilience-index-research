# Resilience Index

**Making recovery capacity measurable.**

Resilience Index is an open biomedical research project investigating whether multidomain physiological and cognitive recovery can be measured longitudinally following real-world stress.

## Current stage

### Stage 1 — Measure

The initial objective is to make an individual's recovery capacity measurable and trackable over time.

The pilot asks:

> **Can we objectively measure an individual's recovery trajectory following a real-world stressor, and determine whether a multidomain measure provides information beyond HRV alone?**

The project separates two related aspects of resilience:

- **Reserve:** current biological and cognitive capacity.
- **Bounce-back:** how well and how quickly the individual returns toward baseline after a stressor.

Stage 2 will investigate factors and interventions that may improve recovery capacity. Future work may develop a closed-loop system: **Measure → Understand → Recommend → Intervene → Re-measure.**

The current pilot does not claim to diagnose disease, predict longevity, prevent burnout, or provide clinically validated recommendations.

## Pilot

The current study is a prospective, single-arm observational pilot in approximately 100 completers, with 120–150 participants recruited.

Participants are adults aged 18–40 who actively train or compete in soccer, running, volleyball, tennis, or skating.

Four assessment touchpoints are planned:

1. Baseline — approximately 5 days before the event
2. Acute — immediately after or within hours of the event
3. Peak — approximately 24–48 hours
4. Recovery — approximately 7–10 days

### Measures

**Clinical / physiological**
- C-reactive protein (CRP)
- HbA1c
- Resting ln-rMSSD heart-rate variability (HRV)

**Cognitive**
- Trail Making Test Part B (TMT-B)
- Digit Span

**Functional**
- Sport-specific within-person performance measure

**Subjective**
- Short Recovery-Stress Scale (SRSS)
- RESTQ-Sport as a secondary baseline/recovery measure

## Composite score

The pilot evaluates two prespecified weighting schemes:

```text
RI_50/50 = 0.5 × Clinical_z + 0.5 × Cognitive_z

RI_60/40 = 0.6 × Clinical_z + 0.4 × Cognitive_z
```

Recovery deficit is defined as:

```text
Deficit(t) = max(0, RI(baseline) - RI(t))
```

The primary analysis evaluates whether the area of resilience deficit across the observation period is associated with percentage change in standardized sport-specific performance, with sport included as a categorical covariate.

## Validation and falsification

The composite will be compared against:

- HRV alone
- conventional clinical biomarkers
- individual components
- clinical-domain and cognitive-domain measures
- an unweighted clinical + cognitive model

The project is explicitly falsifiable. The hypothesis will be considered unsupported if the association is absent, practically trivial, reverses after sport adjustment, is not robust to prespecified sensitivity analyses, consistently runs in the opposite direction, or the composite does not meaningfully explain more variance than HRV alone.

## Scientific boundaries

This repository represents a research program, not a validated clinical product.

The current pilot does **not** establish:

- universal validity across populations
- disease diagnosis
- longevity prediction
- prevention of illness or burnout
- clinical superiority over consumer recovery platforms
- individualized treatment recommendations

Those questions require subsequent validation.

## Roadmap

**Stage 1 — Measure**

Establish whether recovery capacity can be measured and tracked longitudinally following real-world stress.

**Stage 2 — Improve**

Investigate what factors or interventions improve recovery capacity.

**Stage 3 — Personalize**

Investigate whether recovery interventions can be individualized around the question:

> **What works specifically for you?**

## Open science

The project is intended to develop openly where ethics, participant confidentiality, and data-protection requirements permit.

The repository will contain the research protocol, scientific architecture, analysis plan, reproducible code, synthetic/example data where appropriate, and study outputs as they become available.

Aggregate results will be shared publicly. Row-level participant data will only be shared when permitted by consent, ethics approval, and applicable data-protection requirements.

## Repository structure

```text
docs/          Study documents and scientific documentation
analysis/      Statistical analysis plan, notebooks, and figures
data/          Synthetic/example data and data documentation
src/           Reusable analysis code
scripts/       Reproducibility and utility scripts
workflows/     Computational workflows
tests/         Tests for analysis components
legacy/        Notes pointing to older, separate project infrastructure
```

The older computational Resilience Index pipeline based on All of Us / HMP-resistome demonstration data is intentionally kept separate from this research repository.

## Core documents

The project documentation includes:

- Concept Note
- Full Proposal
- Scientific Architecture
- Pilot Protocol
- Pilot Budget
- Timeline
- Risk Management Plan
- Dissemination & Impact Plan

## Funding target

The current recommended pilot budget is **₦10,148,320 (approximately US$6,765 at the planning exchange rate used in the budget)**.

## Project lead

**Ali Wisdom (Penforce)**  
Medical Laboratory Scientist · Biomedical Research Analyst

The project is being developed as an open, reproducible biomedical research program with the long-term goal of translating validated recovery science into useful tools and products.