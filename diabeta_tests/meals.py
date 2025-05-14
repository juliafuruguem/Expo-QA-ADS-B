def register_meal(name, time, date):
    if not name or not isinstance(name, str) or name.isdigit():
        raise ValueError("Nome do alimento inválido.")
    if not time or not date:
        raise ValueError("Horário e data são obrigatórios.")
    return {"alimento": name, "horário": time, "data": date}