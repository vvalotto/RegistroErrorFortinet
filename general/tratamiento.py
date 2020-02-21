import json, datetime
from general.registro_errores import *


def tratar_errores(registro_errores, errores):
    for k, v in errores.items():
        print("%s -> %s" %(k,v))
    registro_errores.registrar_en_archivos(errores)
    return


def leer_json():
    with open('errores.json') as archivo_json:
        datos_error = json.load(archivo_json)
    return datos_error


if __name__ == "__main__":
    registro = RegistroErrores("w:\\DESARROLLO\\Proyectos\\errores_")
    registro.inicializar_registro(datetime.datetime.now().strftime('%d-%m-%Y'))
    datos = leer_json()
    datos["fecha"] = datetime.datetime.now().strftime('%d-%m-%Y')
    tratar_errores(registro, datos)
