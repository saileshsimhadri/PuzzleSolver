from copy import deepcopy

class Cell:

    def __init__(self, domain, constraints, x, y):
        self.d = set(domain)
        self.c = set(constraints)
        self.x = x
        self.y = y

    def constraints(self):
        return self.c

    def coordinates(self):
        return self.x, self.y

    def domain(self):
        return self.d

    def removeFromDomain(self, item):
        self.d.discard(item)

    def assign(self, item):
        self.d = set([item])

class Puzzle():

    class Row:

        def __init__(self, cells):
            self.cells = cells

        def __iter__(self):
            for cell in self.cells:
                yield cell

        def __getitem__(self, index):
            return self.cells[index]

    def __init__(self, board, constraints):
        self.rows = []
        current_row = []
        for row in board:
            for cell in row:
                current_row.append(cell)
            self.rows.append(Puzzle.Row(current_row))
            current_row = []
        self.c = constraints


    def __iter__(self):
        for row in self.rows:
            yield row

    def __getitem__(self, index):
        return self.rows[index]

    def constraints(self):
        return self.c

    def copy(self):
        return deepcopy(self)
