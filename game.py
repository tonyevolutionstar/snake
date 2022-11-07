import os
import pygame
import random
from food import Food
from snake import Snake
from command import Command, InputHandler
from spawner import Spawner
from pygame import mixer
#print("File location using os.getcwd():", os.getcwd())

WIDTH, HEIGHT = 80, 40
SCALE = 10
snake_color1 = "red"

display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()
#pygame.init()
# Starting the mixer
mixer.init()
tunnel = pygame.mixer.Sound("Tunnel_of_Light.mp3")  
eating_sound = pygame.mixer.Sound("eating_sound.wav")  


def main():
    #pygame.mixer.music.play(loops=-1)
    tunnel.play()
    tunnel.set_volume(0.5)
    snake = Snake("player_red",display, WIDTH, HEIGHT, SCALE, snake_color1)
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
                snake_direction = i.handleInput(event, snake_direction, snake_color1)
                #snake_direction2 = i.handleInput(event, snake_direction2, "purple")
            elif event.type == GAME_EVENT:
                print(event.txt)
            
        display.fill("white")

        snake.fill_snake()
        running, s.food = snake.eat(running, s.food, eating_sound)
        snake.fill_snake()
        running, s2.food = snake.eat(running, s2.food, eating_sound)
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





