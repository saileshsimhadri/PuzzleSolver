class Solver:

    def constraintPropogation(self, puzzle):
        queue = set(puzzle.constraints())
        while(queue):
            constraint = queue.pop()
            for cell, values in constraint.invalidValues().items():
                length = len(cell.domain())
                for value in values:
                    cell.removeFromDomain(value)
                if len(cell.domain()) == 0:
                    return False
                if length == len(cell.domain()):
                    continue
                queue.update(cell.constraints())
        return puzzle

    def backtrack(self, puzzle):
        if (not puzzle) or self.solved(puzzle):
            return puzzle
        cell = self.minDomain(puzzle)
        return self.some(self.backtrack(self.assign(cell.coordinates(), value, puzzle.copy())) for value in cell.domain())

    def some(self, seq):
        """Return some element of seq that is true"""
        for e in seq:
            if(e): return e
        return False

    def minDomain(self, puzzle):
        min = float("inf")
        min_cell = None
        for row in puzzle:
            for cell in row:
                if len(cell.domain()) < min and len(cell.domain()) > 1:
                    min_cell = cell
                    min = len(cell.domain())
        return min_cell

    def solved(self, puzzle):
        for row in puzzle:
            for cell in row:
                if len(cell.domain()) > 1:
                    return False
        return True

    def assign(self, coordinates, value, puzzle):
        puzzle[coordinates[0]][coordinates[1]].assign(value)
        return self.constraintPropogation(puzzle)

    def solve(self, puzzle):
        return self.backtrack(self.constraintPropogation(puzzle))
