# item.py
class Carrot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 200, 0)  # Amarelo
        self.collected = False
    
    @property
    def pos(self):
        return (self.x, self.y)