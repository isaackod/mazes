"""Basic Classes for Maze construction"""

import random


class Array(object):
    """ Composition of list for returning None outside of list bounds. Also implements tuple notation.
    eg, a = Array([[1, 2], [3, 4]])
    a[0, 0] returns 1. a[5] returns None. Try not to shoot yourself in the foot.
    """
    
    def __init__(self, wrapped):
        self._wrapped = wrapped
    
    def get_single(self, index):
        if index < 0 or index >= len(self._wrapped):
            return None
        else:
            return self._wrapped[index]
    
    def __getitem__(self, indices):
        if isinstance(indices, int):
            return self.get_single(indices)
        else:
            line = self.get_single(indices[0])
            if line:
                return line[indices[1]]
            else:
                return None
            
    def __iter__(self):
        return iter(self._wrapped)
    
    def __repr__(self):
        return str(self._wrapped)

class Cell(object):
    """Cell object initialized with row and column."""
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._links = {}
        # TODO: make these properties the right way 
        self.north, self.south, self.east, self.west = None, None, None, None
        
    def __repr__(self):
        return f"Cell[{self._row}, {self._col}]"
    
    @property
    def row(self):
        return self._row
    
    @property
    def col(self):
        return self._col
    
    @row.setter
    def row(self, val):
        if not isinstance(val,int) or val < 0:
            raise ValueError(f"Recieved: {val}, row idx must be 0+ integer.")
        else:
            self._row = val 
            
    @col.setter
    def col(self, val):
        if not isinstance(val,int) or val < 0:
            raise ValueError(f"Recieved: {val}, col idx must be 0+ integer.")
        else:
            self._col = val 
            
    def link(self, cell, bd=True):
        self._links[cell] = True
        if bd: #bidirectional
            cell.link(self, False)
            
    def unlink(self, cell, bd=True):
        del(self._links[cell])
        if bd: #bidirectional
            cell.unlink(self, False)
    
    def links(self):
        return self._links.keys()
    
    def is_linked(self, cell):
        return cell in self._links.keys()


class Grid(object):
    """Grid object. Zero-indexed, with (0,0) at the top left in printed repr."""
    def __init__(self, rows=6, cols=6):
        self._rows = rows
        self._cols = cols
        self._grid = self.prepare_grid()
        self.prepare_cells()
    
    def __repr__(self):
        output = "+" + "---+" * self._cols + "\n"
        for row in self.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                body = "   "
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body
                top += east_boundary
                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary
                bottom += corner
            top += "\n"
            bottom += "\n"
            output += top
            output += bottom
        return output
    
    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, val):
        if not isinstance(val, int) or val < 0:
            raise ValueError(f"Received {val}; grid rows must be int > 0)")
        else:
            self._rows = val
            
    @property
    def cols(self):
        return self._cols
    
    @cols.setter
    def cols(self, val):
        if not isinstance(val, int) or val < 0:
            raise ValueError(f"Received {val}; grid cols must be int > 0)")
        else:
            self._cols = val
   
    def prepare_grid(self):
        grid = Array([Array([Cell(row, col) for col in range(self._cols)]) for row in range(self._rows)])
        return grid
    
    def prepare_cells(self):
        for line in self._grid:
            for cell in line:
                row, col = cell.row, cell.col
                cell.north = self._grid[row-1, col]
                cell.south = self._grid[row+1, col]
                cell.east = self._grid[row, col+1]
                cell.west = self._grid[row, col-1]
        
    def random_cell(self):
        row = random.randint(0, self._rows-1)
        col = random.randint(0, self._cols-1)
        return self._grid[row][col]
    
    def size(self):
        return self._rows * self._cols
    
    def each_row(self):
        for row in self._grid:
            yield row
    
    def each_cell(self):
        for row in self._grid:
            for cell in row:
                yield cell if cell else None
