import pytest
from user_profile import (
    calculate_average_glucose,
    is_valid_meal,
    is_glucose_alert,
    register_glucose_entry,
    generate_report
)

def test_average_glucose_normal():
    readings = [100, 110, 90, 105]
    assert calculate_average_glucose(readings) == 101.25

def test_average_glucose_empty_list():
    with pytest.raises(ValueError):
        calculate_average_glucose([])

def test_average_glucose_invalid_values():
    with pytest.raises(ValueError):
        calculate_average_glucose([100, 'a', 95])

def test_valid_meal():
    meal = {"name": "Arroz", "date": "2025-05-14", "time": "12:00"}
    assert is_valid_meal(meal) is True

def test_invalid_meal_name():
    meal = {"name": "Arroz123", "date": "2025-05-14", "time": "12:00"}
    assert is_valid_meal(meal) is False

def test_invalid_meal_fields():
    meal = {"name": "", "date": 20250514, "time": None}
    assert is_valid_meal(meal) is False

def test_glucose_alert_trigger():
    assert is_glucose_alert(60) is True
    assert is_glucose_alert(200) is True
    assert is_glucose_alert(100) is False

def test_custom_alert_range():
    assert is_glucose_alert(150, max_val=140) is True

def test_register_glucose_entry():
    entries = {}
    new_entry = {"date": "2025-05-14", "time": "08:00", "value": 110}
    updated = register_glucose_entry(entries, new_entry)
    assert updated[("2025-05-14", "08:00")] == 110

def test_register_duplicate_entry():
    entries = {("2025-05-14", "08:00"): 110}
    new_entry = {"date": "2025-05-14", "time": "08:00", "value": 120}
    with pytest.raises(ValueError):
        register_glucose_entry(entries, new_entry)

def test_generate_report_with_data():
    entries = {("2025-05-14", "08:00"): 110, ("2025-05-14", "12:00"): 100}
    assert generate_report(entries) == "Relatório gerado com 2 registros."

def test_generate_report_empty():
    assert generate_report({}) == "Nenhum dado disponível para gerar relatório."
