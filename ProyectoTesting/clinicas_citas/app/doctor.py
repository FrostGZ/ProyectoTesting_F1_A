# Clase que representa a un doctor del sistema de citas médicas
class Doctor:
    def __init__(self, nombre, especialidad, disponibilidad):
        # Nombre del doctor (ej. "Dr. Pérez")
        self.nombre = nombre

        # Especialidad médica del doctor (ej. "Cardiología", "Pediatría")
        self.especialidad = especialidad

        # Lista de horas en las que el doctor está disponible (ej. ["08:00", "09:00"])
        self.disponibilidad = disponibilidad

        # Diccionario que representa la agenda del doctor, con horas como claves
        # y nombres de pacientes como valores (ej. {"08:00": "Carlos"})
        self.agenda = {}

    # Método que verifica si el doctor está disponible en una hora específica
    def esta_disponible(self, hora):
        # Retorna True si la hora está en la disponibilidad y no está ya ocupada en la agenda
        return hora in self.disponibilidad and hora not in self.agenda