from tkinter import *
from grille import Grille
from solver import Solver

"""
Tkinter GUI of the sudoku solver
Top Level
"""
fenetre = Tk()
fenetre.title("9x9sudoku solver")
fenetre.config(bg = "#87CEEB")
##fenetre.geometry("230x340")
fenetre.resizable(0, 0)
grille = Frame(fenetre, bg="navajo white")

entry = [[],[],[],[],[],[],[],[],[]]

for x in range (0, 9):
    for y in range (0, 9):

        """Bloc regroupment """
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0

        """Horyzontal Margin """
        if (y+1) % 3 == 0:
            x2 = 10
        elif y == 0:
            x1 = 10

        """Vertical Margin """
        if (x + 1) % 3 == 0:
            y2 = 10
        elif x == 0 :
            y1 = 10

        #toDo : add background color
        v = StringVar()
        entree = Entry(grille, width=1, textvariable=v, highlightbackground="navajo white").grid(column=y, row=x, padx=(x1, x2), pady=(y1, y2))
        v.set("0")
        entry[x].append(v)

grille.grid(column=0, row=0, padx=(5, 5), pady=(5, 5))

def solve():
    matrix = [[], [], [], [], [], [], [], [], []]

    for x in range (0, 9):
        for y in range(0, 9):
            matrix[x].append(int(entry[x][y].get()))

    solver = Solver(Grille(matrix))
    solver.solve()
    if solver.solutionExist == True:
        for i in range(0, 9):
            for j in range(0, 9):
                entry[i][j].set(str(solver.grid.get(i, j)))

    #@toDo : add Color : green when solved, red otherwise

def clear():
    for i in range(0, 9):
        for j in range(0, 9):
            entry[i][j].set("0")



solve = Button(fenetre, text="solve", command=solve, fg="midnight blue",
               highlightbackground="#87CEEB", font=('Comic Sans MS', 16)).grid(column = 0, row = 1)

clear = Button(fenetre, text="clear", command=clear, fg="midnight blue",
               highlightbackground="#87CEEB", font=('Comic Sans MS', 16)).grid(column=0, row=2)

fenetre.mainloop()