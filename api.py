from flask import Flask, jsonify, request
from funcion import analizar_datos

app = Flask(__name__)

@app.route('/api/saludo/',methods=['GET'])
def saludo():
    return jsonify({"mensaje":"Hola esta es una api en flask :) "})



@app.route('/api/analizar_datos/',methods=['POST'])
def api_analizar_datos():
    datos = request.json.get("datos", [])
    resultado = analizar_datos(datos) #aquí estoy llamando a mi función
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True, port=5005)