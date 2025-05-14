from reports import generate_report

def test_generate_report_with_data():
    result = generate_report([1, 2, 3])
    assert "3 entradas" in result

def test_generate_report_no_data():
    result = generate_report([])
    assert result == "Nenhum dado disponível para relatório."