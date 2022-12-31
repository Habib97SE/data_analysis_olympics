from dash import html, dcc
import dash_bootstrap_components as dbc
from olympic import Olympic

# import sport layout from "./layout/sport.py"
from layouts.sport import create_sport_section

COUNTRY = ""

card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)


def create_dict(elements):
    new_dict = {}
    for element in elements:
        new_dict[element] = element
    return new_dict


NOC = ""

with open("chosen_country.txt", "r") as f_reader:
    NOC = f_reader.read()


class Layout:
    def __init__(self) -> None:
        self.df_os = Olympic("athlete_events.csv", NOC)

    def create_plot_layout(self, id, title, footer_text):
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

    def layout(self):
        return dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardHeader(
                                            html.H2(
                                                "Olympic Statistics"
                                            )
                                        ),
                                        dbc.CardBody(
                                            [
                                                html.P(
                                                    "This is a web application that shows statistics about the olympic games. The data is from 1896 to 2016. The data is from Kaggle and can be found here: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results"
                                                ),
                                            ]
                                        ),
                                    ]),
                            ]
                        ),
                    ],
                    className="mb-3 mx-auto my-3"
                ),
                dbc.Row(

                    html.Div(
                        children=[
                            html.Div(className="col-xl-3 col-lg-4 col-md-6 col-sm-12",
                                     children=[
                                         # add label to dropdown
                                         html.Label(
                                             "Select a year:", className="form-label"),

                                         # Create a dropdown menu for year
                                         dcc.Dropdown(
                                             id="select_year",
                                             options=[
                                                 {"label": year,
                                                  "value": year}
                                                 for year in self.df_os.get_unique_sorted_items("Year", True)
                                             ],
                                             value=self.df_os.get_unique_sorted_items("Year", True)[
                                                 0],
                                             clearable=False,
                                             className="form-control",
                                             placeholder="Select a year",
                                         ),

                                     ]
                                     ),

                        ]),
                    className="mb-3 mx-auto my-3",
                ),
                dbc.Row(
                    [
                        self.create_plot_layout("graph_medals_per_year", "Medals per year",
                                                "This graph shows the medals per year"),
                        self.create_plot_layout("graph_most_successfull_athletes", "Most successful athletes",
                                                "This graph shows the most successful athletes"),
                    ],
                    className="mb-3 mx-auto my-3",

                ),
                dbc.Row([
                        self.create_plot_layout(
                            "graph_medals_per_sport", "Medals per sport", "This graph shows the medals per sport"),
                        ],
                        className="mb-3 mx-auto my-3",
                        ),
                dbc.Row(
                    dbc.CardHeader(
                        [
                            html.H2("History of Canada in the olympics"),
                            html.P(
                                "This is a graph that shows the history of Canada in the olympics"),
                        ]
                    ),
                    className="mb-3 mx-auto my-3",
                ),
                dbc.Row([
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                html.H2("Medals per year for Canada")
                            ),
                            dbc.CardBody(
                                dcc.Graph(id="graph_canada_medals_all_years")
                            ),
                            dbc.CardFooter(
                                html.P(
                                    "This graph shows the medals per year for Canada")
                            )
                        ]
                    )
                ]),
                dbc.Row(
                    [
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    html.H2("Medals per sport for Canada")
                                ),
                                dbc.CardBody(
                                    create_sport_section()
                                ),
                                dbc.CardFooter(
                                    html.P(
                                        "This graph shows the medals per sport for Canada")
                                )
                            ]
                        )
                    ]),
            ])
