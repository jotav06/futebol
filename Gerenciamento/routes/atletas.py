from flask import Blueprint, render_template
from models import Atleta

atletas_bp = Blueprint("atletas", __name__)

@atletas_bp.route("/atletas")
def listar_atletas():
    atletas = Atleta.query.all()
    return render_template("atletas.html", atletas=atletas)

@atletas_bp.route("/atletas/<int:id>")
def detalhe_atleta(id):
    atleta = Atleta.query.get_or_404(id)
    return render_template("atleta_detalhe.html", atleta=atleta)
