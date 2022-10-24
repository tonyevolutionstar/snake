import pygame
import random
from food import Food
from snake import Snake
from command import Command, InputHandler
from spawner import Spawner

WIDTH, HEIGHT = 80, 40
SCALE = 10

display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()

def main():

    snake = Snake("player_red", WIDTH, HEIGHT)
    #snake2 = Snake("player_purple",WIDTH, HEIGHT)
    snake_direction = (1, 0)
    #snake_direction2 = (1, 0)
    spawner = Spawner(display,SCALE, WIDTH, HEIGHT)
    spawner2 = Spawner(display,SCALE, WIDTH, HEIGHT)
    
    food_c = Food(display,SCALE, WIDTH, HEIGHT)
    s = spawner.spawn_food(food_c)
    s2 = spawner2.spawn_food(food_c)
    
    if s == s2 or s2 == s:
        s = spawner.spawn_food(food_c)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(snake)
    #all_sprites.add(snake2)
    all_sprites.add(s)
    all_sprites.add(s2)

    GAME_EVENT = pygame.event.custom_type()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                i = InputHandler()
                snake_direction = i.handleInput(event, snake_direction, "red")
                #snake_direction2 = i.handleInput(event, snake_direction2, "purple")
            elif event.type == GAME_EVENT:
                print(event.txt)
            
        display.fill("white")
        
        running, s.food = snake.fill_snake(running, s.food, GAME_EVENT, display, SCALE, "red")
        running, s2.food = snake.fill_snake(running, s2.food, GAME_EVENT, display, SCALE, "red")

        #running, food = snake2.fill_snake(running, food, GAME_EVENT, display, SCALE, "purple")
        draw_food(s.food)
        draw_food(s2.food)
        #all_sprites.draw(display)
        snake.snake_dir(snake_direction)
        #snake2.snake_dir(snake_direction2)

        pygame.display.flip()
        clock.tick(15)

    pygame.quit()

def draw_food(food):
    pygame.draw.rect(display, "green", (SCALE * food[0], SCALE * food[1], SCALE, SCALE))


if __name__ == '__main__':  
   main()





