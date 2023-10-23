import numpy as np
import random
import os
import keyboard
import time

WIDTH = 22
HEIGHT = 12


WALL_AREA = (1, HEIGHT - 2), (1, WIDTH - 2)
FOOD_AREA = (1, HEIGHT - 2), (1, WIDTH - 2)


SNAKE_HEAD = '@'
SNAKE_BODY = '*'
FOOD = '$'
WALL = 'X'
EMPTY = ' '


screen = np.full((HEIGHT, WIDTH), EMPTY)


snake = [(2, 2), (2, 1), (2, 0)]
snake_direction = (0, 1)


food = (
    random.randint(FOOD_AREA[0][0], FOOD_AREA[0][1]),
    random.randint(FOOD_AREA[1][0], FOOD_AREA[1][1]),
)

def create_wall():
    global walls


    for j in range(0, WIDTH):
        walls.append((0, j))
        walls.append((HEIGHT - 1, j))


    for i in range(1, HEIGHT - 1):
        walls.append((i, 0))
        walls.append((i, WIDTH - 1))


walls = []
create_wall()

def draw_screen():
    global screen


    os.system('cls' if os.name == 'nt' else 'clear')


    for i in range(HEIGHT):
        for j in range(WIDTH):	
            if (i, j) == snake[0]:
                screen[i, j] = SNAKE_HEAD
            elif (i, j) in snake:
                screen[i, j] = SNAKE_BODY
            elif (i, j) == food:
                screen[i, j] = FOOD
            elif (i, j) in walls:
                screen[i, j] = WALL
            else:
                screen[i, j] = EMPTY

  
    for row in screen:
        print(' '.join(row))
    print('Score:', len(snake) - 3)

def check_eat():
    global snake, food, walls, speed

    if snake[0] == food:
        snake.append(snake[-1])
        food = (
            random.randint(FOOD_AREA[0][0], FOOD_AREA[0][1]),
            random.randint(FOOD_AREA[1][0], FOOD_AREA[1][1]),
        )
        walls.append(
            (
                random.randint(WALL_AREA[0][0], WALL_AREA[0][1]),
                random.randint(WALL_AREA[1][0], WALL_AREA[1][1]),
            )
        )


def check_game_over():
    head = snake[0]
    if (
        head in snake[1:]
        or head[0] < 1
        or head[0] >= HEIGHT - 1
        or head[1] < 1
        or head[1] >= WIDTH - 1
	or head in walls
    ):
        return True
    return False

def check_win_game():
    if len(snake)
    

while True:
    draw_screen()
    check_eat()

    if check_game_over():
        print('Game Over')
        break
    
    if (keyboard.is_pressed('up') or keyboard.is_pressed('w')) and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif (keyboard.is_pressed('down') or keyboard.is_pressed('s'))  and snake_direction != (-1, 0):
        snake_direction = (1, 0)
    elif (keyboard.is_pressed('left') or keyboard.is_pressed('a')) and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif (keyboard.is_pressed('right') or keyboard.is_pressed('d')) and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif keyboard.is_pressed('q'):
        print("LOGOUT")
        break

    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)
    snake.pop()

    time.sleep(2)
    

