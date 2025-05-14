def generate_report(data):
    if not data:
        return "Nenhum dado disponível para relatório."
    return f"Relatório gerado com {len(data)} entradas."