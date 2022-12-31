import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
from olympic import Olympic

NOC = ""
with open("chosen_country.txt", "r") as f_reader:
    NOC = f_reader.read()

df_olympic = Olympic("athlete_events.csv", NOC)


def top_medalists():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Top Medalists of all time")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_top_medalists")
            ),
            dbc.CardFooter(
                html.P("This graph shows the top 10 medalists of all time")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def top_10_sports():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Top 10 Sports")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_top_10_sports")
            ),
            dbc.CardFooter(
                html.P("This graph shows the top 10 sports of all time")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def gender_dist():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Gender Distribution")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_gender_dist")
            ),
            dbc.CardFooter(
                html.P("This graph shows gender distribution of the olympics")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def top_country():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Top Countries")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_top_countries")
            ),
            dbc.CardFooter(
                html.P("This graph shows the top country of all time")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def height_weight_athletes():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Height and Weight of Athletes")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_height_weight_athletes")
            ),
            dbc.CardFooter(
                html.P("This graph shows the height and weight of athletes")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )

# Create sport section of the dashboard


def create_sport_section():
    return html.Div(
        [
            top_medalists(),
            top_10_sports(),
            dbc.Row(
                [
                    dbc.Col(
                        gender_dist(),
                    ),
                    dbc.Col(
                        top_country(),
                    )
                ]
            ),
            height_weight_athletes(),

        ]
    )
