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
      self.food = (random.randrange(WIDTH), random.randrange(HEIGHT))

    def clone(self, display,SCALE, WIDTH, HEIGHT):
      return Food(display,SCALE, WIDTH, HEIGHT)




