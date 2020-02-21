from .registro_errores import *
import datetime, os

class Configurador:

    registro = RegistroErrores("/archivo")
    registro.inicializar_registro(datetime.datetime.now().strftime('%d-%m-%Y'))