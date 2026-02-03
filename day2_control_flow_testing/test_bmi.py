import pytest
from bmi import bmi_calculator


def test_valid_bmi_float_inputs():
    assert bmi_calculator(1.80, 75) == 23.15
    assert bmi_calculator(1.60, 50) == 19.53


def test_valid_bmi_int_inputs():
    assert bmi_calculator(2, 80) == 20.0


def test_invalid_height_value():
    with pytest.raises(ValueError):
        bmi_calculator(0, 70)


def test_invalid_weight_value():
    with pytest.raises(ValueError):
        bmi_calculator(1.7, -1)


def test_invalid_height_type():
    with pytest.raises(TypeError):
        bmi_calculator("1.8", 70)


def test_invalid_weight_type():
    with pytest.raises(TypeError):
        bmi_calculator(1.7, None)


def test_bool_inputs_rejected():
    with pytest.raises(TypeError):
        bmi_calculator(True, 70)

    with pytest.raises(TypeError):
        bmi_calculator(1.7, False)
