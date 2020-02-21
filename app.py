"""
lanzador de la aplicacion, punto de entrada
"""
from servicios.api import *

if __name__ == "__main__":
    """
    Aplicacion de servicios corre en el servidor definido (sin direccion IP especifica)
    """
    app_api.run(host='0.0.0.0', port=7000, debug=True, ssl_context=("2018-11_energiaer.com.ar.crt", "www.energiaer.com.ar.key"))
