import random
from pygame import *
from pygame.sprite import *
from observer import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, entity, display, WIDTH, HEIGHT, SCALE, color):
        pygame.sprite.Sprite.__init__(self)
        self.obs = ScoreBoard(entity)
        self.body = []
        self.w = WIDTH
        self.h = HEIGHT
        for i in range(3):
            x, y = (random.randrange(self.w), random.randrange(self.h))
            if (x,y) not in self.body:
                self.body.append((x,y))
           
        self.direction = (1, 0)
        self.length = 3
        self.display = display
        self.scale = SCALE
        self.color = color 
        

    def snake_dir(self, vector):
        x, y = vector
        self.body[0:0] = [(self.body[0][0] + x, self.body[0][1] + y)]
        while len(self.body) > self.length:
            self.body.pop()
    
    def fill_snake(self):
        for x, y in self.body:
            pygame.draw.rect(self.display, self.color, (self.scale * x, self.scale * y, self.scale, self.scale))


    def eat(self, running, food, eating_sound):
        for x, y in self.body:
            if food == (x, y):
                self.length += 1
                eating_sound.play()
                eating_sound.set_volume(0.8)
                self.obs.add_score()
                self.obs.status("Eat food")
                food = (random.randrange(self.w), random.randrange(self.h))

            if x not in range(self.w) or y not in range(self.h):
                self.obs.status("Snake crashed against the wall")
                self.obs.finish()
                running = False

            if self.body.count((x, y)) > 1:
                self.obs.status("Snake eats self")
                self.obs.finish()
                
                running = False
        return running, food 