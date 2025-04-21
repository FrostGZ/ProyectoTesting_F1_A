# Clase que representa una consulta médica solicitada por un paciente
class Consulta:
    def __init__(self, tipo, duracion_min, requiere_equipo=None):
        # Tipo de consulta (por ejemplo: "revisión", "ecografía", etc.)
        self.tipo = tipo

        # Duración de la consulta en minutos
        self.duracion = duracion_min

        # Nombre del equipo médico requerido, si aplica (por ejemplo: "ecógrafo")
        # Si no se necesita equipo, se deja como None
        self.requiere_equipo = requiere_equipo