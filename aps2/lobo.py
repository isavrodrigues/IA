from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State

#HLWC -> homem, lobo, carneiro, couve
class EstadoHLWC(State):
    def __init__(self, homem, lobo, carneiro, couve):
        self.homem = homem 
        self.lobo = lobo
        self.carneiro = carneiro
        self.couve = couve

    def is_goal(self):
        #todos estao no lado direito
        return self.homem and self.lobo and self.carneiro and self.couve 

    def sucessores(self):
        sucessores = []
        novo_estado = EstadoHLWC(not self.homem, self.lobo, self.carneiro, self.couve)
        if not novo_estado.is_invalido():
            sucessores.append(('Homem se move sozinho', novo_estado))
        
        if self.homem == self.lobo:
            novo_estado = EstadoHLWC(not self.homem, not self.lobo, self.carneiro, self.couve)
            if not novo_estado.is_invalido():
                sucessores.append(('Homem se move com o lobo', novo_estado))
        
        if self.homem == self.carneiro:
            novo_estado = EstadoHLWC(not self.homem, self.lobo, not self.carneiro, self.couve)
            if not novo_estado.is_invalido():
                sucessores.append(('Homem se move com o carneiro', novo_estado))

        if self.homem == self.couve:
            novo_estado = EstadoHLWC(not self.homem, self.lobo, self.carneiro, not self.couve)
            if not novo_estado.is_invalido():
                sucessores.append(('Homem se move com a couve', novo_estado))
        
        return sucessores

    def is_invalido(self):
        #se o lobo comer o carneiro ou a couve
        if self.lobo == self.carneiro and self.homem != self.lobo:
            return True
        if self.carneiro == self.couve and self.homem != self.carneiro:
            return True
        return False

    def __eq__(self, outro):
        return (self.homem == outro.homem and 
                self.lobo == outro.lobo and 
                self.carneiro == outro.carneiro and 
                self.couve == outro.couve)

    def __hash__(self):
        return hash((self.homem, self.lobo, self.carneiro, self.couve))

    def __str__(self):
        return f"Homem: {self.homem}, Lobo: {self.lobo}, Carneiro: {self.carneiro}, Couve: {self.couve}"

def resolver_hlwc():
    estado_inicial = EstadoHLWC(False, False, False, False)
    algoritmo = BuscaLargura()
    resultado = algoritmo.search(estado_inicial)
    if resultado:
        print("Solução encontrada!")
        print(resultado.show_path())
    else:
        print("Nenhuma solução encontrada.")

resolver_hlwc()