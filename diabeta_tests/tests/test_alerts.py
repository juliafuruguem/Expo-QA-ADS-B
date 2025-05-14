from alerts import check_glucose_alert

def test_low_glucose():
    assert check_glucose_alert(50, 70, 180) == "Glicose baixa"

def test_high_glucose():
    assert check_glucose_alert(200, 70, 180) == "Glicose alta"

def test_normal_glucose():
    assert check_glucose_alert(100, 70, 180) == "Glicose dentro do normal"