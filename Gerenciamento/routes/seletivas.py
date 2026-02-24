from flask import Blueprint, render_template
from models import Seletiva

seletivas_bp = Blueprint("seletivas", __name__)

@seletivas_bp.route("/seletivas")
def seletivas():
    seletivas = Seletiva.query.all()
    return render_template("seletivas.html", seletivas=seletivas)
