from app.paciente import Paciente

# Verifica que se cree un paciente con valores por defecto correctamente
def test_paciente_basico():
    paciente = Paciente("Elena", 28)
    assert paciente.nombre == "Elena"  # Nombre asignado correctamente
    assert paciente.edad == 28         # Edad asignada correctamente
    assert paciente.nivel_urgencia == 1  # Urgencia por defecto
    assert paciente.comorbilidades == []  # Lista vacía por defecto

# Verifica que se asignen comorbilidades correctamente al paciente
def test_paciente_con_comorbilidades():
    paciente = Paciente("José", 65, nivel_urgencia=4, comorbilidades=["diabetes", "asma"])
    assert "diabetes" in paciente.comorbilidades
    assert paciente.nivel_urgencia == 4

# Verifica que se asignen niveles de urgencia altos correctamente
def test_paciente_urgencia_maxima():
    paciente = Paciente("Nicolle", 57, nivel_urgencia=5)
    assert paciente.nivel_urgencia == 5

# Verifica que el paciente pueda tener múltiples comorbilidades
def test_paciente_con_muchas_comorbilidades():
    comorbilidades = ["asma", "diabetes", "hipertensión", "artritis"]
    paciente = Paciente("Roberto", 63, 3, comorbilidades)
    assert len(paciente.comorbilidades) == 4
    assert "asma" in paciente.comorbilidades