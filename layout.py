from dash import html, dcc
import dash_bootstrap_components as dbc
from olympic import Olympic

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


class Layout:
    def __init__(self) -> None:
        self.df_os = Olympic("athlete_events.csv", "CAN")

    def layout(self):
        return dbc.Container(
            [
                dbc.Card(
                    dbc.CardBody(html.H1(f"Olympic Performance for {self.df_os.get_country_fullname()}")), class_name="mt-3 header_title"
                ),
                dbc.CardBody(
                    dbc.Row(
                        [
                            html.Ul(
                                [
                                    self.df_os.short_description()
                                ]
                            )
                        ]
                    )
                )
            ]
        )
