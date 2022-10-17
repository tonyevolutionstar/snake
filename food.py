import random
from pygame import *
from pygame.sprite import *

class Food(pygame.sprite.Sprite):
      def __init__(self, display, SCALE, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.SCALE = SCALE
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

      def draw_food(self, food):
        self.rect = pygame.draw.rect(self.display, "green", (self.SCALE * food[0], self.SCALE * food[1], self.SCALE, self.SCALE))