import math
import pytest

from resilience_index.scoring import (
    ReferenceParameter,
    ReferenceParameterNotVerified,
    composite_scores,
    crp_transformed_z,
    deficit,
    direction_correct,
    interpolate_internal_missing,
    recovery_within_tolerance,
    trapezoidal_area,
)


def test_unverified_reference_is_blocked():
    with pytest.raises(ReferenceParameterNotVerified):
        crp_transformed_z(1.0, ReferenceParameter(0.5, 0.2))


def test_crp_transformation():
    ref = ReferenceParameter(math.log(2.0), 0.5, verified=True)
    assert crp_transformed_z(1.0, ref) == pytest.approx(0.0)


def test_direction_correction():
    assert direction_correct(1.2, True) == pytest.approx(-1.2)
    assert direction_correct(1.2, False) == pytest.approx(1.2)


def test_composites():
    assert composite_scores(1.0, 0.0) == pytest.approx((0.5, 0.6))


def test_deficit_has_zero_floor():
    assert deficit(0.2, 0.8) == 0.0
    assert deficit(0.8, 0.2) == pytest.approx(0.6)


def test_trapezoidal_area_uses_actual_days():
    assert trapezoidal_area([0, 1, 3], [0, 2, 0]) == pytest.approx(4.0)


def test_internal_missing_interpolation():
    assert interpolate_internal_missing([0, 2, 5], [0.0, None, 5.0]) == pytest.approx([0, 2, 5])


def test_edge_missing_is_not_imputed():
    with pytest.raises(ValueError):
        interpolate_internal_missing([0, 2, 5], [None, 2.0, 5.0])


def test_recovery_tolerance():
    assert recovery_within_tolerance(1.1, 1.0)
    assert not recovery_within_tolerance(1.31, 1.0)
