import pygame
import random

WIDTH, HEIGHT = 80, 40
SCALE = 10

display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()

snake_body = [(40, 20), (39, 20), (38, 20)]
snake_direction = (1, 0)
snake_length = 3
food = (random.randrange(WIDTH), random.randrange(HEIGHT))

GAME_EVENT = pygame.event.custom_type()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)
        elif event.type == GAME_EVENT:
            print(event.txt)
            

    display.fill("white")

    pygame.draw.rect(display, "green", (SCALE * food[0], SCALE * food[1], SCALE, SCALE))

    for x, y in snake_body:
        pygame.draw.rect(display, "red", (SCALE * x, SCALE * y, SCALE, SCALE))

        if food == (x, y):
            snake_length += 1
            ev = pygame.event.Event(GAME_EVENT, {'txt': "mmmnhami"})
            pygame.event.post(ev)
            print("Sent")
            ev = pygame.event.Event(GAME_EVENT, {'txt': "dammmm"})
            pygame.event.post(ev)
            food = (random.randrange(WIDTH), random.randrange(HEIGHT))

        if x not in range(WIDTH) or y not in range(HEIGHT):
            print("Snake crashed against the wall")
            running = False

        if snake_body.count((x, y)) > 1:
            print("Snake eats self")
            running = False

    # move snake
    snake_body[0:0] = [
        (snake_body[0][0] + snake_direction[0], snake_body[0][1] + snake_direction[1])
    ]
    while len(snake_body) > snake_length:
        snake_body.pop()

    # update window
    pygame.display.flip()
    clock.tick(15)

pygame.quit()
