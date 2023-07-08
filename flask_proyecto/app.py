from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

promociones = {
"Gold": {"beneficios": "30% de descuencto en todas las compras", "membresia": "10% de nuestros clientes"},
"Silver": {"beneficios": "20% de descuencto en todas las compras", "membresia": "30% de nuestros clientes"}
}

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/promociones/")
def get_all_promociones():
    gold = promociones["Gold"]
    silver = promociones["Silver"]
    return render_template("promociones.html", promocion_gold=gold, promocion_silver=silver)

@app.get("/promociones/<int:id>")
def get_promocion(id):
    if id in promociones:
        promocion = promociones[id]
        return render_template('promociones.html', id=id, promocion=promocion)
    else:
        return ("no existen promociones", 404)