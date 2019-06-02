"""Various maze creation strategies."""
from maze_utils import *
import random

class BinaryTree(Grid):
    """Binary tree algorithm. Start at (0,0), flip a coin to go south or east. Enforce boundaries."""
    def on(self):
        for cell in self.each_cell():
            neighbors = []
            if cell.south:
                neighbors.append(cell.south)
            if cell.east:
                neighbors.append(cell.east)
            if neighbors:
                index = random.randint(0, len(neighbors)-1)
                neighbor = neighbors[index]
                cell.link(neighbor)


class Sidewinder(Grid):
    """Sidewinder algorithm. Start at (0,0), flip a coin and keep track of a run of cells.
        Go east if heads and continue run. Pick random cell in run if tails and go north, reset run.
        Enforce boundaries.
        bias is coin bias percentage. 100% is always east."""
    def __init__(self, row, col, bias=50):
        super().__init__(row, col)
        self.bias = bias
        
    def on(self):
        current_run = []
        for cell in self.each_cell():
            current_run.append(cell)
            coin = random.randint(0, 100)
            # print(self, coin)
            if not cell.east and cell.south:
                cell.link(cell.south)
                current_run = []
            elif not cell.south and cell.east:
                cell.link(cell.east)
                current_run = []
            elif coin <= self.bias and cell.east:
                cell.link(cell.east)
            elif coin >= self.bias:
                index = random.randint(0, len(current_run)-1)
                new_cell = current_run[index]
                current_run = []
                if new_cell.south:
                    new_cell.link(new_cell.south)