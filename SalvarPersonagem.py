import json
import random
from datetime import datetime
from typing import Dict, List, Any

class PersonagemOldDragon:
    def __init__(self, nome: str, raca: str, classe: str):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = 1
        self.pontos_vida = 0
        self.pontos_vida_maximos = 0
        self.atributos = {}
        self.modificadores = {}
        self.habilidades = []
        self.equipamentos = []
        self.data_criacao = datetime.now().isoformat()
        
    def rolar_dados(self, quantidade: int = 3, lados: int = 6) -> List[int]:
        """Rola dados para gerar atributos"""
        return [random.randint(1, lados) for _ in range(quantidade)]
    
    def calcular_modificador(self, valor: int) -> int:
        """Calcula modificador baseado no valor do atributo"""
        if valor <= 3: return -3
        elif valor <= 5: return -2
        elif valor <= 8: return -1
        elif valor <= 12: return 0
        elif valor <= 15: return +1
        elif valor <= 17: return +2
        else: return +3
    
    def gerar_atributos(self):
        """Gera os 6 atributos principais do personagem"""
        atributos_base = ['FOR', 'DES', 'CON', 'INT', 'SAB', 'CAR']
        self.atributos = {}
        self.modificadores = {}
        
        for atributo in atributos_base:
            # Rola 4d6 e descarta o menor
            dados = self.rolar_dados(4, 6)
            dados.sort()
            valor = sum(dados[1:])  # Descarta o menor
            self.atributos[atributo] = valor
            self.modificadores[atributo] = self.calcular_modificador(valor)
    
    def calcular_pontos_vida(self):
        """Calcula pontos de vida baseado na classe e constituição"""
        mod_con = self.modificadores.get('CON', 0)
        
        # Base de PV por classe (simplificado)
        base_pv = {
            'Guerreiro': 8,
            'Ladino': 4,
            'Clérigo': 6,
            'Mago': 4
        }
        
        self.pontos_vida_maximos = base_pv.get(self.classe, 6) + mod_con
        if self.pontos_vida_maximos < 1:
            self.pontos_vida_maximos = 1
        self.pontos_vida = self.pontos_vida_maximos
    
    def adicionar_habilidade(self, habilidade: str):
        """Adiciona uma habilidade ao personagem"""
        self.habilidades.append(habilidade)
    
    def adicionar_equipamento(self, equipamento: str):
        """Adiciona um equipamento ao personagem"""
        self.equipamentos.append(equipamento)
    
    def salvar_json(self, filename: str = None):
        """Salva o personagem em um arquivo JSON"""
        if filename is None:
            filename = f"personagem_{self.nome.lower().replace(' ', '_')}.json"
        
        # Converte o objeto para dicionário
        dados_personagem = self.__dict__
        
        # Salva em arquivo JSON
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dados_personagem, f, indent=2, ensure_ascii=False)
        
        print(f"Personagem salvo em: {filename}")
        return filename

class CriadorPersonagem:
    def __init__(self):
        self.racas_disponiveis = ['Humano', 'Elfo', 'Anão', 'Halfling', 'Meio-Elfo']
        self.classes_disponiveis = ['Guerreiro', 'Ladino', 'Clérigo', 'Mago']
    
    def criar_personagem(self) -> PersonagemOldDragon:
        """Interface para criação de personagem"""
        print("=== CRIADOR DE PERSONAGEM OLDRAGON ===")
        
        # Nome
        nome = input("Digite o nome do personagem: ").strip()
        
        # Raça
        print("\nRaças disponíveis:")
        for i, raca in enumerate(self.racas_disponiveis, 1):
            print(f"{i}. {raca}")
        
        while True:
            try:
                escolha_raca = int(input("\nEscolha a raça (número): "))
                if 1 <= escolha_raca <= len(self.racas_disponiveis):
                    raca = self.racas_disponiveis[escolha_raca - 1]
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Digite um número válido!")
        
        # Classe
        print("\nClasses disponíveis:")
        for i, classe in enumerate(self.classes_disponiveis, 1):
            print(f"{i}. {classe}")
        
        while True:
            try:
                escolha_classe = int(input("\nEscolha a classe (número): "))
                if 1 <= escolha_classe <= len(self.classes_disponiveis):
                    classe = self.classes_disponiveis[escolha_classe - 1]
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Digite um número válido!")
        
        # Cria personagem
        personagem = PersonagemOldDragon(nome, raca, classe)
        
        # Gera atributos
        print("\nGerando atributos...")
        personagem.gerar_atributos()
        
        # Calcula PV
        personagem.calcular_pontos_vida()
        
        # Adiciona habilidades básicas
        habilidades_base = {
            'Guerreiro': ['Ataque Poderoso', 'Combate com Duas Armas'],
            'Ladino': ['Furtividade', 'Ataque Furtivo', 'Armadilhas'],
            'Clérigo': ['Cura Divina', 'Turnar Mortos-Vivos'],
            'Mago': ['Magia Arcana', 'Identificar Magia']
        }
        
        for habilidade in habilidades_base.get(classe, []):
            personagem.adicionar_habilidade(habilidade)
        
        # Adiciona equipamentos básicos
        equipamentos_base = {
            'Guerreiro': ['Espada Longa', 'Armadura de Couro', 'Escudo'],
            'Ladino': ['Adaga', 'Armadura de Couro', 'Kit de Ladrão'],
            'Clérigo': ['Maça', 'Armadura de Cota de Malha', 'Símbolo Sagrado'],
            'Mago': ['Cajado', 'Livro de Feitiços', 'Poções']
        }
        
        for equipamento in equipamentos_base.get(classe, []):
            personagem.adicionar_equipamento(equipamento)
        
        return personagem
    
    def exibir_personagem(self, personagem: PersonagemOldDragon):
        """Exibe os detalhes do personagem criado"""
        print("\n" + "="*50)
        print("PERSONAGEM CRIADO!")
        print("="*50)
        print(f"Nome: {personagem.nome}")
        print(f"Raça: {personagem.raca}")
        print(f"Classe: {personagem.classe}")
        print(f"Nível: {personagem.nivel}")
        print(f"Pontos de Vida: {personagem.pontos_vida}/{personagem.pontos_vida_maximos}")
        
        print("\nATRIBUTOS:")
        for atributo, valor in personagem.atributos.items():
            mod = personagem.modificadores[atributo]
            sinal = "+" if mod >= 0 else ""
            print(f"  {atributo}: {valor} ({sinal}{mod})")
        
        print("\nHABILIDADES:")
        for habilidade in personagem.habilidades:
            print(f"  - {habilidade}")
        
        print("\nEQUIPAMENTOS:")
        for equipamento in personagem.equipamentos:
            print(f"  - {equipamento}")
        
        print(f"\nData de Criação: {personagem.data_criacao}")

def carregar_personagem(filename: str) -> Dict[str, Any]:
    """Carrega um personagem salvo de um arquivo JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return dados
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado!")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo {filename}!")
        return None

def main():
    """Função principal do programa"""
    criador = CriadorPersonagem()
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Criar novo personagem")
        print("2. Carregar personagem existente")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            # Cria novo personagem
            personagem = criador.criar_personagem()
            
            # Exibe personagem criado
            criador.exibir_personagem(personagem)
            
            # Salva em JSON
            salvar = input("\nDeseja salvar o personagem? (s/n): ").strip().lower()
            if salvar in ['s', 'sim']:
                filename = input("Nome do arquivo (deixe em branco para automático): ").strip()
                if not filename:
                    filename = None
                personagem.salvar_json(filename)
        
        elif opcao == "2":
            # Carrega personagem existente
            filename = input("Digite o nome do arquivo JSON: ").strip()
            dados = carregar_personagem(filename)
            
            if dados:
                print("\nPersonagem carregado:")
                for chave, valor in dados.items():
                    if chave != 'data_criacao':  # Não mostra data completa para simplificar
                        if isinstance(valor, dict):
                            print(f"{chave}:")
                            for sub_chave, sub_valor in valor.items():
                                print(f"  {sub_chave}: {sub_valor}")
                        elif isinstance(valor, list):
                            print(f"{chave}:")
                            for item in valor:
                                print(f"  - {item}")
                        else:
                            print(f"{chave}: {valor}")
        
        elif opcao == "3":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()