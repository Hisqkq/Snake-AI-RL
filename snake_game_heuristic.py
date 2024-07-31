import pygame
import time
import random
import numpy as np

snake_speed = 12

window_width = 720
window_height = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Snake Game with Heuristic AI')
game_display = pygame.display.set_mode((window_width, window_height))

fps = pygame.time.Clock()

snake_head_position = [100, 50]

snake_body_positions = [[100, 50],
                        [90, 50],
                        [80, 50],
                        [70, 50]
                        ]

food_position = [random.randrange(1, (window_width // 10)) * 10,
                 random.randrange(1, (window_height // 10)) * 10]

food_spawn = True

current_direction = 'RIGHT'
next_direction = current_direction

game_score = 0

def display_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(game_score), True, color)
    score_rect = score_surface.get_rect()
    game_display.blit(score_surface, score_rect)

def end_game():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(game_score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_width / 2, window_height / 4)
    game_display.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def ai_decision(snake_position, food_position, direction):
    """Heuristic Function to find the direction of the food while considering the current direction"""
    snake_x, snake_y = snake_position
    food_x, food_y = food_position

    possible_moves = {
        'UP': (snake_x, snake_y - 10),
        'DOWN': (snake_x, snake_y + 10),
        'LEFT': (snake_x - 10, snake_y),
        'RIGHT': (snake_x + 10, snake_y)
    }

    if direction == 'UP':
        possible_moves.pop('DOWN')
    elif direction == 'DOWN':
        possible_moves.pop('UP')
    elif direction == 'LEFT':
        possible_moves.pop('RIGHT')
    elif direction == 'RIGHT':
        possible_moves.pop('LEFT')

    best_move = direction
    min_distance = float('inf')
    for move, (new_x, new_y) in possible_moves.items():
        distance = abs(new_x - food_x) + abs(new_y - food_y)
        if distance < min_distance:
            min_distance = distance
            best_move = move

    return best_move

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_direction = 'UP'
            if event.key == pygame.K_DOWN:
                next_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                next_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                next_direction = 'RIGHT'

    next_direction = ai_decision(snake_head_position, food_position, current_direction)

    if next_direction == 'UP' and current_direction != 'DOWN':
        current_direction = 'UP'
    if next_direction == 'DOWN' and current_direction != 'UP':
        current_direction = 'DOWN'
    if next_direction == 'LEFT' and current_direction != 'RIGHT':
        current_direction = 'LEFT'
    if next_direction == 'RIGHT' and current_direction != 'LEFT':
        current_direction = 'RIGHT'

    if current_direction == 'UP':
        snake_head_position[1] -= 10
    if current_direction == 'DOWN':
        snake_head_position[1] += 10
    if current_direction == 'LEFT':
        snake_head_position[0] -= 10
    if current_direction == 'RIGHT':
        snake_head_position[0] += 10

    snake_body_positions.insert(0, list(snake_head_position))
    if snake_head_position[0] == food_position[0] and snake_head_position[1] == food_position[1]:
        game_score += 10
        food_spawn = False
    else:
        snake_body_positions.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (window_width // 10)) * 10,
                         random.randrange(1, (window_height // 10)) * 10]

    food_spawn = True
    game_display.fill(black)

    for pos in snake_body_positions:
        pygame.draw.rect(game_display, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_display, white, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    if snake_head_position[0] < 0 or snake_head_position[0] > window_width - 10:
        end_game()
    if snake_head_position[1] < 0 or snake_head_position[1] > window_height - 10:
        end_game()

    for block in snake_body_positions[1:]:
        if snake_head_position[0] == block[0] and snake_head_position[1] == block[1]:
            end_game()

    display_score(1, white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(snake_speed)
