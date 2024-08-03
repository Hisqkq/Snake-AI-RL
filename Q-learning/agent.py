import numpy as np
import random
from collections import deque
from snake_game import Direction, Point, SnakeGameAI

class QLearningAgent:
    def __init__(self, actions):
        self.actions = actions
        self.step_size = 0.3
        self.gamma = 0.9
        self.epsilon = 1.0
        self.epsilon_decay_rate = 0.95
        self.min_epsilon = 0.001
        self.q_table = dict()

    def get_state(self, game):
        head = game.snake[0]
        point_l = Point(head.x - 20, head.y)
        point_r = Point(head.x + 20, head.y)
        point_u = Point(head.x, head.y - 20)
        point_d = Point(head.x, head.y + 20)

        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            game.food.x < game.head.x,
            game.food.x > game.head.x,
            game.food.y < game.head.y,
            game.food.y > game.head.y,
            game.is_collision(point_l),
            game.is_collision(point_r),
            game.is_collision(point_u),
            game.is_collision(point_d)
        ]

        return tuple(state)

    def act(self, state):
        if state not in self.q_table:
            self.q_table[state] = {a: 0.0 for a in self.actions}

        if np.random.rand() <= self.epsilon:
            return random.choice(self.actions)

        q_values = self.q_table[state]
        max_q = max(q_values.values())
        actions_with_max_q = [a for a, q in q_values.items() if q == max_q]

        return random.choice(actions_with_max_q)

    def update_q_value(self, state, reward, action, next_state, done):
        if next_state not in self.q_table:
            self.q_table[next_state] = {a: 0.0 for a in self.actions}

        max_q_next = max(self.q_table[next_state].values())
        self.q_table[state][action] += self.step_size * (
            reward + self.gamma * max_q_next * (1.0 - done) - self.q_table[state][action]
        )

    def decay_epsilon(self):
        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay_rate)
