import requests
"""
consultor de datos estadísticos

recibe una lista de números por parte del usuario y hará la consulta a la API

"""

link_api = "http://127.0.0.1:5005/api/analizar_datos/"

lista = input("favor agregar los valores (en numeros) separados por una coma: ").split(",")
lista2 = [float(i) for i in lista]

datos = {"datos" : lista2}

respuesta = requests.post(link_api, json=datos)
print(respuesta.json())