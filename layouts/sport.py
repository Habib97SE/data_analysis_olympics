from dash import html
import dash_bootstrap_components as dbc
from layouts.layout import Layout

sport_layout = Layout()

dropdown_sport = sport_layout.create_dropdown_menu(
    "dropdown_sport", "Sport", "Basketball")


def create_sport_section():
    return html.Div(
        [
            sport_layout.create_card_header("Sport"),
            sport_layout.create_card("graph_top_medalists", "Top Medalists of all time",
                                     "This graph shows the top medalists of all time in the olympics games."),
            sport_layout.create_card("graph_top_10_sports", "Top 10 Sports",
                                     "Top 10 sports in the olympics games based on the number of competitors and countries participating in the sport."),
            dbc.Row(
                [
                    dbc.Col(
                        sport_layout.create_card("graph_gender_dist", "Gender Distribution",
                                                 "This graph shows distribution of athletes in the olympics games of all time.")
                    ),
                    dbc.Col(
                        sport_layout.create_card("graph_top_countries", "Top Countries",
                                                 "This graph shows countries with most medals in the olympics games of all time.")
                    )
                ]
            ),
            dbc.Card(
                [
                    sport_layout.create_card_header(
                        "Height and Weight ratio of Athletes"),
                    sport_layout.create_card_body(
                        "graph_height_weight_athletes", dropdown_sport),
                    sport_layout.create_card_footer(
                        "This graph shows the height and weight of athletes")
                ]
            ),
            sport_layout.create_card("graph_age_distribution", "Age Distribution",
                                     "This graph shows the age distribution of athletes"),
        ],
        className="main_section"
    )
