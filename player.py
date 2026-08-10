# player.py
import pygame
from constants import *

class Bunny:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (200, 180, 255)  # Roxo do Blue Lock
    
    @property
    def pos(self):
        return (self.x, self.y)
    
    def move(self, key, maze):
        dx = dy = 0
        if key == pygame.K_UP: dy = -1
        elif key == pygame.K_DOWN: dy = 1
        elif key == pygame.K_LEFT: dx = -1
        elif key == pygame.K_RIGHT: dx = 1
        
        new_x, new_y = self.x + dx, self.y + dy
        if maze.is_walkable(new_x, new_y):
            self.x, self.y = new_x, new_y