from app.doctor import Doctor
from app.reagendador import reagendar

# Verifica que una cita se pueda reagendar correctamente de un doctor a otro
def test_reagendamiento_simple():
    doctor1 = Doctor("Dr. González", "General", ["09:00"])
    doctor2 = Doctor("Dra. López", "General", ["09:00"])
    doctor1.agenda["09:00"] = "Carlos"

    reubicadas = reagendar(doctor1, [doctor2], ["Carlos"])
    assert len(reubicadas) == 1
    assert doctor1.agenda == {}  # La cita debe haber sido removida
    assert doctor2.agenda["09:00"] == "Carlos"

# Verifica que si no hay reemplazo disponible, la cita no se reasigne
def test_reagendamiento_sin_reemplazo():
    doctor1 = Doctor("Dr. Macedo", "Pediatría", ["09:00"])
    doctor2 = Doctor("Dr. Rivero", "Pediatría", ["09:00"])
    doctor2.agenda["09:00"] = "Juan"
    doctor1.agenda["09:00"] = "Carlos"
    
    reubicadas = reagendar(doctor1, [doctor2], ["Carlos"])
    assert reubicadas == []
    assert doctor1.agenda == {}  # Igual se borra la agenda del doctor afectado

# Verifica que varias citas puedan ser reagendadas correctamente
def test_reagendamiento_varias_citas():
    doctor1 = Doctor("Dr. García", "Cardio", ["09:00", "10:00"])
    doctor2 = Doctor("Dra. Montoya", "Cardio", ["09:00", "10:00"])
    doctor1.agenda["09:00"] = "Laura"
    doctor1.agenda["10:00"] = "José"
    
    resultado = reagendar(doctor1, [doctor2], ["Laura", "José"])
    assert len(resultado) == 2
    assert "Laura" in doctor2.agenda.values()
    assert "José" in doctor2.agenda.values()

# Verifica que una cita pueda ser reagendada a cualquiera de varios doctores disponibles
def test_reagendamiento_varias_opciones():
    doc1 = Doctor("Dr. Martínez", "Neurología", ["08:00"])
    doc2 = Doctor("Dra. Silva", "Neurología", ["08:00"])
    doc3 = Doctor("Dr. Foreman", "Neurología", ["08:00"])
    doc1.agenda["08:00"] = "Marta"
    resultado = reagendar(doc1, [doc2, doc3], ["Marta"])
    assert len(resultado) == 1
    assert resultado[0][1] in ["Dra. Silva", "Dr. Foreman"]  # A cualquiera de los dos

# Verifica que si no hay horas libres, la cita no se reasigna
def test_reagendamiento_sin_ninguna_hora_libre():
    doc1 = Doctor("Dr. Sánchez", "Trauma", ["08:00"])
    doc2 = Doctor("Dra. Cuddy", "Trauma", ["08:00"])
    doc2.agenda["08:00"] = "Lisa"
    doc1.agenda["08:00"] = "Eric"
    resultado = reagendar(doc1, [doc2], ["Eric"])
    assert resultado == []
    assert doc1.agenda == {}  # Agenda limpiada, sin cita reasignada