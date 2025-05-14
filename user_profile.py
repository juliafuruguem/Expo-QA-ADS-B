from datetime import datetime

def calculate_average_glucose(glucose_readings):
    if not glucose_readings:
        raise ValueError("A lista de leituras não pode estar vazia.")
    if not all(isinstance(g, (int, float)) for g in glucose_readings):
        raise ValueError("Todos os valores devem ser números.")
    return sum(glucose_readings) / len(glucose_readings)

def is_valid_meal(meal):
    return all([
        isinstance(meal.get("name"), str) and meal["name"].isalpha(),
        isinstance(meal.get("date"), str),
        isinstance(meal.get("time"), str)
    ])

def is_glucose_alert(glucose, min_val=70, max_val=180):
    return glucose < min_val or glucose > max_val

def register_glucose_entry(entries, new_entry):
    key = (new_entry['date'], new_entry['time'])
    if key in entries:
        raise ValueError("Entrada duplicada de glicemia.")
    entries[key] = new_entry['value']
    return entries

def generate_report(entries):
    if not entries:
        return "Nenhum dado disponível para gerar relatório."
    return f"Relatório gerado com {len(entries)} registros."
