from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State

class EstadoU2(State):
    def __init__(self, bono, edge, adam, larry, lanterna, acao):
        self.bono = bono 
        self.edge = edge
        self.adam = adam
        self.larry = larry
        self.lanterna = lanterna
        self.acao = acao 

    def is_goal(self):
        return self.bono and self.edge and self.adam and self.larry and self.lanterna

    def sucessors(self):
        sucessores = []
        
        if self.lanterna == self.bono:
            novo_estado = EstadoU2(not self.bono, self.edge, self.adam, self.larry, not self.lanterna, "Bono atravessa")
            sucessores.append(('Bono atravessa', novo_estado))
        
        if self.lanterna == self.edge:
            novo_estado = EstadoU2(self.bono, not self.edge, self.adam, self.larry, not self.lanterna, "Edge atravessa")
            sucessores.append(('Edge atravessa', novo_estado))
        
        if self.lanterna == self.adam:
            novo_estado = EstadoU2(self.bono, self.edge, not self.adam, self.larry, not self.lanterna, "Adam atravessa")
            sucessores.append(('Adam atravessa', novo_estado))

        if self.lanterna == self.larry:
            novo_estado = EstadoU2(self.bono, self.edge, self.adam, not self.larry, not self.lanterna, "Larry atravessa")
            sucessores.append(('Larry atravessa', novo_estado))
        
        return sucessores

    def cost(self):
        if "Bono" in self.acao:
            return 1
        if "Edge" in self.acao:
            return 2
        if "Adam" in self.acao:
            return 5
        if "Larry" in self.acao:
            return 10
        return 0

    def __eq__(self, other):
        return (self.bono == other.bono and 
                self.edge == other.edge and 
                self.adam == other.adam and 
                self.larry == other.larry and 
                self.lanterna == other.lanterna)

    def __hash__(self):
        return hash((self.bono, self.edge, self.adam, self.larry, self.lanterna))

    def __str__(self):
        return f"Bono: {self.bono}, Edge: {self.edge}, Adam: {self.adam}, Larry: {self.larry}, Lanterna: {self.lanterna}"

def resolver_u2():
     #todos começam no lado esquerdo
    estado_inicial = EstadoU2(False, False, False, False, False, "") 
    algoritmo = AEstrela()
    resultado = algoritmo.search(estado_inicial)
    if resultado:
        print("Solução encontrada!")
        print(resultado.show_path())
    else:
        print("Nenhuma solução encontrada.")


resolver_u2()