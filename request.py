import requests

link_api = "http://127.0.0.1:5005/api/analizar_datos/"

lista = input("favor agregar los valores: ").split(",")
lista2 = [float(i) for i in lista]

datos = {"datos" : lista2}

respuesta = requests.post(link_api, json=datos)
print(respuesta.json())