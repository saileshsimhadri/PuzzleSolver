class Constraint:

    def invalidValues(self):
        pass

    def testElement(self, item):
        pass

    def __iter__(self):
        pass

class AllDiffConstraint(Constraint):

    def __init__(self):
        self.cells = set()
        self.cell_dict = {}

    def __iter__(self):
        for cell in self.cells:
            yield cell

    def testElement(self, item):
        for cell in self.cells:
            if len(cell.domain()) == 1 and next(iter(cells.domain())) == item:
                return false
        return true

    def create_dict(self):
        cell_d = {}
        for cell in self.cells:
            d = cell.domain()
            for item in d:
                cell_d.setdefault(item, set()).add(cell)
        return cell_d

    def add_cell(self, cell):
        self.cells.add(cell)

    def invalidValues(self):
        d_remove = {}
        cell_d = self.create_dict()
        for cell in self.cells:
            if(len(cell.domain()) != 1):
                continue
            for other_cell in self.cells:
                if (other_cell != cell):
                    d_remove.setdefault(other_cell, set()).add(next(iter(cell.domain())))
        for item, cells in cell_d.items():
            if len(cells) == 1:
                val = item
                for v in next(iter(cells)).domain():
                    if v != val:
                        d_remove.setdefault(next(iter(cells)), set()).add(v)
        return d_remove
