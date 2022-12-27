from olympic import Olympic
import os
import dash
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from layout import Layout

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # makes possible for responsivity
    meta_tags=[
        dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)

app.layout = Layout().layout()


def main():
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
