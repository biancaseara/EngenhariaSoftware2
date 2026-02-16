from enum import Enum, auto
import time

# Contantes
CHAVE_VELHA = "CHAVE VELHA"
VOLTAR = "Voltar"
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
        # Mapeamos o Enum para o atributo da instância
        mapping = {
            QTEType.TUTORIAL: self.tutorial,
            QTEType.QTE1: self.qte1,
            QTEType.QTE2: self.qte2,
            QTEType.QTE3: self.qte3,
            QTEType.QTE4: self.qte4,
            QTEType.QTE5: self.qte5,
            QTEType.QTE6: self.qte6,
        }

        # Pegamos a lista correspondente
        lista = mapping.get(qte_type)

        # Retornamos o último item se a lista existir e não estiver vazia
        return lista[-1] if lista else None

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
        # Mapeamento para reduzir Complexidade Cognitiva
        handlers = {
            Tela.MENU: self._handle_menu,
            Tela.INTRO: self._handle_intro,
            Tela.NOME: self._handle_nome,
            Tela.CONFIRMA_NOME: self._handle_confirma_nome,
            Tela.SIGNO: self._handle_signo,
            Tela.CONFIRMA_SIGNO: self._handle_confirma_signo,
            Tela.INICIO_DEMO: self._handle_inicio_demo,
            Tela.ESCOLHA_SALAO: self._handle_escolha_salao,
            Tela.BIBLIOTECA: self._handle_biblioteca,
            Tela.GAVETAS: self._handle_gavetas,
            Tela.LAMPIAO: self._handle_lampiao,
            Tela.BIBLIOTECA_CHAVE: self._handle_biblioteca_transicao,
            Tela.BIBLIOTECA_LAMPIAO: self._handle_biblioteca_transicao,
            Tela.BURACO: self._handle_buraco,
            Tela.COZINHA: self._handle_cozinha,
            Tela.COZINHA_CHOICE: self._handle_cozinha_choice,
            Tela.QTE: self._handle_qte,
            Tela.FUGA: self._handle_fuga,
            Tela.ACOUGUE: self._handle_acougue,
            Tela.OUTRO_ANFITRIAO: self._handle_outro_anfitriao,
            Tela.ESCOLHAS_FINAIS: self._handle_escolhas_finais,
            Tela.GAME_OVER: self._handle_fim_triste,
            Tela.FIM: self._handle_fim_real
        }

        handler = handlers.get(self.tela_atual)
        if handler:
            handler(value)

    # --- MÉTODOS PRIVADOS DE SUPORTE ---
    def _handle_menu(self, value):
        if value == "1":
            self.tela_atual = Tela.INTRO
            self.textos = ["Olá, é um prazer ter você conosco.", "[ENTER para continuar]"]
            self.escolhas = ["ok"]
        elif value == "0":
            self.finished = True

    def _handle_intro(self, _):
        self.tela_atual = Tela.NOME
        self.textos = ["Gostaria de ser formal. Qual o seu nome?"]
        self.escolhas = ["input"]

    def _handle_nome(self, value):
        self.player.set_name(value)
        self.tela_atual = Tela.CONFIRMA_NOME
        self.textos = [f"Então o seu nome é {value}, correto?", "[1] SIM", "[2] NÃO"]
        self.escolhas = ["1", "2"]

    def _handle_confirma_nome(self, value):
        if value == "1":
            self.tela_atual = Tela.SIGNO
            self.textos = ["Ótimo.", "Qual o seu signo?"]
            self.escolhas = ["input"]
        else:
            self.tela_atual = Tela.NOME
            self.textos = ["Corrija seu nome, por favor."]
            self.escolhas = ["input"]

    def _handle_signo(self, value):
        self.player.set_signo(value)
        self.definir_planta_por_signo(value)
        self.tela_atual = Tela.CONFIRMA_SIGNO
        self.textos = [f"Então seu signo é {self.player.signo}, correto?", "[1] SIM", "[2] NÃO"]
        self.escolhas = ["1", "2"]

    def _handle_confirma_signo(self, value):
        if value == "1":
            self.tela_atual = Tela.INICIO_DEMO
            self.textos = [f"Seu signo ({self.player.signo}) foi confirmado.", f"Sua planta especial: {self.player.planta}.", "CONTINUAR"]
            self.escolhas = ["ok"]
        else:
            self.tela_atual = Tela.SIGNO
            self.textos = ["Informe seu signo correto:"]
            self.escolhas = ["input"]

    def _handle_inicio_demo(self, _):
        self.tela_atual = Tela.ESCOLHA_SALAO
        self.textos = ["Você está no salão principal da árvore.", "O que deseja fazer?", "1) Biblioteca", "2) Buraco", f"3) {VOLTAR}"]
        self.escolhas = ["1", "2", "3"]

    def _handle_escolha_salao(self, value):
        if value == "1":
            self.tela_atual = Tela.BIBLIOTECA
            self.textos = ["Você entrou na biblioteca.", "1) Estantes", "2) Lampião", f"3) {VOLTAR}"]
            self.escolhas = ["1", "2", "3"]
        elif value == "2":
            self.tela_atual = Tela.BURACO
            self.textos = ["Você se aproxima do buraco escuro.", "CONTINUAR"]
            self.escolhas = ["ok"]
        else:
            self.textos = ["Não Lara, você precisa do livro...", "CONTINUAR"]
            self.escolhas = ["ok"]

    def _handle_biblioteca(self, value):
        if value == "1":
            self.tela_atual = Tela.GAVETAS
            self.textos = ["Gavetas com bolor.", "[1] Forçar", "[2] Deixar"]
            self.escolhas = ["1", "2"]
        elif value == "2":
            self.tela_atual = Tela.LAMPIAO
            self.textos = ["Um lampião.", "[1] Pegar", "[2] Não"]
            self.escolhas = ["1", "2"]
        else:
            self._ir_para_salao()

    def _handle_gavetas(self, value):
        if value == "1":
            self.player.add_item(f"{CHAVE_VELHA}")
            self.choices.impacto1.append(f"Achou a {CHAVE_VELHA}.")
            self.tela_atual = Tela.BIBLIOTECA_CHAVE
            self.textos = ["Achou a CHAVE!", "[1] Pegar lampião", "[2] Sair"]
            self.escolhas = ["1", "2"]
        else:
            self.tela_atual = Tela.BIBLIOTECA
            self.textos = ["Desistiu das gavetas.", "1-Estantes", "2-Lampião", f"3-{VOLTAR}"]
            self.escolhas = ["1", "2", "3"]

    def _handle_lampiao(self, value):
        if value == "1":
            self.player.add_item("LAMPIÃO")
            self.tela_atual = Tela.BIBLIOTECA_LAMPIAO
            self.textos = ["Pegou o lampião.", "[1] Olhar estantes", "[2] Sair"]
            self.escolhas = ["1", "2"]
        else:
            self.tela_atual = Tela.BIBLIOTECA
            self.textos = ["Lampião ficou.", "1-Estantes", "2-Lampião", f"3-{VOLTAR}"]
            self.escolhas = ["1", "2", "3"]

    def _handle_biblioteca_transicao(self, value):
        if value == "1":
            item = "LAMPIÃO" if self.tela_atual == Tela.BIBLIOTECA_CHAVE else f"{CHAVE_VELHA}"
            self.player.add_item(item)
        self._ir_para_salao()

    def _handle_buraco(self, _):
        self.tela_atual = Tela.COZINHA
        self.textos = ["Você chega à cozinha.", "CONTINUAR"]
        self.escolhas = ["ok"]

    def _handle_cozinha(self, _):
        self.tela_atual = Tela.COZINHA_CHOICE
        self.textos = ["Cuca vista.", "[1] Negociar", "[2] Roubar"]
        self.escolhas = ["1", "2"]

    def _handle_cozinha_choice(self, value):
        if value == "1":
            if self.player.has_item(f"{CHAVE_VELHA}"):
                self.player.add_item("HERBÁRIO")
                self.tela_atual = Tela.FUGA
                self.textos = ["Cuca aceitou a chave. Você tem o livro.", "ok"]
            else:
                self.tela_atual = Tela.GAME_OVER
                self.textos = ["Sem chave. GAME OVER.", "ok"]
            self.escolhas = ["ok"]
        else:
            self.qte_aguardando = QTEType.QTE3
            self.tela_atual = Tela.QTE
            self.textos = ["QTE: Pressione 'r'!", "qte"]
            self.escolhas = ["qte"]

    def _handle_qte(self, value):
        self.qte_manager.register_qte(self.qte_aguardando, value)
        if value == "SUCESSO":
            self.player.add_item("HERBÁRIO")
            self.tela_atual = Tela.FUGA
            self.textos = ["Sucesso!", "ok"]
        else:
            self.tela_atual = Tela.GAME_OVER
            self.textos = ["Falhou!", "ok"]
        self.escolhas = ["ok"]

    def _handle_fuga(self, _):
        self.tela_atual = Tela.ACOUGUE
        self.textos = ["Criança presa!", "[1] Salvar", "[2] Fugir"]
        self.escolhas = ["1", "2"]

    def _handle_acougue(self, value):
        if value == "1" and self.player.has_item(f"{CHAVE_VELHA}"):
            msg = "Você salvou a criança!"
        else:
            msg = "A criança não foi salva."
        self.choices.crianca_salva.append(msg)
        self.tela_atual = Tela.OUTRO_ANFITRIAO
        self.textos = [msg, "ok"]
        self.escolhas = ["ok"]

    def _handle_outro_anfitriao(self, _):
        self.tela_atual = Tela.ESCOLHAS_FINAIS
        self.textos = ["Fim da aventura!", f"Escolhas: {self.choices.impacto1}", "ENTER"]
        self.escolhas = ["ok"]

    def _handle_escolhas_finais(self, _):
        self.finished = True
        self.tela_atual = Tela.FIM

    def _handle_fim_triste(self, _):
        self.tela_atual = Tela.FIM
        self.finished = True

    def _handle_fim_real(self, _):
        self.finished = True

    def _ir_para_salao(self):
        self.tela_atual = Tela.ESCOLHA_SALAO
        self.textos = ["Retornou ao salão.", "1) Biblioteca", "2) Buraco", f"3) {VOLTAR}"]
        self.escolhas = ["1", "2", "3"]

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
