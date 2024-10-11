from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State

class Puzzle8(State):
    def __init__(self, tabuleiro, operacoes=''):
        self.tabuleiro = tabuleiro
        self.operator = operacoes
        self.goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    def successors(self):     
        sucessors = []
        directions = ["cima", "baixo", "esquerda", "direita"]
        for direction in directions:
            novo_estado = self.move(direction)
            if novo_estado:
                sucessors.append(novo_estado)
        return sucessors

    def is_goal(self):
        return self.tabuleiro == self.goal

    def description(self):
        return "Este é um agente que resolve o problema do 8-puzzle."

    def cost(self):
        return 1 

    def env(self):
        return str(self.tabuleiro)

    def get_pos(self, valor):
        for i, row in enumerate(self.tabuleiro):
            if valor in row:
                return (i, row.index(valor))
        return None

    def move(self, direction):
        zero_pos = self.get_pos(0)
        new_tabuleiro = [row[:] for row in self.tabuleiro]  
        i, j = zero_pos

        if direction == "cima" and i > 0:
            antigo = new_tabuleiro[i-1][j]
            new_tabuleiro[i-1][j] = new_tabuleiro[i][j]
            new_tabuleiro[i][j] = antigo
            return Puzzle8(new_tabuleiro, 'cima')
        elif direction == "baixo" and i < 2:
            antigo = new_tabuleiro[i+1][j]
            new_tabuleiro[i+1][j] = new_tabuleiro[i][j]
            new_tabuleiro[i][j] = antigo
            return Puzzle8(new_tabuleiro, 'baixo')
        elif direction == "esquerda" and j > 0:
            antigo = new_tabuleiro[i][j-1]
            new_tabuleiro[i][j-1] = new_tabuleiro[i][j]
            new_tabuleiro[i][j] = antigo
            return Puzzle8(new_tabuleiro, 'esquerda')
        elif direction == "direita" and j < 2:
            antigo = new_tabuleiro[i][j+1]
            new_tabuleiro[i][j+1] = new_tabuleiro[i][j]
            new_tabuleiro[i][j] = antigo
            return Puzzle8(new_tabuleiro, 'direita')
        return None

    #funcao heuristica que caulcula a soma das distancias de manhattan para todas as pecas
    def h(self):
        dist = 0
        for i in range(3):
            for j in range(3):
                value = self.tabuleiro[i][j]
                if value != 0:
                    goal_pos = self.get_pos(value)
                    dist += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
        return dist


    def show_path(self):
        algorithm = AEstrela()
        result = algorithm.search(self)
        if result is not None:
            return result.show_path()
        else:
            return 'Nao achou solucao'