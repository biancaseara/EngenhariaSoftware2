import pytest
from grey_roots_backend import GameState, Tela, QTEType

def test_valores_invalidos_no_menu():
    jogo = GameState()
    jogo.start()
    jogo.process_action("escolha", "x")  # valor inesperado
    # Deve permanecer no MENU, sem travar
    assert jogo.tela_atual == Tela.MENU

def test_qte_invalido():
    jogo = GameState()
    jogo.start()
    jogo.tela_atual = Tela.QTE
    jogo.qte_aguardando = QTEType.QTE3
    jogo.process_action("qte", "ERRO")  # valor incorreto
    assert jogo.tela_atual == Tela.GAME_OVER  # Falha deve levar ao fim

def test_remover_item_inexistente():
    from grey_roots_backend import Player
    p = Player()
    p.remove_item("ITEM QUE NÃO EXISTE")
    assert p.inventario == []  # não deve quebrar
