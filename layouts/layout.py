from dash import html, dcc
import dash_bootstrap_components as dbc
from olympic import Olympic


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
        self._df_os = Olympic("athlete_events.csv", NOC)
        self._COUNTRY = self.df_os.get_country_fullname(NOC)

    @property
    def df_os(self):
        return self._df_os

    @df_os.setter
    def df_os(self, df_os):
        self._df_os = df_os

    @property
    def COUNTRY(self):
        return self._COUNTRY

    @COUNTRY.setter
    def COUNTRY(self, COUNTRY):
        self._COUNTRY = COUNTRY

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

    def create_dropdown_menu_data(self, column: str) -> dict:
        """
        Creates a dictionary with the unique values of a column as keys and values.
        - params: 
            - param column: The column to get the unique values from.
        - return: 
            - A dictionary with the unique values of a column as keys and values.
        """
        return {key: key for key in self._df_os.get_unique_items(column)}

    def create_dropdown_menu(self, id: str, column: str, value: str) -> dcc.Dropdown:
        """
        Creates a dropdown menu with the unique values of a column as options.
        - params:
            - param id: The id of the dropdown menu.
            - param column: The column to get the unique values from.
            - param value: The default value of the dropdown menu.
        - return:
            - A dropdown menu with the unique values of a column as options.
        """
        return dcc.Dropdown(
            id=id,
            options=[
                {"label": key, "value": value}
                for key, value in self.create_dropdown_menu_data(column).items()
            ],
            value=value,
        )

    def create_card_header(self, title: str) -> dbc.CardHeader:
        """
        Creates a card header with a title.
        - params:
            - param title: The title of the card header.
        - return:
            - A card header with a title.
        """
        return dbc.CardHeader(
            html.H2(title)
        )

    def create_card_header(self, header_content: dbc.Row) -> dbc.CardHeader:
        """
        Creates a card header with a row.
        - params:
            - param header_content: The content of the card header.
        - return:
            - A card header with a row of HTML content.
        """
        return dbc.CardHeader(
            header_content
        )

    def create_card_body(self, id: str, additional_content=None) -> dbc.CardBody:
        """
        Creates a card body with a graph and additional content.
        - params:
            - param id: The id of the graph.
            - param additional_content: Additional content to add to the card body.
        - return:
            - A card body with a graph and additional content.
        """
        if additional_content is not None:
            return dbc.CardBody(
                [dcc.Graph(id=id), additional_content]
            )
        return dbc.CardBody(
            dcc.Graph(id=id)
        )

    def create_card_footer(self, footer_text: str) -> dbc.CardFooter:
        """
        Creates a card footer with a text.
        - params:
            - param footer_text: The text of the card footer.
        - return:
            - A card footer with a text.
        """
        return dbc.CardFooter(
            html.P(footer_text)
        )

    def create_card(self, id: str, title: str, footer_text: str) -> dbc.Card:
        """
        Creates a card with a header, body and footer.
        - params:
            - param id: The id of the graph.
            - param title: The title of the card.
            - param footer_text: The text of the card footer.
        - return:
            - A card with a header, body and footer.
        """
        return dbc.Card(
            [
                self.create_card_header(title),
                self.create_card_body(id),
                self.create_card_footer(footer_text)
            ]
        )
