def register_glucose_entry(entries, new_entry):
    if new_entry in entries:
        raise ValueError("Entrada duplicada.")
    entries.append(new_entry)
    return entries