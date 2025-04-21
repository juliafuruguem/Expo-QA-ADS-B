def calculate_average_glucose(glucose_readings):

    if not glucose_readings:
        raise ValueError("A lista de leituras não pode estar vazia.")
    
    if not all(isinstance(g, (int, float)) for g in glucose_readings):
        raise ValueError("Todos os valores devem ser números.")
    
    return sum(glucose_readings) / len(glucose_readings)
