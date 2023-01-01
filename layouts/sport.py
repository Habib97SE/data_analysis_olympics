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


def plot_top_medalists():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Top Medalists of all time")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_top_medalists")
            ),
            dbc.CardFooter(
                html.P(
                    "This graph shows the top medalists of all time in the olympics games.")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def plot_top_10_sports():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Top 10 Sports")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_top_10_sports")
            ),
            dbc.CardFooter(
                html.P(
                    "Top 10 sports in the olympics games based on the number of competitors and countries participating in the sport.")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def plot_gender_dist():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Gender Distribution")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_gender_dist")
            ),
            dbc.CardFooter(
                html.P(
                    "This graph shows gender distribution of athletes in the olympics games of all time.")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def plot_top_country():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Top Countries")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_top_countries")
            ),
            dbc.CardFooter(
                html.P(
                    "This graph shows countries with most medals in the olympics games of all time.")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def plot_height_weight_athletes():
    return dbc.Card(
        [
            dbc.CardHeader(
                dbc.Row(
                    [
                        dbc.Col(
                            html.H2("Height and Weight of Athletes")
                        ),
                        dbc.Col(
                            [
                                html.Label("Choose a sport:"),
                                dcc.Dropdown(
                                    id="dropdown_sport",
                                    options=df_olympic.get_unique_items(
                                        "Sport"),
                                    value="Basketball",
                                ),
                            ]

                        )
                    ]
                )

            ),
            dbc.CardBody(
                dcc.Graph(id="graph_height_weight_athletes"),
            ),
            dbc.CardFooter(
                html.P("This graph shows the height and weight of athletes")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def plot_searched_sport():
    return dbc.Row(
        [dbc.Row(
            [
                dcc.Input(
                    id="input_sport",
                    type="text",
                    placeholder="Enter sport name",
                    className="form-control",
                )
            ]
        ),
            dbc.Row(
            dbc.Card(
                [
                    dbc.CardHeader(
                        html.H2("Searched Sport")
                    ),
                    dbc.CardBody(
                        dcc.Graph(id="graph_searched_sport")
                    ),
                    dbc.CardFooter(
                        html.P("This graph shows the searched sport")
                    )
                ],
                class_name="mt-3 my-3 mx-auto",
            )
        )]
    )


def plot_age_distribution():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Age Distribution")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_age_distribution")
            ),
            dbc.CardFooter(
                html.P("This graph shows the age distribution of athletes")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


# Create sport section of the dashboard


def create_sport_section():
    return html.Div(
        [
            plot_top_medalists(),
            plot_top_10_sports(),
            dbc.Row(
                [
                    dbc.Col(
                        plot_gender_dist(),
                    ),
                    dbc.Col(
                        plot_top_country(),
                    )
                ]
            ),

            plot_height_weight_athletes(),
            plot_age_distribution(),
        ]
    )
