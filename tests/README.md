# Tests

Automated tests verify deterministic scientific transformations before analysis.

Current v0.1 coverage:

- blocking of unverified reference parameters;
- CRP transformation;
- z-score direction correction;
- RI_5050 and RI_6040;
- deficit floor at zero;
- trapezoidal area with unequal intervals;
- single internal missing-touchpoint interpolation;
- edge-missingness protection;
- recovery tolerance.

Tests use synthetic values only. They do not constitute validation of the Resilience Index in human participants.