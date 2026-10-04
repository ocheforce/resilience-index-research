# Resilience Index — Project Diagram

## Scientific architecture

```mermaid
flowchart TD
    A[Healthy active adult] --> B[Baseline<br/>~5 days pre-event]
    B --> C[Real-world stressor<br/>competition/event]
    C --> D[Acute<br/>immediately / hours]
    D --> E[Peak<br/>24–48 hours]
    E --> F[Recovery<br/>day 7–10]

    B --> G[CRP · HbA1c · ln-rMSSD HRV]
    B --> H[TMT-B · Digit Span]
    B --> I[Sport-specific performance · SRSS]
    D --> G
    D --> H
    D --> I
    E --> G
    E --> H
    E --> I
    F --> G
    F --> H
    F --> I

    G --> J[Reference normalization]
    H --> J
    J --> K[Clinical_z + Cognitive_z]
    K --> L[RI 50/50<br/>RI 60/40]
    L --> M[Baseline-relative deficit]
    M --> N[Recovery trajectory<br/>+ trapezoidal deficit area]

    I --> O[Performance change]
    N --> P{Primary research question}
    O --> P
    P --> Q[Does multidomain recovery<br/>explain performance change<br/>beyond HRV alone?]
```

## Interpretation

The project treats resilience as a **trajectory**, not a single snapshot:

**Baseline → Stressor → Response → Recovery**

The pilot first asks whether this trajectory can be measured reproducibly. It then tests whether the multidomain signal contains information about performance change beyond HRV alone.

This is a research architecture diagram, not a clinical decision pathway. It does not imply diagnostic validity or treatment recommendations.
