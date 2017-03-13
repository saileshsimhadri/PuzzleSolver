from Solver.puzzle import Puzzle
from Solver.puzzle import Cell
from Solver.solver import Solver
from Solver.constraint import AllDiffConstraint

class Sudoku(Puzzle):

    def __init__(self, path):
        s = SudokuParser()
        cells = s.parse(path)
        board = [[0 for x in range(9)] for y in range(9)]
        rowConst = [0 for x in range(9)]
        colConst = [0 for x in range(9)]
        unitConst = [[0 for x in range(3)] for y in range(3)]
        for x in range(0,9):
            rowConst[x] = AllDiffConstraint()
            colConst[x] = AllDiffConstraint()
        for x in range(0,3):
            for y in range(0,3):
                unitConst[x][y] = AllDiffConstraint()
        for x in range(0,9):
            for y in range(0,9):
                unitx = int(x/3)
                unity = int(y/3)
                constraints = [rowConst[x], colConst[y], unitConst[unitx][unity]]
                if cells[x][y] != 0:
                    domain = [cells[x][y]]
                else:
                    domain = [1,2,3,4,5,6,7,8,9]
                board[x][y] = Cell(domain, constraints, x, y)
                rowConst[x].add_cell(board[x][y])
                colConst[y].add_cell(board[x][y])
                unitConst[unitx][unity].add_cell(board[x][y])
        constraints = []
        for c in rowConst:
            constraints.append(c)
        for c in colConst:
            constraints.append(c)
        for row in unitConst:
            for c in row:
                constraints.append(c)
        super(Sudoku, self).__init__(board, constraints)
        self.solver = Solver()

    def solve(self):
        return self.solver.solve(self)

    def __str__(self):
        board = ""
        for row in self:
            for cell in row:
                if len(cell.domain()) == 1:
                    board += str(next(iter(cell.domain()))) + " "
                else:
                    board += ". "
            board += "\n"
        return board


class SudokuParser:

    def parse(self, path):
        s = []
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                s.append([int(char) for char in line.rstrip()])
        return s


if __name__=="__main__":
    s = Sudoku("puzzles/p2.txt")
    print(s)
    print(s.solve())
