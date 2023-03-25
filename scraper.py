import pandas as pd
import datetime as dt

url = 'https://www.pro-football-reference.com/years/2022/fantasy.htm'

# read tables from the url
tables = pd.read_html(url)

# select the table you want to convert to a data frame (in this case, the first table)
table_df = tables[0]

# print the data frame to verify that it has been created successfully
table_df.columns = table_df.columns.droplevel(level=0)

players_df = (
    table_df
    .loc[:, ['Rk','Player', 'Tm','Age']]
    .assign(Player=lambda x: x['Player'].replace(r'[*+]', '', regex=True))
    .loc[lambda x: x['Age'].str.isdigit()]
    .assign(Rk=lambda x: x['Rk'].astype(int),
            Age=lambda x: x['Age'].astype(int),
            Timestamp=pd.to_datetime(dt.datetime.now()))
)