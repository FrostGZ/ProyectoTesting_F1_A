# Importación de clases del sistema a probar
from app.paciente import Paciente
from app.consulta import Consulta
from app.doctor import Doctor
from app.recurso import Recurso
from app.asignador import asignar_cita

# Verifica que una cita básica sin equipo se asigne correctamente
def test_asignacion_simple():
    paciente = Paciente("Carlos", 30, nivel_urgencia=3)
    consulta = Consulta("revisión", 30)
    doctor = Doctor("Dra. Ana", "General", ["10:00", "10:30"])
    resultado = asignar_cita(paciente, consulta, [doctor], {}, "10:00")
    assert "Dra. Ana" in resultado  # La cita debe ser asignada a Dra. Ana

# Verifica que la asignación funcione correctamente si se requiere un equipo médico
def test_asignacion_con_equipo():
    paciente = Paciente("Laura", 45, 4)
    consulta = Consulta("ecografía", 30, requiere_equipo="ecógrafo")
    doctor = Doctor("Dr. Luis", "Diagnóstico", ["10:00"])
    ecografo = Recurso("ecógrafo", ["10:00", "10:30"])
    resultado = asignar_cita(paciente, consulta, [doctor], {"ecógrafo": ecografo}, "10:00")
    assert "ecógrafo" in resultado  # Debe incluir el nombre del equipo en el resultado

# Verifica que el sistema no permita asignar una cita si el doctor ya está ocupado
def test_asignacion_sin_disponibilidad():
    paciente = Paciente("Carlos", 30)
    consulta = Consulta("revisión", 30)
    doctor = Doctor("Dra. Ana", "General", ["10:00"])
    doctor.agenda["10:00"] = "Ocupado"  # Simula que el doctor ya tiene una cita
    resultado = asignar_cita(paciente, consulta, [doctor], {}, "10:00")
    assert resultado == "No hay disponibilidad"

# Verifica que si el equipo requerido está ocupado, la cita no se asigne
def test_asignacion_equipo_ocupado():
    paciente = Paciente("Lucía", 40)
    consulta = Consulta("ecografía", 30, requiere_equipo="ecógrafo")
    doctor = Doctor("Dr. Luis", "Diagnóstico", ["10:00"])
    ecografo = Recurso("ecógrafo", ["10:00"])
    ecografo.ocupado.add("10:00")  # Marca el equipo como ya ocupado
    resultado = asignar_cita(paciente, consulta, [doctor], {"ecógrafo": ecografo}, "10:00")
    assert resultado == "No hay disponibilidad"

# Verifica que si hay varios doctores disponibles, se priorice alfabéticamente
def test_asignacion_multiples_doctores_con_prioridad():
    paciente = Paciente("Raúl", 32)
    consulta = Consulta("revisión", 30)
    doctor1 = Doctor("Zeta", "General", ["10:00"])
    doctor2 = Doctor("Alfa", "General", ["10:00"])
    resultado = asignar_cita(paciente, consulta, [doctor1, doctor2], {}, "10:00")
    assert "Alfa" in resultado  # El sistema debe asignar a "Alfa" por orden alfabético

# Verifica que se asigne correctamente una cita cuando el paciente no tiene urgencia
def test_asignacion_paciente_sin_urgencia():
    paciente = Paciente("Mario", 25, nivel_urgencia=1)
    consulta = Consulta("control", 20)
    doctor = Doctor("Dra. Vega", "Clínica", ["11:00"])
    resultado = asignar_cita(paciente, consulta, [doctor], {}, "11:00")
    assert "Dra. Vega" in resultado

# Verifica que si el equipo requerido no está en la lista de recursos, no se asigne cita
def test_equipo_requerido_no_existe_en_recursos():
    paciente = Paciente("Andrea", 34, 3)
    consulta = Consulta("resonancia", 45, requiere_equipo="resonador")
    doctor = Doctor("Dr. Salas", "Imagenología", ["10:00"])
    resultado = asignar_cita(paciente, consulta, [doctor], {}, "10:00")
    assert resultado == "No hay disponibilidad"

# Verifica que si el doctor no tiene disponibilidad en la hora solicitada, no se asigne cita
def test_asignacion_en_hora_no_disponible():
    paciente = Paciente("Luis", 29)
    consulta = Consulta("revisión", 30)
    doctor = Doctor("Dr. Osorio", "General", ["09:00"])  # No tiene "10:00"
    resultado = asignar_cita(paciente, consulta, [doctor], {}, "10:00")
    assert resultado == "No hay disponibilidad"