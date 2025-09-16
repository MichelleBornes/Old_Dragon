# model/raca.py
class Raca:
    def __init__(self, nome, movimento, infravisao, alinhamento, habilidades):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades

    def as_dict(self):
        return {
            "nome": self.nome,
            "movimento": self.movimento,
            "infravisao": self.infravisao,
            "alinhamento": self.alinhamento,
            "habilidades": self.habilidades
        }

# RAÇAS disponíveis
RACAS = {
    "Humano": Raca("Humano", 9, "0", "Qualquer", ["+10% (XP)", "+1 em uma Jogada de Proteção"]),
    "Elfo": Raca("Elfo", 9, 18, "Tendem à Neutralidade", ["Percepção Natural", "Imunes a Sono/Paralisia", "+1 em arcos"]),
    "Anão": Raca("Anão", 6, 18, "Tendem à Ordem", ["Detectar anomalias em pedras", "+1 em Testes de Constituição", "Inimigos de Orcs/Ogros/Hobglobins"]),
    "Halfling": Raca("Halfling", 6, 0, "Tendem a Neutralidade", ["Furtivos", "Destemidos", "Difícil de acertar por grandes"])
}
