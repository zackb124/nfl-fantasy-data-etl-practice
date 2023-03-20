import pandas as pd

url = 'https://www.pro-football-reference.com/years/2022/fantasy.htm'

# read tables from the url
tables = pd.read_html(url)

# select the table you want to convert to a data frame (in this case, the first table)
table_df = tables[0]

# print the data frame to verify that it has been created successfully

table_df.columns = table_df.columns.droplevel(level=0)

players_df = table_df.loc[:, ['Player', 'Tm','Age']]

players_df['Player'] = players_df['Player'].replace(r'[*+]', '', regex=True)

players_df = players_df[players_df['Age'].str.isdigit()]