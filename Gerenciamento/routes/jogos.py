from flask import Blueprint, render_template
from models import Jogo

jogos_bp = Blueprint("jogos", __name__)

@jogos_bp.route("/agenda")
def agenda():
    jogos = Jogo.query.all()
    return render_template("jogos.html", jogos=jogos)
