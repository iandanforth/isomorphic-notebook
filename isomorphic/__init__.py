import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot as plot

def run(in_colab):
    env_string = "Google colab" if in_colab else "local Jupyter"
    print("You're up and running in a {} environment!".format(env_string))

    # Plotly demo
    init_notebook_mode()

    layout = go.Layout(
        autosize=False,
        width=500,
        height=500,
        xaxis=dict(
            range=[1, 4]
        ),
    )

    check_trace = go.Scatter(
        x = [1.3, 2, 3.5],
        y = [5, 1, 10],
        mode="lines",
        line = dict(
            color = ('rgb(65, 168, 52)'),
            width = 12,
        )
    )

    fig = go.Figure(data=[check_trace], layout=layout)
    plot(fig)
