from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Atleta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)
    pe_preferido = db.Column(db.String(20), nullable=False)
    gols = db.Column(db.Integer, default=0)
    assistencias = db.Column(db.Integer, default=0)

class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adversario = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    campeonato = db.Column(db.String(100))
    local = db.Column(db.String(100))

class Seletiva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20), nullable=False)
    categoria = db.Column(db.String(50))
    descricao = db.Column(db.Text)

class Titulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(50))