from aicode.search.SearchAlgorithms import BuscaGananciosa
from aicode.search.SearchAlgorithms import AEstrela
from aicode.search.Graph import State
import time
import networkx as nx
import csv

class Map(State):

    def __init__(self, actualCity, goalCity, op):
        self.actualCity = actualCity
        self.goalCity = goalCity
        self.operator = op
    
    def sucessors(self):
        sucessors = []

        for city in self.area[self.actualCity]:
            sucessors.append(Map(city[1], 
                                self.goalCity,
                                "move to " + city[1]))

        return sucessors
    
    def is_goal(self):
        return self.actualCity == self.goalCity
    
    def description(self):
        return "The map of cities with road distances"
    
    def cost(self):
        for city in self.area[self.actualCity]:
            if city[1] == self.operator.split()[-1]:
                return city[0]
        return 1
    
    def print(self):
        return str(self.operator)
    
    def env(self):
        return self.actualCity + "#" + str(self.cost)

    def h(self):
        return int(Map.g.edges[self.actualCity, self.goalCity]["distance"])

    @staticmethod
    def createArea():
        #
        # TODO mover a definicao do mapa de uma forma hard-coded para para leitura
        # a partir de um arquivo, similar ao que é feito no metodo createHeuristics()
        # 
        Map.area = {
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

    @staticmethod
    def createHeuristics():
        #
        # O arquvo MapHeuristics.csv considera apenas os objetivos "o" e "x"
        # TODO modificar o arquivo para considerar todas as cidades. talvez modificar
        # a estrutura do arquivo considerando uma estrutura otimizada
        #
        Map.g = nx.Graph()
        f = csv.reader(open("data/MapHeuristics.csv","r"))
        for row in f: 
            Map.g.add_edge(row[0],row[1], distance = row[2])


def mainAEstrela(initial, goal):

    Map.createArea()
    Map.createHeuristics()

    print(f'Busca por algoritmo A*: sair de {initial} e chegar em {goal}')
    state = Map(initial, goal, '')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print('O número de passos da solução é: ' + str(result.g))
        print('O custo da solução é: ' + str(result.h()))
    else:
        print('Não achou solução')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('')
    
def mainGanancioso(initial, goal):

    Map.createArea()
    Map.createHeuristics()

    print(f'Busca por algoritmo Ganancioso: sair de {initial} e chegar em {goal}')
    state = Map(initial, goal, '')
    algorithm = BuscaGananciosa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print('O número de passos da solução é: ' + str(result.g))
        print('O custo da solução é: ' + str(result.h()))
    else:
        print('Não achou solução')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('')


if __name__ == '__main__':
    i, g = 'i', 'x'
    mainAEstrela(i, g)
    mainGanancioso(i, g)
