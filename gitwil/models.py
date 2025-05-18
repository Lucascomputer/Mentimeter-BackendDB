from gitwil import db
from datetime import datetime

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow())
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    contato = db.Column(db.String, nullable=True)
    assunto = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer, default=0)

class aluno_resposta(db.Model):
    ip = db.Column(db.String(20), primary_key=True)
    resposta = db.Column(db.String(1), nullable=True)