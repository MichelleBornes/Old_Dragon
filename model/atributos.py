# model/atributos.py
import random

class Atributos:
    atributos_base = ["Força", "Destreza", "Constituição",
                      "Inteligência", "Sabedoria", "Carisma"]

    # 3d6 em ordem fixa: gera os 6 valores e retorna dicionário mapeando atributos na ordem fixa.
    @staticmethod
    def classico():
        atributos = {}
        for atr in Atributos.atributos_base:
            atributos[atr] = sum(random.randint(1, 6) for _ in range(3))
        return atributos

    # Retorna lista das 6 rolagens (usado apenas se preferir apresentar as rolagens).
    @staticmethod
    def rolagens_classicas_list():

        return [sum(random.randint(1, 6) for _ in range(3)) for _ in range(6)]

    # Gera 6 rolagens 3d6 e retorna lista (o usuário distribui livremente).
    @staticmethod
    def aventureiro_rolls():
        return [sum(random.randint(1, 6) for _ in range(3)) for _ in range(6)]

    #Gera 6 rolagens 4d6 descartando o menor em cada conjunto.
    @staticmethod
    def heroico_rolls():
        rolagens = []
        for _ in range(6):
            dados = [random.randint(1, 6) for _ in range(4)]
            dados.remove(min(dados))
            rolagens.append(sum(dados))
        return rolagens