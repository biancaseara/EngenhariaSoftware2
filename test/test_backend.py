import pytest
from grey_roots_backend import (
    GameState, Tela, Player, QTEManager, QTEType, Choices
)

# ==========================================================
#  TESTES UNITÁRIOS DAS CLASSES AUXILIARES
# ==========================================================

def test_player_basico():
    p = Player()
    p.set_name("Lara")
    p.set_signo("Touro")
    p.add_item("CHAVE")
    p.add_item("CHAVE")  # não duplica
    assert p.has_item("CHAVE")
    p.remove_item("CHAVE")
    assert not p.has_item("CHAVE")


def test_choices_e_qtemanager_cleanup_e_getlast():
    c = Choices()
    c.impacto1.append("teste")
    c.cleanup()
    assert not c.impacto1

    q = QTEManager()
    for t in QTEType:
        q.register_qte(t, "SUCESSO")
        assert q.get_last_result(t) == "SUCESSO"
    q.cleanup()
    for t in QTEType:
        assert q.get_last_result(t) is None


# ==========================================================
#  TESTES DO FLUXO PRINCIPAL DO GAMESTATE
# ==========================================================

def test_start_e_sair():
    game = GameState()
    game.start()
    assert game.tela_atual == Tela.MENU
    game.process_action("0")
    assert game.finished


def test_fluxo_nome_corrigido():
    game = GameState()
    game.start()
    game.process_action("1")  # iniciar
    game.process_action("ok")
    game.process_action("Lara")
    game.process_action("2")  # Corrigir nome
    assert game.tela_atual == Tela.NOME
    game.process_action("Lara")
    game.process_action("1")  # confirmar nome
    game.process_action("Touro")
    game.process_action("2")  # Corrigir signo
    assert game.tela_atual == Tela.SIGNO
    game.process_action("Touro")
    game.process_action("1")
    game.process_action("ok")
    assert game.tela_atual == Tela.ESCOLHA_SALAO


@pytest.mark.parametrize("signo", [
    "Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra",
    "Escorpião", "Sagitário", "Capricornio", "Aquário", "Peixes"
])
def test_definir_planta_por_signo(signo):
    g = GameState()
    g.definir_planta_por_signo(signo)
    assert g.player.planta != ""


def test_fluxo_biblioteca_gaveta_e_voltar():
    g = GameState()
    g.tela_atual = Tela.ESCOLHA_SALAO
    g.process_action("1")  # biblioteca
    g.process_action("1")  # gavetas
    g.process_action("2")  # deixar pra lá
    assert g.tela_atual == Tela.BIBLIOTECA


def test_fluxo_biblioteca_chave_pega_lampiao():
    g = GameState()
    g.tela_atual = Tela.BIBLIOTECA
    g.process_action("1")
    g.process_action("1")
    g.process_action("1")
    assert "CHAVE VELHA" in g.player.inventario
    assert "LAMPIÃO" in g.player.inventario


def test_fluxo_lampiao_e_voltar_salao():
    g = GameState()
    g.tela_atual = Tela.BIBLIOTECA
    g.process_action("2")
    g.process_action("2")
    assert g.tela_atual == Tela.BIBLIOTECA


def test_fluxo_biblioteca_lampiao_pegar_chave():
    g = GameState()
    g.player.add_item("LAMPIÃO")
    g.tela_atual = Tela.BIBLIOTECA_LAMPIAO
    g.process_action("1")
    assert "CHAVE VELHA" in g.player.inventario


def test_fluxo_buraco_para_cozinha():
    g = GameState()
    g.tela_atual = Tela.ESCOLHA_SALAO
    g.process_action("2")
    g.process_action("ok")
    assert g.tela_atual == Tela.COZINHA


def test_fluxo_fuga_e_salvar_crianca_sem_chave():
    g = GameState()
    g.tela_atual = Tela.FUGA
    g.process_action("ok")
    g.process_action("2")
    assert "não" in " ".join(g.choices.crianca_salva).lower()


def test_fluxo_fuga_e_salvar_crianca_com_chave():
    g = GameState()
    g.tela_atual = Tela.FUGA
    g.player.add_item("CHAVE VELHA")
    g.process_action("ok")
    g.process_action("1")
    assert "salvou" in " ".join(g.choices.crianca_salva).lower()


def test_outro_anfitriao_ate_fim():
    g = GameState()
    g.tela_atual = Tela.OUTRO_ANFITRIAO
    g.process_action("ok")
    g.process_action("ok")
    assert g.finished


# ==========================================================
#  TESTES DE COZINHA / QTE
# ==========================================================

def test_negociar_com_cuca_com_chave():
    g = GameState()
    g.tela_atual = Tela.COZINHA_CHOICE
    g.player.add_item("CHAVE VELHA")
    g.process_action("1")
    assert "HERBÁRIO" in g.player.inventario


def test_negociar_com_cuca_sem_chave():
    g = GameState()
    g.tela_atual = Tela.COZINHA_CHOICE
    g.process_action("1")
    assert g.tela_atual == Tela.GAME_OVER


def test_roubo_qte_sucesso():
    g = GameState()
    g.tela_atual = Tela.COZINHA_CHOICE
    g.process_action("2")
    assert g.tela_atual == Tela.QTE
    g.process_action("SUCESSO")
    assert g.tela_atual == Tela.FUGA


def test_roubo_qte_falha():
    g = GameState()
    g.qte_aguardando = QTEType.QTE3
    g.tela_atual = Tela.QTE
    g.process_action("FALHA")
    assert g.tela_atual == Tela.GAME_OVER


def test_game_over_e_fim():
    g = GameState()
    g.tela_atual = Tela.GAME_OVER
    g.process_action("ok")
    assert g.finished


def test_get_estado_jogo_funcoes_auxiliares():
    g = GameState()
    g.start()
    estado = g.get_estado_jogo()
    assert isinstance(estado, dict)
    assert isinstance(g.get_textos(), list)
    assert isinstance(g.get_escolhas(), list)
    assert not g.is_finished()


# ==========================================================
#  TESTES ADICIONAIS PARA COBRIR RAMOS NÃO TESTADOS
#  (linhas apontadas no relatório de coverage)
# ==========================================================

def test_escolha_salao_opcao_3_mostra_texto_e_ok():
    g = GameState()
    g.tela_atual = Tela.ESCOLHA_SALAO
    g.process_action("3")
    assert g.escolhas == ["ok"]
    assert any("Você precisa do livro" in t or "Não Lara" in t for t in g.textos)


def test_biblioteca_opcao_3_retorna_para_salao():
    g = GameState()
    g.tela_atual = Tela.BIBLIOTECA
    g.process_action("3")
    assert g.tela_atual == Tela.ESCOLHA_SALAO
    assert "Você retorna ao salão." in g.textos[0]


def test_lampiao_pegar_adiciona_item_e_muda_tela():
    g = GameState()
    g.tela_atual = Tela.LAMPIAO
    g.process_action("1")
    assert "LAMPIÃO" in g.player.inventario
    assert g.tela_atual == Tela.BIBLIOTECA_LAMPIAO


def test_biblioteca_chave_opcao_2_retorna_salao():
    g = GameState()
    g.tela_atual = Tela.BIBLIOTECA_CHAVE
    g.process_action("2")
    assert g.tela_atual == Tela.ESCOLHA_SALAO
    assert "Você retorna ao salão." in g.textos[0]


def test_biblioteca_lampiao_opcao_2_retorna_salao():
    g = GameState()
    g.tela_atual = Tela.BIBLIOTECA_LAMPIAO
    g.player.add_item("CHAVE VELHA")   # garante que o item exista
    g.player.remove_item("CHAVE VELHA")  # agora a remoção efetiva ocorre
    g.process_action("2")
    assert g.tela_atual == Tela.ESCOLHA_SALAO
    assert "Você retorna ao salão." in g.textos[0]


def test_cozinha_transicao_para_escolha_qte():
    g = GameState()
    g.tela_atual = Tela.COZINHA
    g.process_action("ok")
    assert g.tela_atual == Tela.COZINHA_CHOICE
    assert "[1] Tentar negociar" in " ".join(g.textos)

def test_cobertura_fim_real():
    g = GameState()
    # Forçamos o estado para a tela FIM
    g.tela_atual = Tela.FIM
    # Chamamos uma ação qualquer para disparar o handler
    g.process_action("ok")
    # Verificamos se ele executou a linha self.finished = True
    assert g.finished is True