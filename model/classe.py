# model/classe.py
class Classe:
    def __init__(self, nome, pv_base, habilidades):
        self.nome = nome
        self.pv_base = pv_base
        self.habilidades = habilidades

    def as_dict(self):
        return {
            "nome": self.nome,
            "pv_base": self.pv_base,
            "habilidades": self.habilidades
        }

# CLASSES disponíveis
CLASSES = {
    "Guerreiro": Classe("Guerreiro", "1d10", ["Especialista em armas", "Ataque base elevado"]),
    "Clérigo": Classe("Clérigo", "1d8", ["Conjura Magias Divinas", "Afasta Mortos-Vivos"]),
    "Mago": Classe("Mago", "1d4", ["Conjura Magias Arcanas", "Lê Magias", "Detecta Magias"])
}
