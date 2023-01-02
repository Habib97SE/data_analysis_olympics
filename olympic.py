import pandas as pd
import plotly.express as px
import os
import hashlib


def read_data(file_name: str) -> pd.DataFrame():
    df = ""
    try:
        df = pd.read_csv(os.path.join("data", file_name))

    except:
        df = False
    finally:
        return df


class Olympic:
    def __init__(self, file_name: str, country_name: str) -> None:
        self._file_name = file_name
        self._country_name = country_name
        try:
            self._df = read_data(file_name)
            self._df_country = self._df.loc[self._df["NOC"]
                                            == self._country_name]
        except:
            print(
                "Something went wrong while filtering out data for given country, double check the country name [NOC] and try again.")

    @property
    def df_country(self) -> pd.DataFrame:
        return self._df_country

    @df_country.setter
    def df_country(self, value: pd.DataFrame) -> None:
        self._df_country = value

    @property
    def country_name(self) -> str:
        return self._country_name

    @country_name.setter
    def country_name(self, value: str) -> None:
        self._country_name = value

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        self._file_name = value

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @df.setter
    def df(self, value: pd.DataFrame) -> None:
        self._df = value

    def describe_data(self, n: int) -> dict:
        return {"info": self._df.info(), "describe": self._df.describe(), "head": self._df.head(n)}

    def get_unique_items(self, element: str) -> list:
        return self._df[element].unique()

    def get_age_summary(self) -> dict:
        """

        """
        return {
            "min": self._df["Age"].min(),
            "max": self._df["Age"].max(),
            "mean": self._df["Age"].mean(),
            "median": self._df["Age"].median(),
            "std": self._df["Age"].std()
        }

    def plot_figure(self, figure_type: str, df: pd.DataFrame, x, y):
        """
            Plot figure and data with help of dataframe _df
            - Param:
                - figure_type: str -> The chart type (bar, pie, line and histogram)
                - df: pd.DataFrame -> The dataframe
                - x: Data to plot in x-axis
                - y: Data to plot in y-axis
            - Return:
                - return the plot px.Figure else False
        """
        figure_type = figure_type.lower()
        if figure_type == "bar":
            return px.bar(df, x=x, y=y)
        if figure_type == "pie":
            return px.pie(df, x)
        if figure_type == "line":
            return px.pie(df, x=x)
        if figure_type == "histogram":
            return px.histogram(df, x=x, nbins=20)
        return False

    def get_number_of_men_women(self, df) -> pd.DataFrame:
        men = df.loc[df["Sex"] == "M"].count()
        women = df.loc[df["Sex"] == "F"].count()
        gender_dist = {
            "Sex": ["Men", "Women"],
            "Number": [men, women]
        }
        return pd.DataFrame.from_dict(gender_dist)

    def plot_sex_distribution(self):
        sex_distribution = self.get_number_of_men_women(self._df)
        sex_distribution = pd.DataFrame(sex_distribution)
        return self.plot_figure("pie", sex_distribution, "Number", "y")

    def hash_column(self, column_name: str) -> None:
        """
            Using sha256 method to hash values in given column
            - Param:
                - column_name: str -> The column to hash values in
        """
        self._df_country = self._df[column_name].apply(
            lambda x: hashlib.sha256(x.encode('utf-8')).hexdigest())

    def medals_won(self):
        df_sports = self._df_country.loc[(self._df_country["Medal"] == "Gold") | (self._df_country["Medal"] == "Silver") | (self._df_country["Medal"] == "Bronze")].drop_duplicates(
            subset=["Event", "Year"])
        fig = px.pie(df_sports, values=df_sports["Medal"].value_counts(
        ), names=df_sports["Medal"].value_counts().index, title=f"Medals won by {self._country_name}")
        fig.update_traces(
            hovertemplate="Medal: %{label}: <br>Number of medals: %{value}")
        return fig

    def top_country_sports(self):
        """
            Find and plot top ten sport for the country at OS
            - Return:
                - px.Figure : plot variable in bar type.
        """
        df_sports = self._df_country.drop_duplicates(subset=["Event", "Year"])

        df_sports_medals = dict(df_sports.groupby("Sport")["Medal"].count())

        a = sorted(df_sports_medals.items(), key=lambda x: x[1], reverse=True)

        top_ten_sports = [a[i][0] for i in range(10)]

        top_ten_sports_medals = [a[i][1] for i in range(10)]

        fig = px.bar(x=top_ten_sports, y=top_ten_sports_medals)
        fig.update_traces(hovertemplate="%{y} medals in %{x}")

        return fig

    def medals_per_os(self, selected_year_range: list):
        df = self._df_country.loc[(self._df_country["Year"] >= selected_year_range[0]) & (
            self._df_country["Year"] <= selected_year_range[1])]

        df = df.drop_duplicates(subset=["Event", "Year"])

        df = df.groupby("Year")["Medal"].count()

        # create bargroup of medals per year
        fig = px.bar(df, x=df.index, y=df.values)

        return fig

    def age_distribution_country(self):
        return self.plot_figure("histogram", self._df_country, "Age", "y")

    def medal_distribution_countries(self, sport: str):
        df_sports = self._df.loc[self._df["Sport"] == sport].groupby("NOC")[
            "Medal"].count()

        df_sports = df_sports.sort_values(ascending=False)

        fig = px.bar(df_sports.head())
        return fig

    def age_distribution(self, sport: str):
        df_sport = self._df.loc[self._df["Sport"] == sport]

        fig = px.histogram(df_sport, x="Age", nbins=25)

        return fig

    def get_country_fullname(self, noc: str) -> str:
        countries_names = pd.read_csv(os.path.join("data", "noc_regions.csv"))
        return countries_names.loc[countries_names["NOC"] == noc]["region"].values[0]

    def get_gender_by_year(self, year: int):
        df = self._df.loc[self._df["Year"] == year]
        names = ["Male", "Female"]
        fig = px.pie(df, values=df["Sex"].value_counts(
        ), names=names, title="Gender distribution")
        fig.update_traces(hovertemplate="%{label}: %{value} (%{percent})")
        return fig

    def get_unique_sorted_items(self, element: str, reverse=False) -> list:
        elements = self.get_unique_items(element)
        return sorted(elements, reverse=reverse)

    def get_data_based_year(self, year) -> pd.DataFrame:
        self._df_country = self._df.loc[self._df["NOC"] == self.country_name]
        return self._df_country.loc[self._df_country["Year"] == year]

    def get_list_all_countries(self) -> list:
        countries = []
        df_countries = pd.read_csv(os.path.join("data", "noc_regions.csv"))
        for country in df_countries["region"]:
            countries.append(country)
        return countries

    def convert_country_name_to_noc(self, country_name: str) -> str:
        df_countries = pd.read_csv(os.path.join("data", "noc_regions.csv"))
        return df_countries.loc[df_countries["region"] == country_name]["NOC"].to_list()[0]

    def update_country_df(self):
        self._df_country = self._df.loc[self._df["NOC"] == self.country_name]

        print(self._df_country["NOC"])

    def medals_per_year(self, year: int):
        """
            Find and plot medals won by the country in a given year
            - Param:
                - year: int -> The year to find medals in
            - Return:
                - px.Figure -> plot variable in bar type.
        """
        df = self._df_country.loc[self._df_country["Year"] == year]
        df = df.drop_duplicates(subset=["Event", "Year"])
        df = df.groupby("Medal")["Medal"].count()
        # sort the bars Gold > Silver > Bronze
        df = df.reindex(["Gold", "Silver", "Bronze"])
        # show gold medals in green, silver in silver and bronze in brown
        df = df.rename(index={"Gold": "Gold medals",
                       "Silver": "Silver medals", "Bronze": "Bronze medals"})
        fig = px.bar(df, color=df.index)
        return fig

    def get_most_successfull_athletes(self, year: int):
        df = self._df_country.loc[self._df_country["Year"] == year]
        df = df.groupby("Name")["Medal"].count()
        df = df.sort_values(ascending=False)
        fig = px.bar(df.head(5), color=df.head(5).index,
                     title="Most successfull athletes")
        return fig

    def get_top_5_sports(self, year: int):
        df = self._df_country.loc[self._df_country["Year"] == year]
        df = df.drop_duplicates(subset=["Event", "Year"])
        df = df.groupby("Sport")["Medal"].count()
        df = df.sort_values(ascending=False)
        fig = px.bar(df.head(5), color=df.head(5).index,
                     title="Most successfull sports")
        return fig

    def get_top_medalists(self):
        df = self._df.drop_duplicates(subset=["Event", "Year"])
        df = df.groupby("Name")["Medal"].count()
        df = df.sort_values(ascending=False)
        fig = px.bar(df.head(10), color=df.head(10).index,
                     title="Most successfull athletes")
        return fig

    def get_top_ten_sports(self):
        df = self._df.drop_duplicates(subset=["Event", "Year"])
        df = df.groupby("Sport")["Medal"].count()
        df = df.sort_values(ascending=False)
        fig = px.bar(df.head(10), color=df.head(10).index,
                     title="Most successfull sports")
        return fig

    def get_gender_distribution(self):
        names = ["Male", "Female"]
        fig = px.pie(self._df, values=self._df["Sex"].value_counts(
        ), names=names, title="Gender distribution")
        fig.update_traces(hovertemplate="%{label}: %{value} (%{percent})")
        return fig

    def get_top_countries(self):
        df = self._df.drop_duplicates(subset=["Event", "Year"])
        df = df.groupby("NOC")["Medal"].count()
        df = df.sort_values(ascending=False)
        nocs = df.head(5).index.to_list()
        for i in range(len(nocs)):
            nocs[i] = self.get_country_fullname(nocs[i])
        fig = px.bar(df.head(5), color=nocs,
                     title="Most successfull countries")
        return fig

    def get_athlets_height(self, sport: str):
        """
           Return a scatter of the height and weitght of the athletes in the all olympics for a given sport
        """
        df = self._df.loc[self._df["Sport"] == sport]
        fig = px.scatter(df, x="Weight", y="Height")
        # change x and y axis labels
        fig.update_layout(xaxis_title="Weight (KG)", yaxis_title="Height (CM)")
        # when hovering over the point, show the name, height and weight of the athlete
        fig.update_traces(
            hovertemplate="%{text}<br>Height (CM): %{y}<br>Weight (KG): %{x}", text=df["Name"])
        return fig

    def create_dropdown_year_season(self):
        years = [i for i in self.get_unique_sorted_items("Year", True)]
        years_season = {}
        for i in years:
            season = self._df.loc[self._df["Year"] == i]["Season"].to_list()[0]
            years_season[i] = season + " Olympic Game " + str(i)
        return years_season

    def get_years(self):
        return [i for i in self.get_unique_sorted_items("Year", True)]

    def get_age_distribution(self):
        """
            Return a histogram of the age distribution of the athletes in the all olmpics
        """
        fig = px.histogram(self._df, x="Age", nbins=20)
        fig.update_traces(hovertemplate="%{x}: %{y}")
        return fig

    def get_dataframe(self, column, value):
        return self._df.loc[self._df[column] == value]

    def get_age_dist_by_country(self, select_year):
        """
            Return a histogram of the age distribution of the athletes in the all olmpics
        """
        df = ""
        if select_year is not None:
            df = self._df_country.loc[self._df_country["Year"] == int(
                select_year)]
        else:
            df = self._df_country
        fig = px.histogram(df, x="Age", nbins=20)
        fig.update_traces(hovertemplate="%{x}: %{y}")
        return fig
