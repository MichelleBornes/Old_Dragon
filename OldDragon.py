import random

#Classe representando o Personagem
class Personagem:
    def __init__(self, nome, atributos): 
        self.nome = nome
        self.atributos = atributos

    def exibirPersonagem(self):
        print(f"\nPersonagem: {self.nome}")
        for atr, valor in self.atributos.items():
            print(f"{atr}: {valor}")

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

    
def main():
    
    print("---------- CRIAÇÃO DE PERSONAGEM (Old Dragon) ---------- ")
    nome = (input("\nDigite o nome do personagem: ")) 
   
    while True:
    
        print("\nEscolha o estilo de distribuição de atributos: ")
        print("1 - Clássico (3d6 em ordem)")
        print("2 - Aventureiro (3d6 distribua como desejar)")
        print("3 - Heróico (4d6 descartando o menor)")

        escolha = input("\nDigite a opção: ")
        if escolha == "1":
            print("ESTILO CLÁSSICO")
            atributos = Atributos.classico()
            break

        elif escolha == "2":
            print("ESTILO AVENTUREIRO")
            atributos = Atributos.aventureiro()
            break

        elif escolha == "3":
            print("ESTILO HERÓICO")
            atributos = Atributos.heroico()
            break

        else:
            print("Opção inválida! Tente Novamente")
    
    

    personagem = Personagem(nome, atributos)
    personagem.exibirPersonagem()

if __name__ == "__main__":
    main()