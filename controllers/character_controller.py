# controllers/character_controller.py
from model.atributos import Atributos
from model.raca import RACAS
from model.classe import CLASSES
from model.personagem import Personagem

# retorna atributos prontos (dict)
def gerar_classico():
    return Atributos.classico()

# retorna lista de rolagens para o usuário distribuir
def gerar_aventureiro():
    return Atributos.aventureiro_rolls()

# retorna lista de rolagens geradas (4d6, descarta menor)
def gerar_heroico():
    return Atributos.heroico_rolls()

def montar_personagem(nome, atributos_dict, raca_key, classe_key):
    raca = RACAS.get(raca_key)
    classe = CLASSES.get(classe_key)
    p = Personagem(nome, atributos_dict, raca, classe)
    return p
