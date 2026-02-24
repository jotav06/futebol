from flask import Flask, render_template
from config import Config
from models import db, Atleta
from routes.atletas import atletas_bp
from routes.jogos import jogos_bp
from routes.seletivas import seletivas_bp
from routes.titulos import titulos_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(atletas_bp)
app.register_blueprint(jogos_bp)
app.register_blueprint(seletivas_bp)
app.register_blueprint(titulos_bp)

@app.route("/")
def index():
    atletas = Atleta.query.limit(3).all()
    return render_template("index.html", atletas=atletas)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    