# Clase que representa a un paciente que solicita una cita médica
class Paciente:
    def __init__(self, nombre, edad, nivel_urgencia=1, comorbilidades=None):
        # Nombre del paciente (ej. "Elena", "Carlos")
        self.nombre = nombre

        # Edad del paciente
        self.edad = edad

        # Nivel de urgencia médica (por defecto es 1 si no se especifica)
        # Este valor puede utilizarse para priorizar citas (escala sugerida del 1 al 5)
        self.nivel_urgencia = nivel_urgencia

        # Lista de comorbilidades (enfermedades adicionales del paciente)
        # Si no se proporcionan, se inicializa como lista vacía
        self.comorbilidades = comorbilidades or []