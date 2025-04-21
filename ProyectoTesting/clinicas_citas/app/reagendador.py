# Función que intenta reasignar las citas de un doctor que ya no está disponible
def reagendar(doctor_afectado, doctores, pacientes_urgentes):
    # Obtiene todas las citas asignadas al doctor afectado (hora y nombre del paciente)
    citas_afectadas = list(doctor_afectado.agenda.items())

    # Lista para registrar las citas que se logren reubicar
    reubicadas = []

    # Itera por cada cita afectada
    for hora, paciente_nombre in citas_afectadas:
        # Busca otro doctor disponible a la misma hora
        for doc in doctores:
            if doc != doctor_afectado and doc.esta_disponible(hora):
                # Reasigna la cita al nuevo doctor
                doc.agenda[hora] = paciente_nombre
                # Registra la reubicación (nombre, nuevo doctor, hora)
                reubicadas.append((paciente_nombre, doc.nombre, hora))
                break  # Pasa a la siguiente cita después de reasignar

    # Limpia completamente la agenda del doctor afectado
    doctor_afectado.agenda.clear()

    # Devuelve la lista de citas reubicadas
    return reubicadas