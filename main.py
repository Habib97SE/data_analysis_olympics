from olympic import Olympic
import os
from dash import html, dcc, dash
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from layout import Layout


NOC = ""


with open("chosen_country.txt", "r") as f_reader:
    NOC = f_reader.read()


df_olympic = Olympic("athlete_events.csv", NOC)

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CERULEAN],
    # makes possible for responsivity
    meta_tags=[
        dict(name="viewport", content="width=device-width, initial-scale=1.0")],
    title="Olympic Games Dashboard",
    # add favicon

)

server = app.server

app.layout = Layout().layout()


# Number of medals per Olympic year
@app.callback(
    Output("graph_medals_per_year", "figure"),
    Input("select_year", "value"),
)
def update_graph_medals_per_year(selected_year):
    fig = df_olympic.medals_per_year(selected_year)
    return fig


# Top athletes per Olympic year
@app.callback(
    Output("graph_most_successfull_athletes", "figure"),
    Input("select_year", "value"),
)
def update_graph_most_successfull_athletes(selected_year):
    fig = df_olympic.get_most_successfull_athletes(selected_year)
    return fig


# Top 5 Sports per Olympic year
@app.callback(
    Output("graph_medals_per_sport", "figure"),
    Input("select_year", "value"),
)
def update_graph_top_5_sports(selected_year):
    fig = df_olympic.get_top_5_sports(selected_year)
    return fig


@app.callback(
    Output("graph_country_medals_all_years", "figure"),
    Input("select_year", "value"),
    Input("range_slider_country_medals_all_years", "value")
)
def update_graph_country_medals_all_years(selected_year, selected_year_range):
    fig = df_olympic.medals_per_os(selected_year_range)
    return fig


@app.callback(
    Output("graph_top_medalists", "figure"),
    Input("select_year", "value"),
)
def update_graph_top_medalists(selected_year):
    fig = df_olympic.get_top_medalists()
    return fig


@app.callback(
    Output("graph_top_10_sports", "figure"),
    Input("select_year", "value"),
)
def update_graph_top_10_sports(selected_year):
    fig = df_olympic.get_top_ten_sports()
    return fig


@app.callback(
    Output("graph_gender_dist", "figure"),
    Input("select_year", "value"),
)
def update_graph_gender_dist(selected_year):
    fig = df_olympic.get_gender_distribution()
    return fig


@app.callback(
    Output("graph_top_countries", "figure"),
    Input("select_year", "value"),
)
def update_graph_top_countries(selected_year):
    fig = df_olympic.get_top_countries()
    return fig


@app.callback(
    Output("graph_gender_dist_country", "figure"),
    Input("select_year", "value"),
)
def update_gender_graph_dist_country(selected_year):
    fig = df_olympic.get_gender_by_year(selected_year)
    return fig


@app.callback(
    Output("graph_age_distribution", "figure"),
    Input("select_year", "value"),
)
def update_graph_age_distribution(selected_year):
    fig = df_olympic.get_age_distribution()
    return fig


def main():
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
