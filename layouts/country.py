from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from layouts.layout import Layout


country_layout = Layout()

# the header of the country section of the website
country_section_header = dbc.Row(
    [
        dbc.Col(
            [html.H2(
                f"History of {country_layout.COUNTRY} in the olympics"),
             html.P(
                f"This is a graph that shows the history of {country_layout.COUNTRY} in the olympics"),]
        ),
        dbc.Col(

            [html.Label("Select Year",
                        htmlFor="select_year"),
             country_layout.create_dropdown_menu("select_year", "Year", 2016)
             ]
        )

    ]
)

country_age_distribution = dbc.Row([html.H2(
    f"Age Distribution of Athletes ({country_layout.COUNTRY})"),
    country_layout.create_dropdown_menu(
        "country_select_year_age_dist", "Year", 2016),
    country_layout.create_dropdown_menu(
        "country_select_sport", "Sport", "Athletics"),
]
)


medals_per_olympic_rangeslider = dcc.RangeSlider(
    id="range_slider_country_medals_all_years",
    min=1896,
    max=2016,
    step=2,
    value=[1896, 2020],
    marks={int(year): str(year)
           for year in range(1896, 2020, 8)}

)


def create_country_section():

    return html.Div(

        [
            country_layout.create_card_header(country_section_header),

            dbc.Row(
                [
                    dbc.Col(
                        country_layout.create_card("graph_medals_per_year", "Medals per year",
                                                   "This graph shows the medals per year")
                    ),
                    dbc.Col(
                        country_layout.create_card("graph_most_successfull_athletes", "Most successful athletes",
                                                   "This graph shows the most successful athletes")
                    ),
                ]
            ),
            country_layout.create_card("graph_medals_per_sport", "Medals per sport",
                                       "This graph shows the medals per sport"),
            dbc.Card(
                [
                    country_layout.create_card_header(
                        "Medals per olympic games"),
                    country_layout.create_card_body(
                        "graph_country_medals_all_years", medals_per_olympic_rangeslider),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            country_layout.create_card("graph_gender_dist_country", "Gender Distribution",
                                                       "This graph shows gender distribution.")
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        country_layout.create_card_header(
                                            country_age_distribution)
                                    ),
                                    country_layout.create_card_body(
                                        "country_age_dist"),
                                    country_layout.create_card_footer(
                                        "This graph shows the age distribution of athletes in the country"),
                                ]
                            )
                        ],
                        className="mt-3 my-3 mx-auto",
                    )
                ]
            ),

        ],
        className="main_section",
    )
