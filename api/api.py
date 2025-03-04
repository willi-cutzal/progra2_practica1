from flask import Flask, jsonify, request
from funcion import analizar_datos

app = Flask(__name__)




@app.route('/',methods=['GET'])
def saludo():
    """
    saludo de bienvenida al ingresar a la dirección que nos da la API
    """
    return jsonify({"mensaje":"Hola, esta es mi primera API en progra2 :) "})



@app.route('/api/analizar_datos/',methods=['POST'])
def api_analizar_datos():
    """
    ingreso de datos
    
    parámetros: lista de números
    return: promedio y desviación estándar de la lista ingresada
    """
    datos = request.json.get("datos", [])
    resultado = analizar_datos(datos) #aquí estoy llamando a mi función
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True, port=5005)