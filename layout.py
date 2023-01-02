from dash import html, dcc
import dash_bootstrap_components as dbc
from olympic import Olympic
from layouts.sport import create_sport_section
from layouts.country import create_country_section

COUNTRY = ""
NOC = ""


def create_dict(elements):
    new_dict = {}
    for element in elements:
        new_dict[element] = element
    return new_dict


with open("chosen_country.txt", "r") as f_reader:
    NOC = f_reader.read()


class Layout:
    def __init__(self) -> None:
        self.df_os = Olympic("athlete_events.csv", NOC)
        COUNTRY = self.df_os.get_country_fullname(NOC)

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
                                                "This dashboard shows the Olympic Games data for the country " + COUNTRY),
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
