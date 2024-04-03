
import plotly.graph_objects as go

def generate_radar_chart(categories, values):
    fig = go.Figure(data=go.Scatterpolar(
    r=values,
    theta=categories,
    fill='toself'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0,10]
        ),
    ),
    showlegend=False
    )

    return fig