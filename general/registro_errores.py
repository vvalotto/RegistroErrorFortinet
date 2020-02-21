"""
funciones tratan y registran los errores enviados
"""
import csv

"""

"""
class RegistroErrores:

    @property
    def path_registro(self):
        return self._path_registro

    @property
    def nombre_archivo(self):
        return self._nombre_archivo

    @nombre_archivo.setter
    def nombre_archivo(self, valor):
        self._nombre_archivo = valor
        return

    def __init__(self, path_registro):
        self._path_registro = path_registro
        self._nombre_archivo = None

    def inicializar_registro(self, fecha):
        self._nombre_archivo = "registro.csv"
        try:
            registro_datos = open(self._nombre_archivo, 'a' , newline='', encoding='utf-8')

        except IOError:
            print("Error en la escritura del log")
            raise Exception ("Error al abrir el archivo")
        return

    def registrar_en_archivos(self, errores):
        try:
            registro_datos = open(self._nombre_archivo, 'a' , newline='', encoding='utf-8')

            with registro_datos:
                campos = ["fecha", 'url', "clientIP", "serverIP", "userName", "groupName"]
                writer = csv.DictWriter(registro_datos, fieldnames=campos)
                writer.writerow(errores)
        except Exception as e:
            msg = str(e)
            print("Error en la escritura del log")
            raise Exception("Error al escribir el archivo")
        return
