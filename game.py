import pygame
import random
from food import Food
from snake import Snake
from command import Command, InputHandler

WIDTH, HEIGHT = 80, 40
SCALE = 10

display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()

snake = Snake("player_red", WIDTH, HEIGHT)
snake2 = Snake("player_purple",WIDTH, HEIGHT)
snake_direction = (1, 0)
snake_direction2 = (1, 0)
food_c = Food(display,SCALE, WIDTH, HEIGHT)
food = (random.randrange(WIDTH), random.randrange(HEIGHT))
all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
all_sprites.add(snake2)
all_sprites.add(food_c)

GAME_EVENT = pygame.event.custom_type()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            i = InputHandler()
            snake_direction = i.handleInput(event, snake_direction, "red")
            snake_direction2 = i.handleInput(event, snake_direction2, "purple")
        elif event.type == GAME_EVENT:
            print(event.txt)
        
    
    display.fill("white")
    
    running, food = snake.fill_snake(running, food, GAME_EVENT, display, SCALE, "red")
    running, food = snake2.fill_snake(running, food, GAME_EVENT, display, SCALE, "purple")

    #
    food_c.draw_food(food)
    
    #all_sprites.draw(display)
    snake.snake_dir(snake_direction)
    snake2.snake_dir(snake_direction2)

    pygame.display.flip()
    clock.tick(15)

pygame.quit()