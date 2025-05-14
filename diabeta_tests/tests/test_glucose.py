import pytest
from glucose import calculate_average_glucose

def test_average_glucose_normal():
    assert calculate_average_glucose([100, 110, 90]) == 100.0

def test_average_glucose_empty_list():
    with pytest.raises(ValueError):
        calculate_average_glucose([])

def test_average_glucose_invalid_values():
    with pytest.raises(ValueError):
        calculate_average_glucose([100, "a", 95])