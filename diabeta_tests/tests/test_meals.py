import pytest
from meals import register_meal

def test_valid_meal():
    result = register_meal("Arroz", "12:00", "2025-05-10")
    assert result["alimento"] == "Arroz"

def test_invalid_meal_name():
    with pytest.raises(ValueError):
        register_meal("123", "12:00", "2025-05-10")

def test_missing_fields():
    with pytest.raises(ValueError):
        register_meal("Feijão", "", "")