import pandas as pd
import datetime as dt


class FootballData:

    def __init__(self, url):
        self.url = url
        self.table_df = None
        self.players_df = None

    def read_table(self):
        tables = pd.read_html(self.url)
        self.table_df = tables[0]
        self.table_df.columns = self.table_df.columns.droplevel(level=0)

    def clean_players(self):
        self.players_df = (
            self.table_df
            .loc[:, ['Rk', 'Player', 'Tm', 'Age']]
            .assign(Player=lambda x: x['Player'].replace(r'[*+]', '', regex=True))
            .loc[lambda x: x['Age'].str.isdigit()]
            .assign(Rk=lambda x: x['Rk'].astype(int),
                    Age=lambda x: x['Age'].astype(int),
                    Timestamp=pd.to_datetime(dt.datetime.now()))
        )
