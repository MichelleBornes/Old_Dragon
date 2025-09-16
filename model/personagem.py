# model/personagem.py
from .raca import Raca
from .classe import Classe

class Personagem:
    def __init__(self, nome: str, atributos: dict, raca: Raca, classe: Classe):
        self.nome = nome
        self.atributos = atributos
        self.raca = raca
        self.classe = classe

    def as_dict(self):
        return {
            "nome": self.nome,
            "atributos": self.atributos,
            "raca": self.raca.as_dict() if self.raca else None,
            "classe": self.classe.as_dict() if self.classe else None
        }
