import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def plot(scores, mean_scores, last_10_mean_scores, last_100_mean_scores):
    # Dark theme plot
    fig_dark = make_subplots(rows=1, cols=1)

    score_trace_dark = go.Scatter(
        x=list(range(len(scores))),
        y=scores,
        mode='lines+markers',
        name='Score',
        line=dict(color='lime', width=2),
        marker=dict(size=5)
    )

    mean_score_trace_dark = go.Scatter(
        x=list(range(len(mean_scores))),
        y=mean_scores,
        mode='lines+markers',
        name='Mean Score',
        line=dict(color='red', width=2),
        marker=dict(size=5)
    )
    
    last_10_mean_score_trace_dark = go.Scatter(
        x=list(range(len(last_10_mean_scores))),
        y=last_10_mean_scores,
        mode='lines+markers',
        name='Last 10 Mean Score',
        line=dict(color='blue', width=2),
        marker=dict(size=5)
    )

    last_100_mean_score_trace_dark = go.Scatter(
        x=list(range(len(last_100_mean_scores))),
        y=last_100_mean_scores,
        mode='lines+markers',
        name='Last 100 Mean Score',
        line=dict(color='orange', width=2),
        marker=dict(size=5)
    )

    fig_dark.add_trace(score_trace_dark, row=1, col=1)
    fig_dark.add_trace(mean_score_trace_dark, row=1, col=1)
    fig_dark.add_trace(last_10_mean_score_trace_dark, row=1, col=1)
    fig_dark.add_trace(last_100_mean_score_trace_dark, row=1, col=1)

    fig_dark.update_layout(
        title='Training Progress (Dark Theme)',
        xaxis_title='Number of Games',
        yaxis_title='Score',
        template='plotly_dark'
    )

    fig_dark.show()

    # Light theme plot
    fig_light = make_subplots(rows=1, cols=1)

    score_trace_light = go.Scatter(
        x=list(range(len(scores))),
        y=scores,
        mode='lines+markers',
        name='Score',
        line=dict(color='lime', width=2),
        marker=dict(size=5)
    )

    mean_score_trace_light = go.Scatter(
        x=list(range(len(mean_scores))),
        y=mean_scores,
        mode='lines+markers',
        name='Mean Score',
        line=dict(color='red', width=2),
        marker=dict(size=5)
    )
    
    last_10_mean_score_trace_light = go.Scatter(
        x=list(range(len(last_10_mean_scores))),
        y=last_10_mean_scores,
        mode='lines+markers',
        name='Last 10 Mean Score',
        line=dict(color='blue', width=2),
        marker=dict(size=5)
    )

    last_100_mean_score_trace_light = go.Scatter(
        x=list(range(len(last_100_mean_scores))),
        y=last_100_mean_scores,
        mode='lines+markers',
        name='Last 100 Mean Score',
        line=dict(color='orange', width=2),
        marker=dict(size=5)
    )

    fig_light.add_trace(score_trace_light, row=1, col=1)
    fig_light.add_trace(mean_score_trace_light, row=1, col=1)
    fig_light.add_trace(last_10_mean_score_trace_light, row=1, col=1)
    fig_light.add_trace(last_100_mean_score_trace_light, row=1, col=1)

    fig_light.update_layout(
        title='Training Progress (Light Theme)',
        xaxis_title='Number of Games',
        yaxis_title='Score',
        template='plotly_white'
    )

    fig_light.show()


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