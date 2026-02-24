import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "chave-secreta-escolinha"
    SQLALCHEMY_DATABASE_URI = F"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    