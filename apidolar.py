import requests
import json

class Dolar(object):
    __valor = float

    def __init__(self):
        r = json.loads(requests.get("https://www.dolarsi.com/api/api.php?type=dolar").content)
        i=0
        while i<len(r) and not ("casa" in r[i] and r[i]["casa"]["nombre"]=="Oficial"):
            i+=1
        if i<len(r):
            self.__valor= float(r[i]["casa"]["venta"].replace(",", "."))
        else:
            self.__valor = -1
    def obtener(self):
        return self.__valor