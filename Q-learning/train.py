from agent import QLearningAgent
from snake_game import SnakeGameAI
from utils import plot, compute_statistics, print_statistics

def train():
    actions = [0, 1, 2]  
    agent = QLearningAgent(actions)
    game = SnakeGameAI()

    scores = []
    moves_list = []  # Liste pour enregistrer les mouvements
    mean_scores = []
    last_10_mean_scores = []
    last_100_mean_scores = []
    total_score = 0

    for game_number in range(1, 1001):
        game.reset()  
        state = agent.get_state(game)
        score = 0
        moves = 0

        while True:
            action = agent.act(state)
            final_move = [0, 0, 0]
            final_move[action] = 1

            reward, done, score = game.play_step(final_move)
            next_state = agent.get_state(game)

            agent.update_q_value(state, reward, action, next_state, done)

            state = next_state
            moves += 1

            if done:
                agent.decay_epsilon()
                scores.append(score)
                moves_list.append(moves)  # Enregistrer les mouvements de cette partie
                total_score += score
                mean_score = total_score / game_number
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

                print(f'Game {game_number}, Score: {score}, Moves: {moves}, Average Score: {mean_score:.2f}')

                break

    plot(scores, mean_scores, last_10_mean_scores, last_100_mean_scores)

    last_200_scores = scores[-200:]
    last_200_moves = moves_list[-200:]  # Utiliser les mouvements enregistrés
    statistics = compute_statistics(last_200_scores, last_200_moves)

    print_statistics(statistics)

if __name__ == "__main__":
    train()
