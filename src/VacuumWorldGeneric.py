from sre_constants import SUCCESS
from aicode.search.SearchAlgorithms import BuscaLargura
from aicode.search.SearchAlgorithms import BuscaProfundidade
from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aicode.search.Graph import State

class VacuumWorldGeneric(State):

    def __init__(self, mapa, row, col, op):
        self.mapa = mapa
        self.row = row
        self.col = col
        self.operator = op

    def env(self):
        s = ""
        for i in self.mapa:
            for j in i:
                s += str(int(j)) + ";"
            s = s[:len(s)-1] + "\n"
        return s

    def cost(self):
        return 1

    def description(self):
        return "Problema do aspirador de pó, contendo uma sala genérica"

    def sucessors(self):
        sucessors = []

        newMapa = []
        for i in range(len(self.mapa)):
            newMapa.append(self.mapa[i].copy())

        newMapa[self.row][self.col] = False
        sucessors.append(VacuumWorldGeneric(newMapa, self.row, self.col, "limpar"))

        if (self.row == 0):
            sucessors.append(VacuumWorldGeneric(self.mapa, self.row, self.col, "Move Up"))
        else:
            sucessors.append(VacuumWorldGeneric(self.mapa, self.row-1, self.col, "Move Up"))

        if (self.row == len(self.mapa)-1):
            sucessors.append(VacuumWorldGeneric(self.mapa, self.row, self.col, "Move Down"))
        else:
            sucessors.append(VacuumWorldGeneric(self.mapa, self.row+1, self.col, "Move Down"))
        
        if (self.col == 0):
            sucessors.append(VacuumWorldGeneric(self.mapa, self.row, self.col, "Move Left"))
        else:
            sucessors.append(VacuumWorldGeneric(self.mapa, self.row, self.col-1, "Move Left"))

        if (self.col == len(self.mapa[0])-1):
            sucessors.append(VacuumWorldGeneric(self.mapa, self.row, self.col, "Move Right"))
        else:
            sucessors.append(VacuumWorldGeneric(self.mapa, self.row, self.col+1, "Move Right"))

        return sucessors

    def print(self):
        return str(self.operator)

    def is_goal(self):
        for r in self.mapa:
            if any(r):
                return False
        return True

def convert_file_to_map(filename):
    f = open(filename, "r")
    mapa = []
    for line in f.readlines():
        row = []
        for pos in line:
            if (pos.isalnum()):
                row.append(bool(int(pos)))
        mapa.append(row)
    f.close()
    return mapa

def main():
    file_map_path = 'data/vacuum_simple_2.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')

def main2():
    print('\n#### Largura Simples 2 ####')
    file_map_path = 'data/vacuum_simple_2.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')

def exemplo3():
    print('\n#### Largura Simples 2 ####')
    file_map_path = 'data/example_2.txt'
    lin = 2
    col = 3
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    print('\n')

if __name__ == '__main__':
    exemplo3()