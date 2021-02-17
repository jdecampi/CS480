#Eight Puzzle Program

from informedSearch import *

class PuzzleState(InformedProblemState):

    def __init__(self, myList):
        self.myList = myList

    def __str__(self):
        return str(self.myList)

    def illegal(self):
        if self.myList.index(0) < 0 or self.myList.index(0) > 8: return 1
        return 0

    def heuristic(self, goal):
        return 0

    def equals(self, state):
        return self.myList == state.myList

    def moveUp(self):
        newList = self.myList[:]
        if (newList.index(0) > 2):
            blank, num = newList.index(0), newList.index(0)-3
            newList[num], newList[blank] = newList[blank], newList[num]
        return PuzzleState(newList)

    def moveLeft(self):
        newList = self.myList[:]
        if ((newList.index(0) != 0) and (newList.index(0) != 3) and (newList.index(0) != 6)):
            blank, num = newList.index(0), newList.index(0)-1
            newList[num], newList[blank] = newList[blank], newList[num]
        return PuzzleState(newList)

    def moveDown(self):
        newList = self.myList[:]
        if (newList.index(0) < 6):
            blank, num = newList.index(0), newList.index(0)+3
            newList[num], newList[blank] = newList[blank], newList[num]
        return PuzzleState(newList)

    def moveRight(self):
        newList = self.myList[:]
        if ((newList.index(0) != 2) and (newList.index(0) != 5) and (newList.index(0) != 8)):
            blank, num = newList.index(0), newList.index(0)+1
            newList[num], newList[blank] = newList[blank], newList[num]
        return PuzzleState(newList)

    def operatorNames(self):
        return ["moveUp", "moveLeft", "moveDown", "moveRight"]

    def applyOperators(self):
        return [self.moveUp(), self.moveLeft(), self.moveDown(), self.moveRight()]

InformedSearch(PuzzleState([1,3,0,8,2,4,7,6,5]), PuzzleState([1,2,3,8,0,4,7,6,5])) #A
print("-----------------------------------------------------------------------------------------------------")
InformedSearch(PuzzleState([1,3,4,8,6,2,0,7,5]), PuzzleState([1,2,3,8,0,4,7,6,5])) #B
print("-----------------------------------------------------------------------------------------------------")
InformedSearch(PuzzleState([0,1,3,4,2,5,8,7,6]), PuzzleState([1,2,3,8,0,4,7,6,5])) #C
print("-----------------------------------------------------------------------------------------------------")
InformedSearch(PuzzleState([7,1,2,8,0,3,6,5,4]), PuzzleState([1,2,3,8,0,4,7,6,5])) #D
print("-----------------------------------------------------------------------------------------------------")
InformedSearch(PuzzleState([8,1,2,7,0,4,6,5,3]), PuzzleState([1,2,3,8,0,4,7,6,5])) #E
print("-----------------------------------------------------------------------------------------------------")
InformedSearch(PuzzleState([2,6,3,4,0,5,1,8,7]), PuzzleState([1,2,3,8,0,4,7,6,5])) #F
print("-----------------------------------------------------------------------------------------------------")
InformedSearch(PuzzleState([7,3,4,6,1,5,8,0,2]), PuzzleState([1,2,3,8,0,4,7,6,5])) #G
print("-----------------------------------------------------------------------------------------------------")
InformedSearch(PuzzleState([7,4,5,6,0,3,8,1,2]), PuzzleState([1,2,3,8,0,4,7,6,5])) #H

'''             Node Expansions
Problem   BFS  A*(tiles)  A*(dist)
A         6    NA         NA
B         77
C         209
D
E
F
G
H
'''
