from grid import Grid, GridForest

class Game:
    def __init__(self, rows, cols, rules=None):
        self.grid = Grid(rows, cols)
        self.rules = rules if rules else []

    def update(self):
        new_grid = [[0 for _ in range(self.grid.cols)] for _ in range(self.grid.rows)]
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                cell = self.grid.grid[row][col]
                alive_neighbors = self.grid.alive_neighbors(row, col)

                new_cell = None
                for rule in self.rules:
                    result = rule.apply(cell, alive_neighbors)
                    if result is not None:
                        new_cell = result
                        break
                
                new_grid[row][col] = new_cell if new_cell is not None else cell

        self.grid.grid = new_grid

class GameFire:
    def __init__(self, rows, cols, rules, density):
        self.grid = GridForest(rows, cols, density)
        self.rules = rules if rules else []
        self.tree_alives = self.grid.tree_alive
        self.tree_burned = 0

    def update(self):
        new_grid = [[0 for _ in range(self.grid.cols)] for _ in range(self.grid.rows)]
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                cell = self.grid.grid[row][col]
                burn_neighbors = self.grid.burning_neighbors(row, col)

                new_cell = None
                for rule in self.rules:
                    result = rule.apply(cell, burn_neighbors)
                    if result is not None:
                        new_cell = result
                        break
                new_grid[row][col] = new_cell if new_cell is not None else cell
                if new_grid[row][col] == 2:
                    self.tree_alives -= 1
                    self.tree_burned += 1

        self.grid.grid = new_grid

    
