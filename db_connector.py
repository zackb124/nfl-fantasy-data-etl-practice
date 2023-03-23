from scraper import *
from sqlalchemy import create_engine

# create a connection to the PostgreSQL database
engine = create_engine('postgresql://postgres:databasetestwsc@localhost:5432/postgres')

# build a new table on PostgreSQL
engine.execute("CREATE TABLE nfl_fantasy_players (Player TEXT, Tm TEXT,Age INT, Datetime TIMESTAMP)")

# write the DataFrame to the PostgreSQL table
players_df.to_sql("nfl_fantasy_players", engine, if_exists="replace", index=False)