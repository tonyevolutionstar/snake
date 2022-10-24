from food import *

class Spawner:
    def __init__(self, display, SCALE, WIDTH, HEIGHT):
        self.display = display
        self.scale = SCALE
        self.width = WIDTH
        self.height = HEIGHT
        
    
    def spawn_food(self, prototype) -> Food:
      return prototype.clone(self.display, self.scale, self.width, self.height)