from flask import Blueprint, render_template
from models import Titulo

titulos_bp = Blueprint("titulos", __name__)

@titulos_bp.route("/titulos")
def titulos():
    titulos = Titulo.query.all()
    return render_template("titulos.html", titulos=titulos)

