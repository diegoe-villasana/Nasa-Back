from flask import Flask, jsonify, request, render_template
from controllers import calculos #se manda a las funciones de controllers

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lista", methods=["GET"])
def lista_meteoros():
    names = calculos.obtener_nombres()
    return jsonify(names)

@app.route("/infoasteroide", methods=["GET"])
def info_asteroide():
    name = request.args.get("name")
    info = calculos.obtener_info(name)
    if info:
        return jsonify(info)
    return jsonify({"error": "No encontrado"}), 404

@app.route("/lista_mayor_impacto", methods=["GET"])
def lista_mayor_impacto():
    top5 = calculos.top_impacto(5)
    return jsonify(top5)

if __name__ == "__main__":
    app.run(debug=True)
