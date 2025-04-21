import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template_string
from clinicas_citas.app.paciente import Paciente
from clinicas_citas.app.consulta import Consulta
from clinicas_citas.app.doctor import Doctor
from clinicas_citas.app.recurso import Recurso
from clinicas_citas.app.asignador import asignar_cita

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Gestión de Citas</title>
<h2>Solicitar Cita Médica</h2>
<form method=post>
  Nombre del paciente: <input type=text name=nombre><br>
  Edad: <input type=number name=edad><br>
  Consulta: <select name=tipo>
    <option value="revisión">Revisión</option>
    <option value="ecografía">Ecografía</option>
  </select><br>
  Hora: <input type=text name=hora placeholder="08:00"><br>
  <input type=submit value=Solicitar>
</form>
<p>{{ resultado }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def solicitar_cita():
    resultado = ""
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tipo = request.form["tipo"]
        hora = request.form["hora"]

        paciente = Paciente(nombre, edad)
        consulta = Consulta(tipo, 30, "ecógrafo" if tipo == "ecografía" else None)
        doctor = Doctor("Dra. Cuddy", "General", [hora])
        recurso = Recurso("ecógrafo", [hora])
        recursos = {"ecógrafo": recurso} if consulta.requiere_equipo else {}

        resultado = asignar_cita(paciente, consulta, [doctor], recursos, hora)
    return render_template_string(TEMPLATE, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)