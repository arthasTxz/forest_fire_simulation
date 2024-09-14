import random

class BurnTreeToBurned:
    @staticmethod
    def apply(cell, live_neighbors):
        if cell == 2:
            return 3
        return None
    
class TreeBurnRule:
    @staticmethod
    def apply(cell, neighbors):
        if cell == 1 and neighbors > 0:
            return 2
        return None
    
class BurnedTreeToTree:
    @staticmethod
    def apply(cell, neighbors):
        if cell == 3 and 0.95 < random.random():
            return 1
        return None
    
# def generate_init_state(rows, cols):
#         return [[1 if 0.8 > random.random() else 0 for _ in range(cols)] for _ in range(rows)]
        
# print(generate_init_state(10, 10))