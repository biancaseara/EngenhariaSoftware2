from enum import Enum, auto
import time

# Contantes
CHAVE_VELHA = "CHAVE VELHA"
CONTINUAR = "PRESSIONE ENTER PARA CONTINUAR"
DIREITA_BIBLIOTECA = "[1] Ir para a direita (biblioteca)"
FRENTE_BURACO = "[2] Ir para frente (buraco)"
VOLTAR_FORA = "[3] Voltar para fora"
OLHAR_ESTANTES = "[1] Olhar estantes"
PEGAR_LAMPIAO =   "[2] Pegar lampião"
VOLTAR_SALAO = "[3] Voltar para o salão"
RETORNA_SALAO = "Você retorna ao salão."


class Tela(Enum):
    MENU = auto()
    INTRO = auto()
    NOME = auto()
    CONFIRMA_NOME = auto()
    SIGNO = auto()
    CONFIRMA_SIGNO = auto()
    INICIO_DEMO = auto()
    ESCOLHA_SALAO = auto()
    BIBLIOTECA = auto()
    GAVETAS = auto()
    LAMPIAO = auto()
    BIBLIOTECA_CHAVE = auto()
    BIBLIOTECA_LAMPIAO = auto()
    BURACO = auto()
    COZINHA = auto()
    COZINHA_CHOICE = auto()
    FUGA = auto()
    ACOUGUE = auto()
    OUTRO_ANFITRIAO = auto()
    ESCOLHAS_FINAIS = auto()
    GAME_OVER = auto()
    QTE = auto()
    FIM = auto()

class QTEType(Enum):
    TUTORIAL = auto
    QTE1 = auto()
    QTE2 = auto()
    QTE3 = auto()
    QTE4 = auto()
    QTE5 = auto()
    QTE6 = auto()

class QTEManager:
    def __init__(self):
        self.tutorial = []
        self.qte1 = []
        self.qte2 = []
        self.qte3 = []
        self.qte4 = []
        self.qte5 = []
        self.qte6 = []

    def cleanup(self):
        self.tutorial.clear()
        self.qte1.clear()
        self.qte2.clear()
        self.qte3.clear()
        self.qte4.clear()
        self.qte5.clear()
        self.qte6.clear()

    def register_qte(self, qte_type, result):
        if qte_type == QTEType.TUTORIAL:
            self.tutorial.append(result)
        elif qte_type == QTEType.QTE1:
            self.qte1.append(result)
        elif qte_type == QTEType.QTE2:
            self.qte2.append(result)
        elif qte_type == QTEType.QTE3:
            self.qte3.append(result)
        elif qte_type == QTEType.QTE4:
            self.qte4.append(result)
        elif qte_type == QTEType.QTE5:
            self.qte5.append(result)
        elif qte_type == QTEType.QTE6:
            self.qte6.append(result)

    def get_last_result(self, qte_type):
        if qte_type == QTEType.TUTORIAL:
            return self.tutorial[-1] if self.tutorial else None
        elif qte_type == QTEType.QTE1:
            return self.qte1[-1] if self.qte1 else None
        elif qte_type == QTEType.QTE2:
            return self.qte2[-1] if self.qte2 else None
        elif qte_type == QTEType.QTE3:
            return self.qte3[-1] if self.qte3 else None
        elif qte_type == QTEType.QTE4:
            return self.qte4[-1] if self.qte4 else None
        elif qte_type == QTEType.QTE5:
            return self.qte5[-1] if self.qte5 else None
        elif qte_type == QTEType.QTE6:
            return self.qte6[-1] if self.qte6 else None

class Player:
    def __init__(self):
        self.name = ""
        self.signo = ""
        self.planta = ""
        self.inventario = []

    def set_name(self, name):
        self.name = name

    def set_signo(self, signo):
        self.signo = signo

    def add_item(self, item):
        if item not in self.inventario:
            self.inventario.append(item)

    def remove_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)

    def has_item(self, item):
        return item in self.inventario

class Choices:
    def __init__(self):
        self.impacto1 = []
        self.impacto2 = []
        self.impacto3 = []
        self.queimar_arvore = []
        self.crianca_salva = []

    def cleanup(self):
        self.impacto1.clear()
        self.impacto2.clear()
        self.impacto3.clear()
        self.queimar_arvore.clear()
        self.crianca_salva.clear()

class GameState:
    def __init__(self):
        self.tela_atual = Tela.MENU
        self.textos = []
        self.escolhas = []
        self.player = Player()
        self.choices = Choices()
        self.qte_manager = QTEManager()
        self.finished = False
        self.qte_aguardando = None
        self.last_qte_config = None
        self.last_action = None

    def start(self):
        self.tela_atual = Tela.MENU
        self.textos = ["----- THE GUTTER -----", "1) Iniciar aventura (DEMO)", "0) Sair"]
        self.escolhas = ["1", "0"]
        self.player = Player()
        self.choices = Choices()
        self.qte_manager = QTEManager()
        self.finished = False

    def definir_planta_por_signo(self, sign):
        signo = sign.lower()
        if signo in ['áries', 'aries']:
            self.player.planta = 'Ira de Xandoré'
        elif signo == 'touro':
            self.player.planta = 'Hâdia de Rudá'
        elif signo in ['gêmeos', 'gemeos']:
            self.player.planta = 'Awôto de Polô'
        elif signo in ['câncer', 'cancer']:
            self.player.planta = 'Áuéra de Jaci'
        elif signo in ['leão', 'leao']:
            self.player.planta = 'Alâdia de Guaraci'
        elif signo == 'virgem':
            self.player.planta = 'Ewûa de Sumé'
        elif signo == 'libra':
            self.player.planta = 'Inkã de Jurupari'
        elif signo in ['escorpião', 'escorpiao']:
            self.player.planta = 'Anhangá'
        elif signo in ['sagitário', 'sagitario']:
            self.player.planta = 'Mangará de Tupã'
        elif signo == 'capricornio':
            self.player.planta = 'Fogo de Angra'
        elif signo in ['aquário', 'aquario']:
            self.player.planta = 'Flauta de Akuanbuba'
        elif signo == 'peixes':
            self.player.planta = 'Rio de Caramuru'

    def process_action(self, value=None):        
        if self.tela_atual == Tela.MENU:
            if value == "1":
                self.tela_atual = Tela.INTRO
                self.textos = ["Olá, é um prazer ter você conosco.", "[ENTER para continuar]"]
                self.escolhas = ["ok"]
            elif value == "0":
                self.finished = True
        elif self.tela_atual == Tela.INTRO:
            self.tela_atual = Tela.NOME
            self.textos = ["Gostaria de ser formal. Qual o seu nome?"]
            self.escolhas = ["input"]
        elif self.tela_atual == Tela.NOME:
            self.player.set_name(value)
            self.tela_atual = Tela.CONFIRMA_NOME
            self.textos = [f"Então o seu nome é {value}, correto?", "[1] SIM", "[2] NÃO"]
            self.escolhas = ["1", "2"]
        elif self.tela_atual == Tela.CONFIRMA_NOME:
            if value == "1":
                self.tela_atual = Tela.SIGNO
                self.textos = ["Ótimo.", "Qual o seu signo?"]
                self.escolhas = ["input"]
            elif value == "2":
                self.tela_atual = Tela.NOME
                self.textos = ["Corrija seu nome, por favor."]
                self.escolhas = ["input"]
        elif self.tela_atual == Tela.SIGNO:
            self.player.set_signo(value)
            self.definir_planta_por_signo(value)
            self.tela_atual = Tela.CONFIRMA_SIGNO
            self.textos = [f"Então seu signo é {self.player.signo}, correto?", "[1] SIM", "[2] NÃO"]
            self.escolhas = ["1", "2"]
        elif self.tela_atual == Tela.CONFIRMA_SIGNO:
            if value == "1":
                self.tela_atual = Tela.INICIO_DEMO
                self.textos = [
                    f"Seu signo ({self.player.signo}) foi confirmado.",
                    f"Sua planta especial: {self.player.planta}.",
                    CONTINUAR
                ]
                self.escolhas = ["ok"]
            elif value == "2":
                self.tela_atual = Tela.SIGNO
                self.textos = ["Informe seu signo correto:"]
                self.escolhas = ["input"]
        elif self.tela_atual == Tela.INICIO_DEMO:
            self.tela_atual = Tela.ESCOLHA_SALAO
            self.textos = [
                "Você está no salão principal da árvore.",
                "O que deseja fazer?",
                DIREITA_BIBLIOTECA,
                FRENTE_BURACO,
                VOLTAR_FORA
            ]
            self.escolhas = ["1", "2", "3"]
        elif self.tela_atual == Tela.ESCOLHA_SALAO:
            if value == "1":
                self.tela_atual = Tela.BIBLIOTECA
                self.textos = [
                    "Você entrou na biblioteca.",
                    OLHAR_ESTANTES,
                    PEGAR_LAMPIAO,
                    VOLTAR_SALAO
                ]
                self.escolhas = ["1", "2", "3"]
            elif value == "2":
                self.tela_atual = Tela.BURACO
                self.textos = ["Você se aproxima do buraco escuro.", CONTINUAR]
                self.escolhas = ["ok"]
            elif value == "3":
                self.textos = ["Não Lara, você precisa do livro. É por ela, lembra disso...", CONTINUAR]
                self.escolhas = ["ok"]
        elif self.tela_atual == Tela.BIBLIOTECA:
            if value == "1":
                self.tela_atual = Tela.GAVETAS
                self.textos = [
                    "Você vai até as gavetas. Elas estão acumuladas de bolor, mofo e fungos.",
                    "[1] Forçar a gaveta",
                    "[2] Deixar para lá"
                ]
                self.escolhas = ["1", "2"]
            elif value == "2":
                self.tela_atual = Tela.LAMPIAO
                self.textos = [
                    "Você se aproxima do lampião.",
                    "[1] Pegar o lampião",
                    "[2] Não pegar"
                ]
                self.escolhas = ["1", "2"]
            elif value == "3":
                self.tela_atual = Tela.ESCOLHA_SALAO
                self.textos = [
                    RETORNA_SALAO,
                    DIREITA_BIBLIOTECA,
                    FRENTE_BURACO,
                    VOLTAR_FORA
                ]
                self.escolhas = ["1", "2", "3"]
        elif self.tela_atual == Tela.GAVETAS:
            if value == "1":
                self.player.add_item(CHAVE_VELHA)
                self.choices.impacto1.append("Você abriu a gaveta e encontrou a CHAVE VELHA.")
                self.tela_atual = Tela.BIBLIOTECA_CHAVE
                self.textos = [
                    "Você encontrou uma CHAVE VELHA!",
                    "[1] Pegar lampião",
                    "[2] Deixar para lá"
                ]
                self.escolhas = ["1", "2"]
            elif value == "2":
                self.choices.impacto1.append("Você não abriu a gaveta.")
                self.tela_atual = Tela.BIBLIOTECA
                self.textos = [
                    "Você decide não mexer nas gavetas.",
                    OLHAR_ESTANTES,
                    PEGAR_LAMPIAO,
                    VOLTAR_SALAO
                ]
                self.escolhas = ["1", "2", "3"]
        elif self.tela_atual == Tela.LAMPIAO:
            if value == "1":
                self.player.add_item("LAMPIÃO")
                self.choices.impacto2.append("Você pegou o lampião!")
                self.tela_atual = Tela.BIBLIOTECA_LAMPIAO
                self.textos = [
                    "Você pegou o lampião.",
                    OLHAR_ESTANTES,
                    "[2] Deixar pra lá"
                ]
                self.escolhas = ["1", "2"]
            elif value == "2":
                self.choices.impacto2.append("Você não pegou o lampião.")
                self.tela_atual = Tela.BIBLIOTECA
                self.textos = [
                    "Você decide não pegar o lampião.",
                    OLHAR_ESTANTES,
                    PEGAR_LAMPIAO,
                    VOLTAR_SALAO
                ]
                self.escolhas = ["1", "2", "3"]
        elif self.tela_atual == Tela.BIBLIOTECA_CHAVE:
            if value == "1":
                self.player.add_item("LAMPIÃO")
                self.choices.impacto2.append("Você pegou o lampião!")
                self.tela_atual = Tela.ESCOLHA_SALAO
                self.textos = [
                    RETORNA_SALAO,
                    DIREITA_BIBLIOTECA,
                    FRENTE_BURACO,
                    VOLTAR_FORA
                ]
                self.escolhas = ["1", "2", "3"]
            elif value == "2":
                self.choices.impacto2.append("Você não pegou o lampião.")
                self.tela_atual = Tela.ESCOLHA_SALAO
                self.textos = [
                    RETORNA_SALAO,
                    DIREITA_BIBLIOTECA,
                    FRENTE_BURACO,
                    VOLTAR_FORA
                ]
                self.escolhas = ["1", "2", "3"]
        elif self.tela_atual == Tela.BIBLIOTECA_LAMPIAO:
            if value == "1":
                self.player.add_item(CHAVE_VELHA)
                self.choices.impacto1.append("Você abriu a gaveta e encontrou a CHAVE VELHA.")
                self.tela_atual = Tela.ESCOLHA_SALAO
                self.textos = [
                    RETORNA_SALAO,
                    DIREITA_BIBLIOTECA,
                    FRENTE_BURACO,
                    VOLTAR_FORA
                ]
                self.escolhas = ["1", "2", "3"]
            elif value == "2":
                self.choices.impacto1.append("Você não abriu a gaveta.")
                self.tela_atual = Tela.ESCOLHA_SALAO
                self.textos = [
                    RETORNA_SALAO,
                    DIREITA_BIBLIOTECA,
                    FRENTE_BURACO,
                    VOLTAR_FORA
                ]
                self.escolhas = ["1", "2", "3"]
        elif self.tela_atual == Tela.BURACO:
            self.tela_atual = Tela.COZINHA
            self.textos = [
                "Você desce pelo buraco e chega à cozinha.",
                CONTINUAR
            ]
            self.escolhas = ["ok"]
        elif self.tela_atual == Tela.COZINHA:
            self.tela_atual = Tela.COZINHA_CHOICE
            self.textos = [
                "Você vê a Cuca na cozinha.",
                "[1] Tentar negociar",
                "[2] Tentar roubar o livro"
            ]
            self.escolhas = ["1", "2"]
        elif self.tela_atual == Tela.COZINHA_CHOICE:
            if value == "1":
                if self.player.has_item(CHAVE_VELHA):
                    self.textos = [
                        "Você oferece a CHAVE VELHA. A Cuca aceita e entrega o livro.",
                        CONTINUAR
                    ]
                    self.player.add_item("HERBÁRIO")
                    self.tela_atual = Tela.FUGA
                    self.escolhas = ["ok"]
                else:
                    self.textos = [
                        "Você não tem a CHAVE VELHA. A negociação falha.",
                        CONTINUAR
                    ]
                    self.tela_atual = Tela.GAME_OVER
                    self.escolhas = ["ok"]
            elif value == "2":
                # Simulação de QTE de roubo
                self.qte_aguardando = QTEType.QTE3
                self.last_qte_config = {'key': 'r', 'max_time': 2}
                self.tela_atual = Tela.QTE
                self.textos = [
                    "QTE: Pressione 'r' rapidamente!",
                    "Aguarde input do frontend."
                ]
                self.escolhas = ["qte"]
        elif self.tela_atual == Tela.QTE:
            # value deve ser "SUCESSO" ou "FALHA"
            qte_type = self.qte_aguardando
            self.qte_manager.register_qte(qte_type, value)
            if value == "SUCESSO":
                self.player.add_item("HERBÁRIO")
                self.textos = [
                    "Você roubou o livro com sucesso!",
                    CONTINUAR
                ]
                self.tela_atual = Tela.FUGA
                self.escolhas = ["ok"]
            else:
                self.textos = [
                    "Você falhou no roubo! A Cuca te pegou.",
                    "GAME OVER"
                ]
                self.tela_atual = Tela.GAME_OVER
                self.escolhas = ["ok"]
        elif self.tela_atual == Tela.FUGA:
            self.tela_atual = Tela.ACOUGUE
            self.textos = [
                "Você fugiu para o açougue.",
                "Lá encontra uma criança presa.",
                "[1] Usar CHAVE VELHA para salvar",
                "[2] Fugir sem salvar"
            ]
            self.escolhas = ["1", "2"]
        elif self.tela_atual == Tela.ACOUGUE:
            if value == "1" and self.player.has_item(CHAVE_VELHA):
                self.choices.crianca_salva.append("Você salvou a criança!")
                self.textos = [
                    "Você salvou a criança!",
                    CONTINUAR
                ]
                self.tela_atual = Tela.OUTRO_ANFITRIAO
                self.escolhas = ["ok"]
            elif value == "2" or not self.player.has_item(CHAVE_VELHA):
                self.choices.crianca_salva.append("Você não salvou a criança.")
                self.textos = [
                    "Você não conseguiu salvar a criança.",
                    CONTINUAR
                ]
                self.tela_atual = Tela.OUTRO_ANFITRIAO
                self.escolhas = ["ok"]
        elif self.tela_atual == Tela.OUTRO_ANFITRIAO:
            self.tela_atual = Tela.ESCOLHAS_FINAIS
            self.textos = [
                "Fim da aventura!",
                "Veja suas escolhas:",
                f"Impacto 1: {self.choices.impacto1}",
                f"Impacto 2: {self.choices.impacto2}",
                f"Impacto 3: {self.choices.impacto3}",
                f"Queimar árvore: {self.choices.queimar_arvore}",
                f"Criança salva: {self.choices.crianca_salva}",
                "PRESSIONE ENTER PARA finalizar"
            ]
            self.escolhas = ["ok"]
        elif self.tela_atual == Tela.ESCOLHAS_FINAIS:
            self.tela_atual = Tela.FIM
            self.textos = ["Obrigado por jogar The Gutter!", "Feche o jogo."]
            self.escolhas = []
            self.finished = True
        elif self.tela_atual == Tela.GAME_OVER:
            self.tela_atual = Tela.FIM
            self.textos = ["GAME OVER!", "Feche o jogo."]
            self.escolhas = []
            self.finished = True

    def get_textos(self):
        return self.textos

    def get_escolhas(self):
        return self.escolhas

    def get_estado_jogo(self):
        # Para debugging ou salvar progresso
        return {
            "tela_atual": self.tela_atual,
            "player": vars(self.player),
            "choices": vars(self.choices),
            "qte": {
                "tutorial": self.qte_manager.tutorial,
                "qte1": self.qte_manager.qte1,
                "qte2": self.qte_manager.qte2,
                "qte3": self.qte_manager.qte3,
                "qte4": self.qte_manager.qte4,
                "qte5": self.qte_manager.qte5,
                "qte6": self.qte_manager.qte6
            }
        }

    def is_finished(self):
        return self.finished
