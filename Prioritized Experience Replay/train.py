from agent import Agent
from snake_game import SnakeGameAI

from utils import plot, compute_statistics, print_statistics


def train():
    scores = []
    moves = []
    mean_scores = []
    last_10_mean_scores = []
    last_100_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    
    while agent.n_games < 400:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        moves.append(game.frame_iteration)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score

            print(f'Game {agent.n_games}, Score: {score}, Record: {record}')

            scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            mean_scores.append(mean_score)
            if len(scores) >= 10:
                last_10_mean_score = sum(scores[-10:]) / 10
            else:
                last_10_mean_score = sum(scores) / len(scores)
            last_10_mean_scores.append(last_10_mean_score)

            if len(scores) >= 100:
                last_100_mean_score = sum(scores[-100:]) / 100
            else:
                last_100_mean_score = sum(scores) / len(scores)
            last_100_mean_scores.append(last_100_mean_score)

            if agent.n_games % 200 == 0:
                plot(scores, mean_scores, last_10_mean_scores, last_100_mean_scores)

    last_200_scores = scores[-200:]
    last_200_moves = moves[-200:]
    statistics = compute_statistics(last_200_scores, last_200_moves)

    print_statistics(statistics)

if __name__ == '__main__':
    train()
