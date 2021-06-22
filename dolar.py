import requests
import json

class Dolar(object):
    __dolares = list
    def __init__(self):
        self.__dolares = []
    def actualizar(self): # Obtiene de la pagina las cotizaciones del dolar
        self.__dolares = []
        r = json.loads(requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales").content)
        for elemento in r:
            if "dolar" in elemento["casa"]["nombre"].lower() and elemento["casa"]["venta"] != "0" and elemento["casa"]["compra"].lower()!="no cotiza":
                d = { "compra": elemento["casa"]["compra"], "venta": elemento["casa"]["venta"], "nombre": elemento["casa"]["nombre"]}
                self.__dolares.append(d)
        return self.__dolares
    def obtener(self):
        return self.__dolares