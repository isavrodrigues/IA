from Puzzle8 import Puzzle8
from datetime import datetime

import pytest
tabuleiro_feito = [[1,2,3],[8,0,4],[7,6,5]]
tabuleiro_trivial = [[1,2,3],[8,4,0],[7,6,5]]
tabuleiro_trivial2 = [[1,2,3],[0,8,4],[7,6,5]]
tabuleiro_trivial3 = [[1,0,3],[8,2,4],[7,6,5]]
tabuleiro_facil = [[8,1,3],[0,7,2],[6,5,4]]
tabuleiro_facil2 = [[8,1,3],[7,0,2],[6,5,4]]
tabuleiro_facil3 = [[0,1,3],[8,7,2],[6,5,4]]
tabuleiro_dificil0 = [[8,3,6],[7,5,4],[2,1,0]]
tabuleiro_dificil1 = [[7,8,6],[2,3,5],[1,4,0]]
tabuleiro_dificil2 = [[7,8,6],[2,3,5],[0,1,4]]
tabuleiro_dificil3 = [[3,1,2],[5,4,8],[0,6,7]]
tabuleiro_dificil4 = [[2,8,6],[7,3,5],[4,0,1]]
tabuleiro_impossivel1 = [[3,4,8],[1,2,5],[7,0,6]]
tabuleiro_impossivel2 = [[5,4,0],[6,1,8],[7,3,2]]
tabuleiro_impossivel3 = [[1,7,2],[3,9,5],[6,4,8]]
tabuleiro_impossivel4 = [[3,1,2],[5,4,8],[0,7,6]]
tabuleiro_invertido = [[8,7,6],[5,0,4],[3,2,1]]

@pytest.mark.timeout(15)
def test_feito():
    print('feito')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_feito, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r == ""
@pytest.mark.timeout(15)
def test_trivial1():
    print('trivial 1')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_trivial, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; esquerda"
@pytest.mark.timeout(15)
def test_trivial2():
    print('trivial 2')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_trivial2, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita"
@pytest.mark.timeout(15)
def test_trivial3():
    print('trivial 3')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_trivial3, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; baixo"
@pytest.mark.timeout(15)
def test_facil1():
    print('facil')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_facil, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 9 and r != "Nao tem solucao"
    #assert r == " ; direita ; direita ; baixo ; esquerda ; esquerda ; cima ; cima ; direita ; baixo"
@pytest.mark.timeout(15)
def test_facil2():
    print('facil')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_facil2, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 8 and r != "Nao tem solucao"
    #assert r == " ; direita ; baixo ; esquerda ; esquerda ; cima ; cima ; direita ; baixo"
@pytest.mark.timeout(15)
def test_facil3():
    print('facil')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_facil3, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 10 and r != "Nao tem solucao"
    #assert r == " ; baixo ; direita ; direita ; baixo ; esquerda ; esquerda ; cima ; cima ; direita ; baixo"
@pytest.mark.timeout(15)
def test_dificil0():
    print('dificil 0')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil0, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 22 and r != "Nao tem solucao"
    #assert r == " ; cima ; cima ; esquerda ; baixo ; esquerda ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; baixo ; direita ; cima ; direita ; baixo ; esquerda ; cima ; cima ; esquerda ; baixo ; direita"
@pytest.mark.timeout(15)
def test_dificil1():
    print('dificil 1')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil1, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 24 and r != "Nao tem solucao"
    #assert r == " ; cima ; esquerda ; baixo ; esquerda ; cima ; cima ; direita ; direita ; baixo ; esquerda ; esquerda ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; direita"
@pytest.mark.timeout(15)
def test_dificil2():
    print('dificil 2')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil2, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 25 and r != "Nao tem solucao"
    #assert r == " ; cima ; cima ; direita ; baixo ; esquerda ; baixo ; direita ; cima ; direita ; cima ; esquerda ; esquerda ; baixo ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; direita ; direita ; baixo ; esquerda ; cima"
@pytest.mark.timeout(15)
def test_dificil3():
    print('dificil 3')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil3, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 26 and r != "Nao tem solucao"
    #assert r == " ; direita ; direita ; cima ; esquerda ; esquerda ; baixo ; direita ; cima ; esquerda ; cima ; direita ; direita ; baixo ; baixo ; esquerda ; cima ; esquerda ; cima ; direita ; baixo ; direita ; cima ; esquerda ; esquerda ; baixo ; direita"
@pytest.mark.timeout(15)
def test_dificil4():
    print('dificil 4')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil4, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 21 and r != "Nao tem solucao"
    #assert r == " ; esquerda ; cima ; cima ; direita ; baixo ; direita ; baixo ; esquerda ; cima ; direita ; cima ; esquerda ; baixo ; esquerda ; cima ; direita ; baixo ; direita ; baixo ; esquerda ; cima"
@pytest.mark.timeout(15)
def test_impossivel1():
    print('impossivel 1')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_impossivel1, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r == "Nao tem solucao"
@pytest.mark.timeout(15)
def test_impossivel2():
    print('impossivel 2')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_impossivel2, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r == "Nao tem solucao"
@pytest.mark.timeout(15)
def test_impossivel3():
    print('impossivel 3')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_impossivel3, '')
    r = state.show_path()
    print(r)
    fim = datetime.now()
    print(fim - inicio)
    assert r == "Nao tem solucao"