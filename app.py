from olympic import Olympic
import os
from dash import html, dcc, dash
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from layouts.sport import create_sport_section
from layouts.country import create_country_section


NOC = ""


with open("chosen_country.txt", "r") as f_reader:
    NOC = f_reader.read()


df_olympic = Olympic("athlete_events.csv", NOC)

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # makes possible for responsivity
    meta_tags=[
        dict(name="viewport", content="width=device-width, initial-scale=1.0")],
    title="Olympic Games Analysis Dashboard",
    # add favicon

)

server = app.server

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Row(
                    [
                        dbc.Card(
                            [dbc.CardHeader(
                                [html.H1("Olympic Games Dashboard"),
                                 ],
                                class_name="text-center my-3 mx-auto"
                            ),

                                dbc.CardBody(
                                [

                                    html.P(
                                        "This dashboard shows the Olympic Games data for the country " + df_olympic.get_country_fullname(NOC)),
                                    html.P(
                                        "The dashboard shows general info about all the Olympic Games, the medals per year, the most successful athletes and the most successful sports."),
                                ]
                            )]
                        )
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("- General info about Olympic Games"),
                        html.P(
                            "This section shows general info about the Olympic Games, here you can find out how many medals the country has won, how many athletes have participated and how many sports have been played."),
                    ],
                    class_name="col-12 my-4 mx-auto"
                )
            ]
        ),
        create_sport_section(),

        dbc.Row(
            [

            ]
        ),
        create_country_section(),
    ]
)


# Number of medals per Olympic year
@ app.callback(
    Output("graph_medals_per_year", "figure"),
    Input("select_year", "value"),
)
def update_graph_medals_per_year(selected_year):
    fig = df_olympic.medals_per_year(selected_year)
    return fig


# Top athletes per Olympic year
@ app.callback(
    Output("graph_most_successfull_athletes", "figure"),
    Input("select_year", "value"),
)
def update_graph_most_successfull_athletes(selected_year):
    fig = df_olympic.get_most_successfull_athletes(selected_year)
    return fig


# Top 5 Sports per Olympic year
@ app.callback(
    Output("graph_medals_per_sport", "figure"),
    Input("select_year", "value"),
)
def update_graph_top_5_sports(selected_year):
    fig = df_olympic.get_top_5_sports(selected_year)
    return fig


@ app.callback(
    Output("graph_country_medals_all_years", "figure"),
    Input("select_year", "value"),
    Input("range_slider_country_medals_all_years", "value")
)
def update_graph_country_medals_all_years(selected_year, selected_year_range):
    fig = df_olympic.medals_per_os(selected_year_range)
    return fig


@ app.callback(
    Output("graph_top_medalists", "figure"),
    Input("select_year", "value"),
)
def update_graph_top_medalists(selected_year):
    fig = df_olympic.get_top_medalists()
    return fig


@ app.callback(
    Output("graph_top_10_sports", "figure"),
    Input("select_year", "value"),
)
def update_graph_top_10_sports(selected_year):
    fig = df_olympic.get_top_ten_sports()
    return fig


@ app.callback(
    Output("graph_gender_dist", "figure"),
    Input("select_year", "value"),
)
def update_graph_gender_dist(selected_year):
    fig = df_olympic.get_gender_distribution()
    return fig


@ app.callback(
    Output("graph_top_countries", "figure"),
    Input("select_year", "value"),
)
def update_graph_top_countries(selected_year):
    fig = df_olympic.get_top_countries()
    return fig


@ app.callback(
    Output("graph_gender_dist_country", "figure"),
    Input("select_year", "value"),
)
def update_gender_graph_dist_country(selected_year):
    fig = df_olympic.get_gender_by_year(selected_year)
    return fig


# sHOW AGE DISTRIBUTION
@ app.callback(
    Output("graph_age_distribution", "figure"),
    Input("select_year", "value"),
)
def update_graph_age_distribution(selected_year):
    fig = df_olympic.get_age_distribution()
    return fig


@ app.callback(
    Output("graph_height_weight_athletes", "figure"),
    Input("dropdown_sport", "value"),
)
def update_graph_height_weight_athletes(selected_sport):
    fig = df_olympic.get_athlets_height(selected_sport)
    return fig


@ app.callback(
    Output("country_age_dist", "figure"),
    Input("country_select_year_age_dist", "value"),
    Input("country_select_sport", "value")
)
def update_country_age_dist(selected_year, selected_sport):
    fig = df_olympic.get_custom_graph(columns=[
        {"column": "Year", "condition": selected_year}, {"column": "Sport", "condition": selected_sport}], chart_type="histogram", x_column="Age", y_column="", title=f"Age distribution of {selected_sport} athletes in {selected_year}")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
