from aicode.search.SearchAlgorithms import AEstrela
from aicode.search.Graph import State
import math

class Puzzle8(State):

    objetivo = [[1,2,3],[8,0,4],[7,6,5]]

    def __init__(self):
        #TODO
        pass
    
    def sucessors(self):
        sucessors = []
        #TODO
        return sucessors
    
    def is_goal(self):
        #TODO
        return True
    
    def description(self):
        return "8 Puzzle"
    
    def cost(self):
        #TODO
        pass

    def print(self):
        return str(self.operator)
    
    def env(self):
        return str(self.tabuleiro)

    def h(self):
        #TODO
        pass

    #
    # Deve-se calcular a quantidade de inversões necessárias para ordenar 
    # certa sequência numérica, determinado por Possível a quantidade de 
    # inversões pares e Impossível a quantidade de inversões ímpares.
    # 
    # referência: https://pt.stackoverflow.com/questions/333702/como-verificar-se-o-sliding-puzzle-%C3%A9-solucion%C3%A1vel 
    #
    def tem_solucao(tabuleiro):
        count = 0
        lista = []
        for lin in range(0,3):
            for col in range(0,3):
                if tabuleiro[lin][col] != 0:
                    lista.append(tabuleiro[lin][col])
        for i in range(0,8):
            for j in range(i+1,8):
                if lista[i] > lista[j]:
                    count = count + 1
        if count % 2:
            return True
        else:
            return False
        
    def show_path(state):
        algorithm = AEstrela()
        if not Puzzle8.tem_solucao(state.tabuleiro):
            return 'Nao tem solucao' 
        result = algorithm.search(state)
        if result != None:
            return result.show_path()
        else:
            return 'Nao achou solucao'


def main():

    tabuleiro_facil = [[8,1,3],[0,7,2],[6,5,4]]
    tabuleiro_dificil1 = [[7,8,6],[2,3,5],[1,4,0]]
    tabuleiro_dificil2 = [[7,8,6],[2,3,5],[0,1,4]]
    tabuleiro_dificil3 = [[8,3,6],[7,5,4],[2,1,0]]
    tabuleiro_impossivel1 = [[3,4,8],[1,2,5],[7,0,6]]
    tabuleiro_impossivel2 = [[5,4,0],[6,1,8],[7,3,2]]

    state = Puzzle8(tabuleiro_facil,'')
    print(state.show_path())

if __name__ == '__main__':
    main()