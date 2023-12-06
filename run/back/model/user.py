from config.config import *

class Usuario(db.Model):
    # atributos da usuario
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254),nullable=False)
    email = db.Column(db.String(254), nullable=False)
    senha = db.Column(db.Text, nullable=False)

    # método para expressar a usuario em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.email + ", " + self.senha

    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
        }
