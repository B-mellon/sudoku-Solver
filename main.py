from grille import Grille
from solver import Solver

test = [[0, 9, 0, 8, 0, 2, 0, 3, 0],
        [0, 0, 2, 0, 0, 1, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 1],
        [8, 0, 0, 4, 0, 3, 0, 0, 2],
        [0, 0, 0, 2, 0, 0, 0, 0, 6],
        [0, 0, 3, 0, 0, 0, 0, 5, 0],
        [1, 0, 0, 3, 0, 0, 0, 0, 0],
        [9, 3, 0, 0, 0, 0, 6, 0, 0],
        [0, 2, 7, 0, 9, 0, 4, 1, 0]]

grille = Grille(test)
print(grille)
solver = Solver(grille)

##solver.solve()

