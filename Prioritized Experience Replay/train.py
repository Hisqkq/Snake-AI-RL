import plotly.graph_objs as go
from plotly.subplots import make_subplots
from agent import Agent
from snake_game import SnakeGameAI
import pandas as pd
import numpy as np

def plot(scores, mean_scores, last_10_mean_scores, last_100_mean_scores):
    fig = make_subplots(rows=1, cols=1)

    score_trace = go.Scatter(
        x=list(range(len(scores))),
        y=scores,
        mode='lines+markers',
        name='Score',
        line=dict(color='lime', width=2),
        marker=dict(size=5)
    )

    mean_score_trace = go.Scatter(
        x=list(range(len(mean_scores))),
        y=mean_scores,
        mode='lines+markers',
        name='Mean Score',
        line=dict(color='red', width=2),
        marker=dict(size=5)
    )
    
    last_10_mean_score_trace = go.Scatter(
        x=list(range(len(last_10_mean_scores))),
        y=last_10_mean_scores,
        mode='lines+markers',
        name='Last 10 Mean Score',
        line=dict(color='blue', width=2),
        marker=dict(size=5)
    )

    last_100_mean_score_trace = go.Scatter(
        x=list(range(len(last_100_mean_scores))),
        y=last_100_mean_scores,
        mode='lines+markers',
        name='Last 100 Mean Score',
        line=dict(color='orange', width=2),
        marker=dict(size=5)
    )

    fig.add_trace(score_trace, row=1, col=1)
    fig.add_trace(mean_score_trace, row=1, col=1)
    fig.add_trace(last_10_mean_score_trace, row=1, col=1)
    fig.add_trace(last_100_mean_score_trace, row=1, col=1)

    fig.update_layout(
        title='Training Progress',
        xaxis_title='Number of Games',
        yaxis_title='Score',
        legend=dict(x=0, y=1, traceorder='normal', bgcolor='rgba(0, 0, 0, 0)', bordercolor='rgba(0, 0, 0, 0)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title_font=dict(size=24, color='white', family='Arial'),
        xaxis=dict(showgrid=False, color='white'),
        yaxis=dict(showgrid=False, color='white')
    )

    fig.show()

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

def print_statistics(statistics):
    print("\nStatistics for the last 200 games:")
    print(f"Average Score: {statistics['Average Score']:.2f}")
    print(f"Variance: {statistics['Variance']:.2f}")
    print(f"Standard Deviation: {statistics['Standard Deviation']:.2f}")
    print(f"Maximum Score: {statistics['Maximum Score']}")
    print(f"Minimum Score: {statistics['Minimum Score']}")
    print(f"Average Moves: {statistics['Average Moves']:.2f}")

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
