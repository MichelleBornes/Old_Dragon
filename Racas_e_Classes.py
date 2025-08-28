import random

class Atributos:
    atributos_base = ["Força", "Destreza", "Constituição", 
                      "Inteligência", "Sabedoria", "Carisma"]
    
    @staticmethod
    #Estilo Clássico: 3d6 em ordem fixa
    def classico():
        atributos = {}

        for atr in Atributos.atributos_base:
            atributos[atr] = sum(random.randint(1, 6) for _ in range(3))

        return atributos
    
    @staticmethod
    #Estilo Aventureiro: 3d6, o jogador escolhe a distribuição
    def aventureiro():
        rolagens = [sum(random.randint(1, 6) for _ in range(3)) for _ in range(6)]
        atributos = {} 
        print("\nRolagens disponíves:", rolagens)
        
        print("Escolha um valor para:")
        for atr in Atributos.atributos_base:
            escolha = int(input(f"{atr}: "))
            while escolha not in rolagens:
                escolha = int(input(f"Valor inválido! Escolha outro valor para {atr}:"))
            atributos[atr] = escolha
            rolagens.remove(escolha) #Remove o numero escolhido da rolagem

        return atributos
    
    @staticmethod
    #Estilo Heróico: 4d6, eliminando o número mais baixo da soma 
    def heroico():
        rolagens = []
        for _ in range(6):
            dados = [random.randint(1, 6) for _ in range(4)]
            dados.remove(min(dados)) #Remove o menor
            rolagens.append(sum(dados))
        atributos = {} 
        print("\nRolagens disponíveis: ", rolagens)
        print("Escolha um valor para: ")
        for atr in Atributos.atributos_base:
            escolha = int(input(f"{atr}: "))
            while escolha not in rolagens:
                escolha = int(input(f"Valor inválido! Escolha de novo para {atr}: "))
            atributos[atr] = escolha
            rolagens.remove(escolha)

        return atributos
    
#Classe Raça    
class Raca:
    def __init__(self, nome, movimento, infravisao, alinhamento, habilidades):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades

    def exibirRaca(self):
        print(f"\nRaça: {self.nome}")
        print(f"Movimento: {self.movimento}m | Ifravisão: {self.infravisao}m | Alinhamento: {self.alinhamento}")
        print(f"Habilidades Raciais:", ", ".join(self.habilidades))

#RAÇAS disponiveis
RACAS = {
    "Humano": Raca("Humano", 9, "0", "Qualquer", ["+10% (XP)", "+1 em uma Jogada de Proteção"]),
    "Elfo": Raca("Elfo", 9, 18, "Tendem à Neutralidade", ["Percepção Natural", "Imunes a Sono/Paralisia", "+1 em arcos"]),
    "Anão": Raca("Anão", 6, 18, "Tendem à Ordem", ["Detectar anomalias em pedras", "+1 em Testes de Constituição", "Inimigos de Orcs/Ogros/Hobglobins"]),
    "Halfling": Raca("Halfling", 6, 0, "Tendem a Neutralidade", ["Furtivos", "Destemidos", "Difícil de acertar por grandes"])
}

#Classe base das Classes do livro
class Classe: 
    def __init__(self, nome, pv_base, habilidades):
        self.nome = nome
        self.pv_base = pv_base
        self.habilidades = habilidades

    def exibirClasse(self):
        print(f"\nClasse: {self.nome}")
        print(f"Pontos de Vida iniciais: {self.pv_base}")
        print(f"Habilidades de Classe: ", ", ".join(self.habilidades))

#CLASSES disponiveis
CLASSES = {
    "Guerreiro": Classe("Guerreiro", "1d10", ["Especialista em armas", "Ataque base elevado"]),
    "Clérigo": Classe("Clérigo", "1d8", ["Conjura Magias Divinas", "Afasta Mortos-Vivos"]),
    "Mago": Classe("Mago", "1d4", ["Conjura Magias Arcanas", "Lê Magias", "Detecta Magias"])
}

#Classe Peresonagem
class Personagem:
    def __init__(self, nome, atributos, raca, classe): 
        self.nome = nome
        self.atributos = atributos
        self.raca = raca
        self.classe = classe

    def exibirPersonagem(self):
        print("\n---------- PERSONAGEM CRIADO ----------")
        print(f"Nome: {self.nome}")
        self.raca.exibirRaca()
        self.classe.exibirClasse()
        print("\nAtributos:")
        for atr, valor in self.atributos.items():
            print(f"{atr}: {valor}")

def main():

    print("---------- CRIAÇÃO DE PERSONAGEM (Old Dragon 2) ---------- ")
    nome = input("\nDigite o nome do personagem: ")

    #Escolha dos atributos
    while True:

        print("\nEscolha o estilo de distribuição de atributos: ")
        print("1 - Clássico (3d6 em ordem)")
        print("2 - Aventureiro (3d6 distribua como desejar)")
        print("3 - Heróico (4d6 descartando o menor)")

        escolha = input("Opção: ")
        if escolha == "1":
            atributos = Atributos.classico()
            break

        elif escolha == "2":
            atributos = Atributos.aventureiro()
            break

        elif escolha == "3":
            atributos = Atributos.heroico()
            break

        else:
            print("Opção inválida! Tente Novamente")


    print("\nEscolha a Raça:")
    for i, r in enumerate(RACAS.keys(), 1):
        print(f"{i} - {r}")
    raca_escolha = list(RACAS.keys())[int(input("Opção: ")) - 1]


    print("\nEscolha a Classe:")
    for i, c in enumerate(CLASSES.keys(), 1):
        print(f"{i} - {c}")
    classe_escolha = list(CLASSES.keys())[int(input("Opção: ")) - 1]


    personagem = Personagem(nome, atributos, RACAS[raca_escolha], CLASSES[classe_escolha])
    personagem.exibirPersonagem()


if __name__ == "__main__":
    main()
