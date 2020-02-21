"""
Servicios de aplicacion - APIs
"""

from flask import Flask, make_response, request, jsonify, send_file
from flask_cors import CORS
from general.tratamiento import *
from general.configurador import *


# Instancia la aplicacion de servicios Flask
app_api = Flask(__name__)
CORS(app_api)

""" API de Errores """
@app_api.errorhandler(404)
def not_fount(error):
    return make_response(jsonify({'error': 'No Encontrado'}), 404)

@app_api.errorhandler(500)
def not_fount(error):
    return make_response(jsonify({'error': error}), 500)

""" API de servicios"""

"""
Peticion para registrar los datos de la pagina de error
desde el cliente
"""
@app_api.route("/datos_error/", methods=["POST"])
def datos_error():

    try:
        datos = request.get_json()
        """
        Agrega la momento del evento al diccionario de datos
        """
        datos["fecha"] = datetime.datetime.now().strftime('%d-%m-%Y:%H:%M:%S')
        """
        Llama a la función interna que tratará los datos
        """
        tratar_errores(Configurador.registro, datos)
    except:
        return not_fount("Error al escribir en el archivo")

    return "Datos Registrado", 201


"""
API de comprobación de servidor respondiendo
"""
@app_api.route("/comprueba/", methods=["GET"])
def comprueba():
    return "OK!", 200


"""
API para recuperar el archivo de datos registrados
"""
@app_api.route("/archivo_errores/", methods=["GET"])
def archivo_errores():

    try:
        return send_file(Configurador.registro.nombre_archivo, as_attachment=True)
    except FileNotFoundError:
        return not_fount("archivo no encontrado")
