# maze.py
import random
from constants import ROWS, COLS

class Maze:
    def __init__(self):
        self.grid = self.generate_maze()
    
    def generate_maze(self):
        # 0 = caminho, 1 = parede
        grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]
        
        # Começa no (1,1) e abre caminho
        stack = [(1, 1)]
        grid[1][1] = 0
        
        while stack:
            x, y = stack[-1]
            neighbors = []
            
            # Verifica vizinhos a 2 células de distância
            for dx, dy in [(-2,0), (2,0), (0,-2), (0,2)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < ROWS and 0 < ny < COLS and grid[nx][ny] == 1:
                    neighbors.append((nx, ny, dx//2, dy//2))
            
            if neighbors:
                nx, ny, mx, my = random.choice(neighbors)
                grid[x + mx][y + my] = 0  # Remove parede entre as células
                grid[nx][ny] = 0           # Abre a nova célula
                stack.append((nx, ny))
            else:
                stack.pop()
        
        # Garante que a saída está aberta
        grid[ROWS-2][COLS-1] = 0
        return grid
    
    def is_walkable(self, x, y):
        if 0 <= x < ROWS and 0 <= y < COLS:
            return self.grid[x][y] == 0
        return False