import pygame
import time
import random
import numpy as np

snake_speed = 12

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

# Initialise game window
pygame.display.set_caption('Heuristic Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

snake_body = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]

fruit_position = [random.randrange(1, (window_x//10)) * 10, 
				random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Score : ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)

def game_over():
	my_font = pygame.font.SysFont('times new roman', 50)
	
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (window_x/2, window_y/4)
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	time.sleep(2)
	pygame.quit()
	quit()

def ai_move(snake_position, fruit_position, direction):
    """Heuristic Function to find the direction of the fruit while considering the current direction"""
    snake_x, snake_y = snake_position
    fruit_x, fruit_y = fruit_position

    possible_moves = {
        'UP': (snake_x, snake_y - 10),
        'DOWN': (snake_x, snake_y + 10),
        'LEFT': (snake_x - 10, snake_y),
        'RIGHT': (snake_x + 10, snake_y)
    }

    # Prevent the snake from moving in the opposite direction directly
    if direction == 'UP':
        possible_moves.pop('DOWN')
    elif direction == 'DOWN':
        possible_moves.pop('UP')
    elif direction == 'LEFT':
        possible_moves.pop('RIGHT')
    elif direction == 'RIGHT':
        possible_moves.pop('LEFT')

    # Choose the move that minimizes the distance to the fruit
    best_move = direction
    min_distance = float('inf')
    for move, (new_x, new_y) in possible_moves.items():
        distance = abs(new_x - fruit_x) + abs(new_y - fruit_y)
        if distance < min_distance:
            min_distance = distance
            best_move = move

    return best_move

# Main Function
while True:
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	# Call AI to choose the next move
	change_to = ai_move(snake_position, fruit_position, direction)

	# Making sure the snake cannot move in the opposite direction instantaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10, 
						random.randrange(1, (window_y//10)) * 10]
		
	fruit_spawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, green,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(game_window, white, pygame.Rect(
		fruit_position[0], fruit_position[1], 10, 10))

	# Game Over	
	if snake_position[0] < 0 or snake_position[0] > window_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-10:
		game_over()

	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score
	show_score(1, white, 'times new roman', 20)

	pygame.display.update()

	fps.tick(snake_speed)
