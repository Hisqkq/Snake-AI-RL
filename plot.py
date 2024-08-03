import plotly.graph_objects as go
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
        legend=dict(x=0, y=1, traceorder='normal', bgcolor='rgba(0, 0, 0, 0)', bordercolor='rgba(0, 0, 0, 0)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title_font=dict(size=24, color='white', family='Arial'),
        xaxis=dict(showgrid=False, color='white'),
        yaxis=dict(showgrid=False, color='white')
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
        legend=dict(x=0, y=1, traceorder='normal', bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
        plot_bgcolor='rgba(255,255,255,1)',
        paper_bgcolor='rgba(255,255,255,1)',
        font=dict(color='black'),
        title_font=dict(size=24, color='black', family='Arial'),
        xaxis=dict(showgrid=True, color='black'),
        yaxis=dict(showgrid=True, color='black')
    )

    fig_light.show()