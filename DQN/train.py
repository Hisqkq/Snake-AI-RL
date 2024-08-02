import plotly.graph_objs as go
from plotly.subplots import make_subplots
from agent import Agent
from snake_game import SnakeGameAI

def plot(scores, mean_scores, last_10_mean_scores):
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

    fig.add_trace(score_trace, row=1, col=1)
    fig.add_trace(mean_score_trace, row=1, col=1)
    fig.add_trace(last_10_mean_score_trace, row=1, col=1)

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

def train():
    scores = []
    mean_scores = []
    last_10_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()

    while agent.n_games < 1000:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

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

            if agent.n_games % 100 == 0:
                plot(scores, mean_scores, last_10_mean_scores)

if __name__ == '__main__':
    train()
