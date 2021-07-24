from grille import Grille

"""
Sudoku Solver Algorithms using 
the backtracking idea
"""
class Solver :

    def __init__(self, grid: Grille):
        self.grid = grid
        self.journey = []
        self.moveDirection = 1
        self.solutionExist = False

    def canMoveBack(self):
        if len(self.journey) >= 1:
            return True
        else:
            return False

    def solve(self):
        ##print("solving starts".center(40, "*"))
        ##print(self.grid)

        """
        while recursion can lead to 
        Overflow and problems using a
        while function seems to be a great idea
        """
        solved = False
        stepNbr = 0
        while solved == False:
            stepNbr = stepNbr + 1

            """Clever alternation between Forward and BackWard Movement """
            if self.moveDirection == 1:
                """ ForeWard Movement """
                emptyCC = self.grid.nextEmpty()

                if emptyCC == -1:
                    ##print(self.grid)
                    ##print("Solved !")
                    solved = True
                    self.solutionExist = True
                else :
                    x = emptyCC // 10
                    y = emptyCC % 10

                    self.moveDirection = -1
                    for value in range (1, 10):
                        if self.grid.canBePlaced(x, y, value):
                            self.grid.writte(x, y, value)
                            self.journey.append(x*10 + y)
                            self.moveDirection = 1
                            break
            else:
                """ BackWard Movement """
                if self.canMoveBack()  == True:

                    lastFilled = self.journey[len(self.journey) -1]
                    self.journey.pop()
                    x = lastFilled // 10
                    y = lastFilled % 10
                    actualValue = self.grid.get(x, y)
                    self.grid.writte(x, y, 0)

                    if actualValue == 9:
                        self.moveDirection = -1
                    else :
                        found = False
                        for value in range (actualValue + 1, 10):
                            if self.grid.canBePlaced(x, y, value) :
                                self.grid.writte(x, y, value)
                                self.journey.append(x*10 + y)
                                self.moveDirection = 1
                                found = True
                                break
                        if found == False :
                            self.moveDirection = -1
                else:
                    ##print("No solution !")
                    solved = True
                    self.solutionExist = False

        ##print(stepNbr, " step required")






