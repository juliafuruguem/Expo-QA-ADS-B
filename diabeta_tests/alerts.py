def check_glucose_alert(glucose_value, min_limit, max_limit):
    if glucose_value < min_limit:
        return "Glicose baixa"
    elif glucose_value > max_limit:
        return "Glicose alta"
    else:
        return "Glicose dentro do normal"