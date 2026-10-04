# Resilience Index Analysis Package

The package contains deterministic research-analysis primitives implementing the frozen pilot scoring rules.

## v0.1 scoring engine

Implemented:

- verified-reference z-scores;
- frozen ln(CRP + 1) transformation;
- direction correction for higher-is-worse variables;
- Clinical_z and Cognitive_z domain means;
- RI_5050 and RI_6040 composites;
- baseline-relative non-negative deficit;
- trapezoidal deficit area using actual day offsets;
- ±0.3 z recovery criterion;
- single internal missing-touchpoint interpolation.

### Reference safety

Reference parameters are passed explicitly and must be marked verified=True. Unverified candidate references raise ReferenceParameterNotVerified rather than silently entering the score.

No candidate reference value is hard-coded in the engine.

### Scope

This is research software. It does not establish clinical validity, diagnostic utility, or treatment recommendations.