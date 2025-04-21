from app.doctor import Doctor

# Verifica que el método esta_disponible funcione correctamente con horas disponibles y no disponibles
def test_doctor_disponibilidad():
    doctor = Doctor("Dra. Pérez", "Cardiología", ["08:00", "09:00"])
    
    # La doctora tiene disponibilidad a las 08:00
    assert doctor.esta_disponible("08:00")
    
    # No tiene disponibilidad a las 10:00, debe retornar False
    assert not doctor.esta_disponible("10:00")

# Verifica que un horario ya ocupado aparezca como no disponible
def test_doctor_agenda():
    doctor = Doctor("Dr. Miota", "Dermatología", ["10:00"])
    
    # Se asigna una cita en la única hora disponible
    doctor.agenda["10:00"] = "Sarah"
    
    # Ya no debería estar disponible a las 10:00
    assert not doctor.esta_disponible("10:00")

# Verifica que el método esta_disponible detecte múltiples horarios ocupados
def test_doctor_agenda_multiple():
    doctor = Doctor("Dr. Bravo", "Gastro", ["09:00", "10:00"])
    
    # Se asignan citas en ambos horarios
    doctor.agenda["09:00"] = "Pedro"
    doctor.agenda["10:00"] = "Sofía"
    
    # Ambas horas ya no están disponibles
    assert not doctor.esta_disponible("09:00")
    assert not doctor.esta_disponible("10:00")