from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade, BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
from datetime import datetime

class SumOne(State):

    def __init__(self, n, op, g):
        self.operator = op
        self.number = n
        self.goal = g

    def successors(self):
        sucessors = []
        if self.number < self.goal:
            sucessors.append(SumOne(self.number+1, "+1 ", self.goal))
            sucessors.append(SumOne(self.number+2, "+2 ", self.goal))
        return sucessors

    def is_goal(self):
        return self.goal == self.number

    def description(self):
        return "Este é um agente simples que sabe somar 1 e 2"

    def cost(self):
        return 1

    def env(self):
        return self.number

def run_experiment(algorithm_class, state, *args):
    algorithm = algorithm_class()
    start_time = datetime.now()
    result = algorithm.search(state, *args)
    end_time = datetime.now()
    return result, (end_time - start_time).total_seconds()

def main():
    with open('tabela.csv', 'a') as f:
        print("Algoritmo\tObjetivo\tTempo de processamento (s)")

        for objetivo in range(48, 51):
            # print(f"Objetivo: {objetivo}")
            state = SumOne(1, '', objetivo)

            # Busca em Largura
            # result, time_taken = run_experiment(BuscaLargura, state)
            # print(f"\n{'Busca em Largura'},{objetivo},{time_taken if result else 'NaN'}")
            # f.write(f"\n{'Busca em Largura'},{objetivo},{time_taken if result else 'NaN'}")

            # Busca em Profundidade com limite 10
            result, time_taken = run_experiment(BuscaProfundidade, state, 10)
            print(f"\n{'Busca em Profundidade com produndidade 10'},{objetivo},{time_taken if result else 'NaN'}")
            f.write(f"\n{'Busca em Profundidade com produndidade 10'},{objetivo},{time_taken if result else 'NaN'}")

            # # Busca em Profundidade com limite 20
            result, time_taken = run_experiment(BuscaProfundidade, state, 100)
            print(f"\n{'Busca em Profundidade com produndidade 100'},{objetivo},{time_taken if result else 'NaN'}")
            f.write(f"\n{'Busca em Profundidade com produndidade 100'},{objetivo},{time_taken if result else 'NaN'}")

            # # Busca em Profundidade Iterativa
            result, time_taken = run_experiment(BuscaProfundidadeIterativa, state)
            print(f"\n{'Busca em Profundidade Iterativa'},{objetivo},{time_taken if result else 'NaN'}")
            f.write(f"\n{'Busca em Profundidade Iterativa'},{objetivo},{time_taken if result else 'NaN'}")

    # Imprimir resultados
        

if __name__ == '__main__':
    main()