"""
class Grille : class extending the functionality a 9 by 9 matrix
               to represent an interactable sudoku Grid
"""
class Grille :

    blocHash = [[1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9]]

    """
    Creation of a Grille with the given 9 by 9 matrix (list of list)
    """
    def __init__(self, matrix: list):
        if type(matrix) != list:
            raise TypeError

        elif len(matrix) != 9:
            raise ValueError

        else :
            matrixCopie = []

            for i in range(0, 9):
                if len(matrix[i]) != 9:
                    raise ValueError
                else :
                    matrixCopie.append(list.copy(matrix[i]))

            self.matrix = matrixCopie

    """
    Textual Representation of The Grid
    """
    def __str__(self):
        rpz = "\n *Grille de sudoku* \n"
        for i in range(0, 9):
            for y in range(0, 9):
                rpz = rpz + str(self.matrix[i][y]) + " "
                if (y + 1) % 3 == 0 and y != 8: rpz += "| "
            rpz += "\n"
            if (i + 1) % 3 == 0 and i != 8 :
                rpz += "-"*21
                rpz += "\n"
        return rpz

    """
    Check if a given Value is in the matrix in the lineNumber
    """
    def inLine(self, lineNumber : int, value: int) -> bool:
        if lineNumber > 8 or lineNumber < 0 or value > 9 or value < 1:
            raise ValueError
        else:
            for y in range(0, 9):
                if self.matrix[lineNumber][y] == value: return True
            return False

    """
    Check if a given Value is in the matrix in the ColumnNumber
    """
    def inColumn(self, columnNumber: int, value: int) -> bool :
        if columnNumber > 8 or columnNumber < 0 or value > 9 or value < 1:
            raise ValueError
        else:
            for i in range(0, 9):
                if self.matrix[i][columnNumber] == value : return True
            return False

    """
    Hash function to determine the bloc value 
    """
    def hashToBloc(self, line:int, column:int) -> int :
        if column < 0 or column > 9 or line > 8 or line < 0:
            raise ValueError
        else :
            return self.blocHash[line][column]

    """
    Check if a given Value is in the matrix in a given Bloc
    """
    def inBloc(self, lineNumber: int, columnNumber: int, value:int) -> bool:
        thisBloc = self.hashToBloc(lineNumber, columnNumber)
        if value < 1 or value > 9 or lineNumber > 8 or lineNumber < 0 or columnNumber > 8 or columnNumber < 0:
            raise ValueError
        else :
            for i in range (0, 9):
                for y in range(0, 9):
                    if thisBloc == self.hashToBloc(i, y) and self.matrix[i][y] == value : return True
            return False

    """
    Return True if the given value can be put at the given position
    """
    def canBePlaced(self, lineNumber: int, columnNumber: int, value: int) -> bool:
        if not self.inLine(lineNumber, value) and not self.inColumn(columnNumber, value) and not self.inBloc(lineNumber, columnNumber, value) :
            return True
        else :
            return False

    """
    Put the value at the given position
    """
    def writte(self, lineNumber, columnNumber, value):
        if lineNumber > 8 or lineNumber < 0 or columnNumber > 8 or columnNumber < 0 or value > 9 or columnNumber < 0 :
            raise ValueError
        else :
            self.matrix[lineNumber][columnNumber] = value

    """
    Return the position of the next Empty case in the grid 
    """
    def nextEmpty(self) -> int:
        for x in range(0, 9):
            for y in range(0, 9):
                if self.matrix[x][y] == 0:
                    return (x*10+y) #empty cases founded and hashed
        return -1 #no empty case found

    """
    Get the value at a postion
    """
    def get(self, lineNumber: int, columnNumber: int) -> int:
        if lineNumber > 8 or lineNumber < 0 or columnNumber > 8 or columnNumber < 0:
            raise ValueError
        else :
            return self.matrix[lineNumber][columnNumber]



