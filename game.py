# game.py
import pygame
from player import Bunny
from enemy import Fox
from item import Carrot
from maze import Maze
from constants import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dungeons of Rabbit - Blue Lock Edition")
        self.clock = pygame.time.Clock()
        self.maze = Maze()
        self.bunny = Bunny(1, 1)
        self.foxes = [Fox(8, 8), Fox(5, 5)]
        self.carrot = Carrot(10, 10)
        self.running = True
        self.won = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if not self.won:
                    self.bunny.move(event.key, self.maze)

    def update(self):
        if not self.won:
            for fox in self.foxes:
                fox.chase(self.bunny, self.maze)
            
            # Verifica se pegou a cenoura
            if self.bunny.pos == self.carrot.pos:
                self.won = True
                print("🎉 Você pegou a cenoura! VITÓRIA!")

    def render(self):
        self.screen.fill((0, 0, 0))  # Preto
        
        # Desenha o labirinto
        for x in range(ROWS):
            for y in range(COLS):
                if self.maze.grid[x][y] == 1:  # Parede
                    pygame.draw.rect(self.screen, (100, 100, 100), 
                                   (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                else:  # Caminho
                    pygame.draw.rect(self.screen, (30, 30, 30), 
                                   (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        # Desenha a cenoura
        pygame.draw.rect(self.screen, self.carrot.color, 
                        (self.carrot.y * CELL_SIZE + 5, self.carrot.x * CELL_SIZE + 5, 
                         CELL_SIZE - 10, CELL_SIZE - 10))
        
        # Desenha as raposas
        for fox in self.foxes:
            pygame.draw.rect(self.screen, fox.color, 
                            (fox.y * CELL_SIZE + 5, fox.x * CELL_SIZE + 5, 
                             CELL_SIZE - 10, CELL_SIZE - 10))
        
        # Desenha o Bunny
        pygame.draw.rect(self.screen, self.bunny.color, 
                        (self.bunny.y * CELL_SIZE + 5, self.bunny.x * CELL_SIZE + 5, 
                         CELL_SIZE - 10, CELL_SIZE - 10))
        
        # Se venceu, mostra mensagem
        if self.won:
            font = pygame.font.Font(None, 74)
            text = font.render("EGOÍSTA!", True, (255, 215, 0))
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            self.screen.blit(text, text_rect)
        
        pygame.display.flip()