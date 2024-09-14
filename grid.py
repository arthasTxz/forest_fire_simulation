import random
import numpy as np

class Grid:
    def __init__(self, rows, cols, init_state):
        self.rows = rows
        self.cols = cols
        if init_state:
            self.grid = init_state
        else:
            self.grid = [[0] * self.cols for _ in range(self.rows)]
    
    def is_cell_in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def is_alive(self, row, col):
        return self.grid[row][col] == 1 if self.is_cell_in_bounds(row, col) else 0
    
    def alive_neighbors(self, row, col):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return sum(
            [self.is_alive(row + off_y, col + off_x) for off_y, off_x in offsets]
        )
    
    def __str__(self):
        rows = ["  ".join(map(str, row)) for row in self.grid]
        return "\n".join(rows)
    

class GridForest:
    def __init__(self, rows, cols, density=0.5,init_state=None):
        self.rows = rows
        self.cols = cols
        self.density = density
        self.tree_alive = 0
        if init_state:
            self.grid = init_state
        else:
            self.grid = self.generate_init_state()
    
    def is_cell_in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def is_burning(self, row, col):
        return self.grid[row][col] == 2 if self.is_cell_in_bounds(row, col) else 0
    
    def burning_neighbors(self, row, col):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return sum(
            [self.is_burning(row + off_y, col + off_x) for off_y, off_x in offsets]
        )
    
    def generate_init_state(self):
        # grid = [[0]*self.cols] * self.rows
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         if self.density > random.random():
        #             grid[i][j] = 1
        #             self.tree_alive += 1
        # print(grid)
        grid = np.random.choice([0, 1], size=(self.rows, self.cols), p=[1-self.density, self.density])
        self.tree_alive = np.sum(grid == 1)
        return grid
        # return grid
        # return [[1 if self.density > random.random() else 0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def __str__(self):
        rows = ["  ".join(map(str, row)) for row in self.grid]
        return "\n".join(rows)