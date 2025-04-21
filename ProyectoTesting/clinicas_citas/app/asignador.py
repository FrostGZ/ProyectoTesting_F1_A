def asignar_cita(paciente, consulta, doctores, recursos, hora_preferencia):
    # Itera sobre la lista de doctores, ordenados alfabéticamente por nombre
    for doctor in sorted(doctores, key=lambda d: d.nombre):

        # Verifica si el doctor está disponible a la hora solicitada
        if doctor.esta_disponible(hora_preferencia):

            # Si la consulta requiere el uso de un equipo médico
            if consulta.requiere_equipo:
                # Se obtiene el equipo necesario desde el diccionario de recursos
                equipo = recursos.get(consulta.requiere_equipo)

                # Se verifica si el equipo existe y está disponible en la hora solicitada
                if equipo and equipo.esta_disponible(hora_preferencia):
                    # Se asigna al doctor la cita con el nombre del paciente en su agenda
                    doctor.agenda[hora_preferencia] = paciente.nombre
                    # Se marca el equipo como ocupado en la hora indicada
                    equipo.ocupado.add(hora_preferencia)
                    # Se retorna un mensaje indicando que la cita fue asignada con el equipo
                    return f"Cita asignada con {doctor.nombre} a las {hora_preferencia} usando {equipo.nombre}"
            else:
                # Si no se requiere equipo, se asigna la cita directamente
                doctor.agenda[hora_preferencia] = paciente.nombre
                # Se retorna un mensaje indicando que la cita fue asignada sin equipo
                return f"Cita asignada con {doctor.nombre} a las {hora_preferencia}"

    # Si ningún doctor y/o recurso estuvo disponible, se retorna un mensaje de no disponibilidad
    return "No hay disponibilidad"