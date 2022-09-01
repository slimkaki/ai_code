from aicode.search.SearchAlgorithms import BuscaLargura
from aicode.search.SearchAlgorithms import BuscaProfundidade
from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aicode.search.Graph import State

class VacuumWorld3Room(State):

    def __init__(self, vacuumPosition, isLeftRoomClean, isCenterRoomClean, isRightRoomClean, op):
        self.vacuumPosition = vacuumPosition
        self.isLeftRoomClean = isLeftRoomClean
        self.isCenterRoomClean = isCenterRoomClean
        self.isRightRoomClean = isRightRoomClean
        self.operator = op
    
    def env(self):
        return str(self.vacuumPosition)+";"+str(self.isLeftRoomClean)+";"+str(self.isCenterRoomClean)+";"+str(self.isRightRoomClean)

    def sucessors(self):
        sucessors = [VacuumWorld3Room("right", self.isLeftRoomClean, self.isRightRoomClean, self.isCenterRoomClean, "Move Right"),
                     VacuumWorld3Room("left", self.isLeftRoomClean, self.isRightRoomClean, self.isCenterRoomClean, "Move Left"),
                     VacuumWorld3Room("center", self.isLeftRoomClean, self.isRightRoomClean, self.isCenterRoomClean, "Move Center")]
        
        if (self.vacuumPosition == 'right'):
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, self.isLeftRoomClean, self.isCenterRoomClean, True, 'clean'))
        elif (self.vacuumPosition == 'left'):
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, True, self.isCenterRoomClean, self.isRightRoomClean, 'clean'))
        else:
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, self.isLeftRoomClean, True, self.isRightRoomClean, 'clean'))

        return sucessors
    
    def is_goal(self):
        return (self.isLeftRoomClean and self.isCenterRoomClean and self.isRightRoomClean)
    
    def description(self):
        return "Problema do aspirador de pó, contendo três (3) salas"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

def main():
    
    #
    # Executando busca em largura
    #
    state = VacuumWorld3Room('left', False, False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    
    #
    # Executando busca em profundidade
    #
    state = VacuumWorld3Room('left', False, False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
