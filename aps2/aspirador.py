from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme
from aigyminsper.search.Graph import State
import time

# Mapa onde 0 -> limpo e 1 -> sujo
class VacuumWorldState(State):
    def __init__(self, estado_inicial, cost_value, operacao, estado_final):
        #copia o mapa
        self.mapa = [row[:] for row in estado_inicial]  
        self.lin = estado_final[0]  
        self.col = estado_final[1]  
        self.operator = operacao  
        self.estado_final = estado_final  
        self.cost_value = cost_value 

    def successors(self):
        successors = []
        rows = len(self.mapa)
        cols = len(self.mapa[0])

        #limpa se estiver suja
        if self.mapa[self.lin][self.col] == 1:
            new_map = [row[:] for row in self.mapa]
            new_map[self.lin][self.col] = 0  # Limpa a célula atual
            new_state = VacuumWorldState(new_map, self.custo + 1, 'limpar', (self.lin, self.col))
            successors.append(new_state)

        #movimentacao aspirador
        if self.col + 1 < cols:
            new_state = VacuumWorldState(self.mapa, self.custo + 1, 'dir', (self.lin, self.col + 1))
            successors.append(new_state)

        if self.col - 1 >= 0:
            new_state = VacuumWorldState(self.mapa, self.custo + 1, 'esq', (self.lin, self.col - 1))
            successors.append(new_state)

        if self.lin + 1 < rows:
            new_state = VacuumWorldState(self.mapa, self.custo + 1, 'baixo', (self.lin + 1, self.col))
            successors.append(new_state)

        if self.lin - 1 >= 0:
            new_state = VacuumWorldState(self.mapa, self.custo + 1, 'cima', (self.lin - 1, self.col))
            successors.append(new_state)

        return successors

    def is_goal(self):
        #verefica se todas as celulas estão limpas
        return all(all(cell == 0 for cell in row) for row in self.mapa)

    def description(self):
        return "Problema do Aspirador de Pó - Busca de solução para limpar todas as células"

    def cost(self):
        return self.cost_value

    def env(self):
        return (self.mapa, self.lin, self.col)

#executa a busca
def main():
    print("Busca de Custo Uniforme - Aspirador de Pó")
    initial_map = [[1, 1, 1], [1, 0, 1], [1, 1, 1]] 
    initial_position = (0, 0) 
    

    initial_state = VacuumWorldState(initial_map, 0, '', initial_position)
    
    algorithm = BuscaCustoUniforme()
    
    start = time.time()
    result = algorithm.search(initial_state, trace=True)
    
    end = time.time()
    
    if result is not None:
        print("Solução encontrada!")
        path = result.show_path()
        print(path)
        print("Custo total: ", result.g)
        print("Tempo de execução: ", end - start)
    else:
        print("Não foi encontrada uma solução.")


def return_result(state):
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    return result

if __name__ == "__main__":
    main()