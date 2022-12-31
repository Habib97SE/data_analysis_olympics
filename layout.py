from dash import html, dcc
import dash_bootstrap_components as dbc
from olympic import Olympic

from layouts.sport import create_sport_section
from layouts.country import create_country_section

COUNTRY = ""


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
                create_sport_section(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Label("Select Year",
                                           htmlFor="select_year"),
                                dcc.Dropdown(
                                    id="select_year",
                                    options=[
                                        {"label": value, "value": key}
                                        for key, value in self.df_os.create_dropdown_year_season().items()
                                    ],
                                    value=2016,
                                ),
                            ],
                            className="col-3",
                        )
                    ]
                ),
                create_country_section(),
            ]
        )
