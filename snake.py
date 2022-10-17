import random
from pygame import *
from pygame.sprite import *


class Snake(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.body = []
        #self.body = [(40, 20), (39, 20), (38, 20)]
        self.w = WIDTH
        self.h = HEIGHT
        for i in range(3):
            x, y = (random.randrange(self.w), random.randrange(self.h))
            if (x,y) not in self.body:
                self.body.append((x,y))
           
        self.direction = (1, 0)
        self.length = 3
        

    def snake_dir(self, vector):
        x, y = vector
     
        self.body[0:0] = [(self.body[0][0] + x, self.body[0][1] + y)]
        while len(self.body) > self.length:
            self.body.pop()
    
    def fill_snake(self, running, food, GAME_EVENT, display, SCALE, color):
        for x, y in self.body:
            pygame.draw.rect(display, color, (SCALE * x, SCALE * y, SCALE, SCALE))

            if food == (x, y):
                self.length += 1
                ev = pygame.event.Event(GAME_EVENT, {'txt': "mmmnhami"})
                pygame.event.post(ev)
                print("Sent")
                ev = pygame.event.Event(GAME_EVENT, {'txt': "dammmm"})
                pygame.event.post(ev)
                food = (random.randrange(self.w), random.randrange(self.h))

            if x not in range(self.w) or y not in range(self.h):
                print("Snake crashed against the wall")
                running = False

            if self.body.count((x, y)) > 1:
                print("Snake eats self")
                running = False
        return running, food 