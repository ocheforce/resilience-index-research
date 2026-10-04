"""Deterministic Resilience Index scoring primitives.

This module implements the frozen pilot scoring rules. It is research
software, not a clinical decision tool. Reference parameters must be
explicitly marked verified before they can be used.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import log
from typing import Mapping, Sequence


class ReferenceParameterNotVerified(ValueError):
    """Raised when a reference parameter is not explicitly verified."""


@dataclass(frozen=True)
class ReferenceParameter:
    mean: float
    sd: float
    verified: bool = False

    def validate(self) -> None:
        if not self.verified:
            raise ReferenceParameterNotVerified(
                "Reference parameter is not verified for production scoring."
            )
        if self.sd <= 0:
            raise ValueError("Reference SD must be > 0.")


def z_score(value: float, reference: ReferenceParameter) -> float:
    reference.validate()
    return (value - reference.mean) / reference.sd


def crp_transformed_z(crp_mg_l: float, reference: ReferenceParameter) -> float:
    """Calculate the prespecified z-score on ln(CRP + 1)."""
    if crp_mg_l < 0:
        raise ValueError("CRP cannot be negative.")
    return z_score(log(crp_mg_l + 1.0), reference)


def direction_correct(z: float, higher_is_worse: bool) -> float:
    return -z if higher_is_worse else z


def mean_required(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("At least one value is required.")
    return sum(values) / len(values)


def domain_scores(
    clinical_z: Mapping[str, float],
    cognitive_z: Mapping[str, float],
) -> tuple[float, float]:
    """Return Clinical_z and Cognitive_z as simple means."""
    return mean_required(list(clinical_z.values())), mean_required(list(cognitive_z.values()))


def composite_scores(clinical_z: float, cognitive_z: float) -> tuple[float, float]:
    """Return RI_5050 and RI_6040."""
    ri_5050 = 0.5 * clinical_z + 0.5 * cognitive_z
    ri_6040 = 0.6 * clinical_z + 0.4 * cognitive_z
    return ri_5050, ri_6040


def deficit(baseline_ri: float, current_ri: float) -> float:
    """Prespecified non-negative resilience deficit."""
    return max(0.0, baseline_ri - current_ri)


def trapezoidal_area(days: Sequence[float], values: Sequence[float]) -> float:
    """Integrate a trajectory using actual day offsets."""
    if len(days) != len(values) or len(days) < 2:
        raise ValueError("days and values need equal length >= 2.")
    if any(b <= a for a, b in zip(days, days[1:])):
        raise ValueError("days must be strictly increasing.")
    return sum(
        0.5 * (v0 + v1) * (t1 - t0)
        for t0, t1, v0, v1 in zip(days, days[1:], values, values[1:])
    )


def recovery_within_tolerance(current_ri: float, baseline_ri: float, tolerance: float = 0.3) -> bool:
    """Whether the current RI is within ±tolerance z units of baseline."""
    if tolerance < 0:
        raise ValueError("tolerance must be non-negative.")
    return abs(current_ri - baseline_ri) <= tolerance


def interpolate_internal_missing(days: Sequence[float], values: Sequence[float | None]) -> list[float]:
    """Linearly interpolate exactly one internal missing value.

    Edge missingness is intentionally not imputed here; the SAP specifies
    that it should be flagged and handled with available-timepoint area.
    """
    missing = [i for i, value in enumerate(values) if value is None]
    if len(missing) != 1:
        raise ValueError("Exactly one missing value is required.")
    i = missing[0]
    if i == 0 or i == len(values) - 1:
        raise ValueError("Missing value is not internal.")
    left, right = values[i - 1], values[i + 1]
    assert left is not None and right is not None
    fraction = (days[i] - days[i - 1]) / (days[i + 1] - days[i - 1])
    result = list(values)
    result[i] = left + fraction * (right - left)
    return [float(x) for x in result]
