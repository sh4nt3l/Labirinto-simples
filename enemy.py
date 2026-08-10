# enemy.py
import random
from ai import a_star

class Fox:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 50, 50)  # Vermelho
        self.move_counter = 0
    
    def chase(self, target, maze):
        """Persegue o Bunny usando A*"""
        self.move_counter += 1
        
        # Só atualiza o caminho a cada 5 frames (economiza processamento)
        if self.move_counter % 5 == 0:
            start = (self.x, self.y)
            goal = (target.x, target.y)
            path = a_star(start, goal, maze)
            
            if path and len(path) > 1:
                next_pos = path[1]  # Próxima posição no caminho
                self.x, self.y = next_pos