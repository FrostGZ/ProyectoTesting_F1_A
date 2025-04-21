from app.paciente import Paciente
from app.consulta import Consulta
from app.doctor import Doctor
from app.recurso import Recurso
from app.asignador import asignar_cita

# Verifica que todo el flujo de asignación funcione correctamente integrando varias clases
def test_flujo_asignacion_completo():
    # Se crea un paciente con datos básicos
    paciente = Paciente("Florencia", 35)
    
    # Se crea una consulta que requiere un equipo médico (ecógrafo)
    consulta = Consulta("ecografía", 30, requiere_equipo="ecógrafo")
    
    # Se crea un doctor con disponibilidad en la hora requerida
    doctor = Doctor("Dr. Vera", "Radiología", ["09:00"])
    
    # Se crea el recurso requerido (ecógrafo), también disponible a esa hora
    recurso = Recurso("ecógrafo", ["09:00"])

    # Se intenta asignar la cita integrando paciente, consulta, doctor y recurso
    resultado = asignar_cita(paciente, consulta, [doctor], {"ecógrafo": recurso}, "09:00")

    # Verifica que el mensaje de confirmación sea correcto
    assert resultado == "Cita asignada con Dr. Vera a las 09:00 usando ecógrafo"
    
    # Verifica que el doctor tenga la cita registrada en su agenda
    assert doctor.agenda["09:00"] == "Florencia"
    
    # Verifica que el recurso esté marcado como ocupado en esa hora
    assert "09:00" in recurso.ocupado