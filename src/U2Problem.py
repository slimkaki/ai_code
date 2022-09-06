from aicode.search.SearchAlgorithms import BuscaCustoUniforme
from aicode.search.Graph import State
from itertools import combinations

class U2Solver(State):

    def __init__(self, side, flashlight, op):
        self.operator = op
        self.bandMembersTime = {"Bono": 1, "Edge":2,
                                "Adam": 5, "Larry":10}
        # False = Lado inicial (Esquerda), True = Lado final (Direita)
        self.side = side # Dict com valores em boolean, correspondendo ao lado de cada membro
        self.flashlight = flashlight # Boolean correspondente ao lado da lanterna
    
    def sucessors(self):
        sucessors = []
        if self.flashlight:
            """Nesse caso a lanterna está no lado final da ponte (Direita)"""
            bandNames = []
            for name in self.side:
                if self.side[name]:
                    bandNames.append(name)
            for i in bandNames:
                newSide = self.side.copy()
                newSide[i] = False
                sucessors.append(U2Solver(newSide, 
                                 False,
                                 str(i) + " atravessa para a esquerda (Lado Inicial)"))
        else:
            """Nesse caso a lanterna está no lado final da ponte (Esquerda)"""
            bandNames = []
            for name in self.side:
                if not self.side[name]:
                    bandNames.append(name)
            if (len(bandNames) > 1):
                it = combinations(bandNames, 2)
                for i in it:
                    newSide = self.side.copy()
                    newSide[i[0]], newSide[i[1]] = True, True
                    sucessors.append(U2Solver(newSide, 
                                     True, 
                                     str(i[0]) + " e " + str(i[1]) + " atravessam para a direita (Lado Final)"))
            else:
                newSide = self.side.copy()
                newSide[bandNames[0]] = True
                sucessors.append(U2Solver(newSide,
                                 True,
                                 str(bandNames[0]) + " atravessa para a direita (Lado Final)"))
        return sucessors
    
    def is_goal(self):
        return all(self.side.values()) and self.flashlight
    
    def description(self):
        return """A banda U2 tem um concerto que começa daqui a 17 minutos e todos precisam cruzar uma ponte par chegar lá. Todos os 4 participantes estão do mesmo lado da ponte. É noite. Só há uma lanterna. A ponte suporta, no máximo, duas pessoas. Qualquer pessoa que passe, uma ou duas, deve passar com a lanterna na mão. A lanterna deve ser levada de um lado para outro e não ser jogada. Cada membro da banda tem um tempo diferente para passar de um lado para o outro. O par deve andar no tempo do menos veloz: Bono: 1 minuto para passar; Edge: 2 minutos para passar; Adam: 5 minutos para passar; e Larry: 10 minutos para passar."""
    
    def cost(self):
        travelers = self.operator.split()[0:3]
        if (travelers[2] in self.bandMembersTime):
            return max(self.bandMembersTime[travelers[0]], self.bandMembersTime[travelers[2]])
        return self.bandMembersTime[travelers[0]]

    def print(self):
        #
        # Usado para imprimir a solução encontrada. 
        # O PATH do estado inicial até o final.
        return str(self.operator)
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None


def main():
    print('Busca em profundidade iterativa')
    side = {"Bono": False, "Edge": False, "Adam": False, "Larry": False}
    state = U2Solver(side, False, '')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
        print(f"Custo total: {result.g} minutos")
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()