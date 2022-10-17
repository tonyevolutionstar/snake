import pygame

class Command:
    def execute(self):
       
        raise NotImplemented

class Up(Command):
    def execute(self, actor):
        actor.up()

class Down(Command):
    def execute(self, actor):
        actor.down()

class Left(Command):
    def execute(self, actor):
        actor.left()

class Right(Command):
    def execute(self, actor):
        actor.right()

class InputHandler:
    command = {
        "w": Up,
        "s": Down,
        "a": Left,
        "d": Right
    }

    def handleInput(self, event, snake_direction, color):
        if color == "red":
            if event.key == pygame.K_w:
                snake_direction = (0, -1)
            elif event.key == pygame.K_s:
                snake_direction = (0, 1)
            elif event.key == pygame.K_a:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_d:
                snake_direction = (1, 0)
        elif color == "purple":
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)
        return snake_direction
