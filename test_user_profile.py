import pytest
from user_profile import calculate_average_glucose

def test_average_glucose_normal():
    readings = [100, 110, 90, 105]
    assert calculate_average_glucose(readings) == 101.25

def test_average_glucose_empty_list():
    with pytest.raises(ValueError):
        calculate_average_glucose([])

def test_average_glucose_invalid_values():
    readings = [100, 'a', 95]
    with pytest.raises(ValueError):
        calculate_average_glucose(readings)
