import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np
import time

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple("Point", "x, y")

pygame.display.init()
pygame.font.init()

font = pygame.font.Font(pygame.font.get_default_font(), 25)

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

# Game settings
BLOCK_SIZE = 20
SPEED = 15

class SnakeGameAI:
    def __init__(self, width=640, height=480):
        self.w = width
        self.h = height
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake AI")
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self._move()
        self.snake.insert(0, self.head)

        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            return -10, True, self.score

        reward = 0
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

        self._update_ui()
        self.clock.tick(SPEED)
        return reward, False, self.score

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    def _move(self):
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        next_direction = ai_decision(self.head, self.food, self.direction)

        if next_direction == 'UP' and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        if next_direction == 'DOWN' and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        if next_direction == 'LEFT' and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        if next_direction == 'RIGHT' and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

    def _update_ui(self):
        self.display.fill(BLACK)
        for pt in self.snake[1:]:
            pygame.draw.rect(self.display, GREEN, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, ORANGE, pygame.Rect(self.head.x, self.head.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

def ai_decision(snake_position, food_position, direction):
    """Heuristic Function to find the direction of the food while considering the current direction"""
    snake_x, snake_y = snake_position.x, snake_position.y
    food_x, food_y = food_position.x, food_position.y

    possible_moves = {
        'UP': (snake_x, snake_y - BLOCK_SIZE),
        'DOWN': (snake_x, snake_y + BLOCK_SIZE),
        'LEFT': (snake_x - BLOCK_SIZE, snake_y),
        'RIGHT': (snake_x + BLOCK_SIZE, snake_y)
    }

    if direction == Direction.UP:
        possible_moves.pop('DOWN')
    elif direction == Direction.DOWN:
        possible_moves.pop('UP')
    elif direction == Direction.LEFT:
        possible_moves.pop('RIGHT')
    elif direction == Direction.RIGHT:
        possible_moves.pop('LEFT')

    best_move = direction
    min_distance = float('inf')
    for move, (new_x, new_y) in possible_moves.items():
        distance = abs(new_x - food_x) + abs(new_y - food_y)
        if distance < min_distance:
            min_distance = distance
            best_move = move

    return best_move

if __name__ == "__main__":
    game = SnakeGameAI()
    while True:
        reward, done, score = game.play_step()
        if done:
            break
        time.sleep(0.1)
