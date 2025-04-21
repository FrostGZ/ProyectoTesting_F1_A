# Clase que representa un recurso médico compartido, como un ecógrafo o resonador
class Recurso:
    def __init__(self, nombre, disponibilidad):
        # Nombre del recurso (ej. "ecógrafo", "resonador")
        self.nombre = nombre

        # Lista de horas en las que el recurso está disponible
        self.disponibilidad = disponibilidad

        # Conjunto de horas en las que el recurso ya está ocupado
        self.ocupado = set()

    # Método que verifica si el recurso está disponible en una hora específica
    def esta_disponible(self, hora):
        # El recurso está disponible si la hora está en la lista de disponibilidad
        # y no se encuentra en el conjunto de horas ocupadas
        return hora in self.disponibilidad and hora not in self.ocupado