from tkinter import *
from grille import Grille
from solver import Solver

fenetre = Tk()
fenetre.title("9x9sudoku solver")
fenetre.config(bg = "#87CEEB")
fenetre.geometry("200x300")
fenetre.resizable(0, 0)
grille = Frame(fenetre)

entry = [[],[],[],[],[],[],[],[],[]]

for x in range (0, 9):
    for y in range (0, 9):
        v = StringVar()
        entree = Entry(grille, width=1, textvariable=v).grid(column = y+1, row = x)
        v.set("0")
        entry[x].append(v)
    """   
        if (y+1) % 3 == 0:
            ##mettre un espace
    
    if (x+1) % 3 == 0:
        ##sauter une ligne
    """

grille.grid(column=0, row=0)

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

def clear():
    for i in range(0, 9):
        for j in range(0, 9):
            entry[i][j].set("0")

solve = Button(fenetre, text="solve", command=solve).grid(column = 0, row = 1)
clear = Button(fenetre, text="clear", command=clear).grid(column=0, row=2)

fenetre.mainloop()