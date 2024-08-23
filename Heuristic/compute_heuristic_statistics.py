import numpy as np
import time
from snake_game_heuristic import SnakeGameAI

def print_statistics(statistics):
    print("\nStatistics for the last 200 games:")
    print(f"Average Score: {statistics['Average Score']:.2f}")
    print(f"Variance: {statistics['Variance']:.2f}")
    print(f"Standard Deviation: {statistics['Standard Deviation']:.2f}")
    print(f"Maximum Score: {statistics['Maximum Score']}")
    print(f"Minimum Score: {statistics['Minimum Score']}")
    print(f"Average Moves: {statistics['Average Moves']:.2f}")

def compute_statistics(scores, moves):
    average_score = np.mean(scores)
    variance = np.var(scores)
    std_deviation = np.std(scores)
    max_score = np.max(scores)
    min_score = np.min(scores)
    average_moves = np.mean(moves)
    
    return {
        "Average Score": average_score,
        "Variance": variance,
        "Standard Deviation": std_deviation,
        "Maximum Score": max_score,
        "Minimum Score": min_score,
        "Average Moves": average_moves
    }

def run_heuristic_games(num_games=200):
    """Run the heuristic Snake Game for a number of games and compute statistics
    
    Args:
        num_games (int): The number of games to play
    """
    scores = []
    moves = []

    for _ in range(num_games):
        game = SnakeGameAI()
        game.reset()
        game_moves = 0

        while True:
            reward, done, score = game.play_step()
            game_moves += 1
            if done:
                break
            time.sleep(0.0001) 
        
        scores.append(score)
        moves.append(game_moves)

    statistics = compute_statistics(scores, moves)
    print_statistics(statistics)

if __name__ == "__main__":
    run_heuristic_games(200)
