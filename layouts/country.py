import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
from olympic import Olympic

NOC = ""
COUNTRY = ""
with open("chosen_country.txt", "r") as f_reader:
    NOC = f_reader.read()

df_olympic = Olympic("athlete_events.csv", NOC)

COUNTRY = df_olympic.get_country_fullname(NOC)


def create_year_dict(years: list):
    return {year: str(year) for year in years}


def create_plot_layout(id, title, footer_text):
    return dbc.Col(
        [
            dbc.Card(
                [dbc.CardHeader(
                    html.H2(title)
                ),
                    dbc.CardBody(
                    dcc.Graph(id=id)
                ),
                    dbc.CardFooter(
                    html.P(footer_text)
                )],
            ),
        ])


def plot_medals_per_year():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Medals per year")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_medals_per_year")
            ),
            dbc.CardFooter(
                html.P("This graph shows the medals per year")
            ),
        ]
    )


def plot_most_successfull_athletes():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Most successful athletes")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_most_successfull_athletes")
            ),
            dbc.CardFooter(
                html.P(
                    "This graph shows the most successful athletes")
            ),
        ]
    )


def plot_medals_per_sport():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Medals per sport")
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_medals_per_sport")
            ),
            dbc.CardFooter(
                html.P("This graph shows the medals per sport")
            ),
        ]
    )


def plot_medals_all_olympics():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Medlas per olympics")
            ),
            dbc.CardBody(
                [
                    dcc.Graph(id="graph_country_medals_all_years"),
                    # add RangeSlider here
                    dcc.RangeSlider(
                        id="range_slider_country_medals_all_years",
                        min=1896,
                        max=2016,
                        step=2,
                        value=[1896, 2020],
                        marks={int(year): str(year)
                               for year in range(1896, 2020, 8)}

                    )
                ]
            ),
            dbc.CardFooter(
                html.P("This graph shows the top 10 sports of all time")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def plot_country_gender_distribution():
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H2("Gender Distribution"),
            ),
            dbc.CardBody(
                dcc.Graph(id="graph_gender_dist_country")
            ),
            dbc.CardFooter(
                html.P(
                    "This graph shows gender distribution in the country for the year")
            )
        ],
        class_name="mt-3 my-3 mx-auto",
    )


def create_country_section():
    return html.Div(
        [
            dbc.CardHeader(
                dbc.Row(
                    [
                        dbc.Col(
                            [html.H2(
                                f"History of {COUNTRY} in the olympics"),
                             html.P(
                                f"This is a graph that shows the history of {COUNTRY} in the olympics"),]
                        ),
                        dbc.Col(

                            [html.Label("Select Year",
                                        htmlFor="select_year"),
                             dcc.Dropdown(
                                id="select_year",
                                options=[
                                    {"label": value, "value": key}
                                    for key, value in df_olympic.create_dropdown_year_season().items()
                                ],
                                value=2016,
                            ),]

                        )

                    ]
                ),
            ),

            dbc.Row(
                [
                    dbc.Col(
                        plot_medals_per_year()
                    ),
                    dbc.Col(
                        plot_most_successfull_athletes()
                    ),
                ]
            ),
            plot_medals_per_sport(),
            plot_medals_all_olympics(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            plot_country_gender_distribution()
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        [html.H2(
                                            f"Age Distribution of Athletes ({COUNTRY})"),
                                            dcc.Dropdown(
                                                id="select_age_dist_year",
                                                options=[
                                                    {"label": value, "value": key} for key, value in df_olympic.create_dropdown_year_season().items()
                                                ],
                                        )
                                        ]
                                    ),
                                    dbc.CardBody(
                                        dcc.Graph(id="country_age_dist")
                                    ),
                                    dbc.CardFooter(
                                        html.P(
                                            "This graph shows the age distribution of athletes in the country")
                                    ),
                                ]
                            )
                        ],
                        className="mt-3 my-3 mx-auto",
                    )
                ]
            ),

        ]
    )
