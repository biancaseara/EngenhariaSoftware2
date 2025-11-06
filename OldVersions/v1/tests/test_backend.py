import pytest
from grey_roots_backend import GameState, Tela

def test_inicializacao():
    jogo = GameState()
    jogo.start()
    assert jogo.tela_atual == Tela.MENU
    assert "Iniciar" in jogo.get_textos()[1]

def test_fluxo_nome_e_signo():
    jogo = GameState()
    jogo.start()

    jogo.process_action("escolha", "1")
    assert jogo.tela_atual == Tela.INTRO

    jogo.process_action("ok")
    assert jogo.tela_atual == Tela.NOME

    jogo.process_action("input", "Lara")
    assert jogo.player.name == "Lara"
    assert jogo.tela_atual == Tela.CONFIRMA_NOME

    jogo.process_action("escolha", "1")
    assert jogo.tela_atual == Tela.SIGNO

    jogo.process_action("input", "Touro")
    assert jogo.player.signo == "Touro"
    assert jogo.player.planta == "Hâdia de Rudá"
    assert jogo.tela_atual == Tela.CONFIRMA_SIGNO
