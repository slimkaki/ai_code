from mimetypes import init
from aicode.search.SearchAlgorithms import BuscaLargura, BuscaCustoUniforme
from aicode.search.Graph import State

class TravellerProblem(State):

    def __init__(self, mapa, actualCity, goalCity, visited, op):
        self.mapa = mapa
        self.actualCity = actualCity
        self.goalCity = goalCity
        self.operator = op
        self.visited = visited
    
    def sucessors(self):
        sucessors = []

        for city in self.mapa[self.actualCity]:
            if (city not in self.visited):
                v = self.visited.copy()
                v.add(city)
                sucessors.append(TravellerProblem(self.mapa, 
                                 city[1], 
                                 self.goalCity,
                                 v, 
                                 "move to " + city[1]))

        return sucessors
    
    def is_goal(self):
        return self.actualCity == self.goalCity
    
    def description(self):
        return "Travel from one city to another"
    
    def cost(self):
        for city in self.mapa[self.actualCity]:
            if city[1] == self.operator.split()[-1]:
                return city[0]
        return 1


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

    # @staticmethod
def createArea():
    #
    # TODO mover a definicao do mapa de uma forma hard-coded para para leitura
    # a partir de um arquivo, similar ao que é feito no metodo createHeuristics()
    # 
    mapa = {
        'a':[(3,'b'),(6,'c')],
        'b':[(3,'a'),(3,'h'),(3,'k')],
        'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
        'd':[(3,'c'),(1,'f'),(1,'e')],
        'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
        'f':[(1,'g'),(1,'e'),(1,'d')],
        'g':[(2,'c'),(1,'f'),(2,'h')],
        'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
        'i':[(2,'e'),(2,'h')],
        'l':[(1,'k')],
        'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
        'm':[(2,'n'),(1,'x'),(14,'e')],
        'n':[(2,'m'),(3,'k')],
        'o':[(2,'c')],
        'p':[(2,'c')],
        'x':[(1,'m')]
        }
    return mapa

def main_buscaLargura():
    print('Busca em largura')
    mapa = createArea()
    initial, goal = "i", "o"
    visited = set(initial)
    state = TravellerProblem(mapa, initial, goal, visited, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

def main_buscaCustoUniforme():
    print('Busca de Custo Uniforme')
    mapa = createArea()
    initial, goal = "i", "o"
    visited = set(initial)
    state = TravellerProblem(mapa, initial, goal, visited, '')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main_buscaLargura()
    print()
    main_buscaCustoUniforme()