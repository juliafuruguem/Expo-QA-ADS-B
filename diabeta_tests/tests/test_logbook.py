import pytest
from logbook import register_glucose_entry

def test_register_entry():
    entries = []
    new_entry = {"data": "2025-05-14", "hora": "10:00", "valor": 110}
    updated_entries = register_glucose_entry(entries, new_entry)
    assert new_entry in updated_entries

def test_duplicate_entry():
    entries = [{"data": "2025-05-14", "hora": "10:00", "valor": 110}]
    with pytest.raises(ValueError):
        register_glucose_entry(entries, {"data": "2025-05-14", "hora": "10:00", "valor": 110})