from scraper import  *
from sqlalchemy import create_engine


dbname='postgres'
user='postgres'
password='databasetestwsc'
host='147.235.202.125'
port = '5432'
conn_str = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

# specify the name of the table you want to create in the database
table_name = 'nfl_players'

# create a SQLAlchemy engine
engine = create_engine(conn_str)

# write the DataFrame to the database as a new table
players_df.to_sql(table_name, engine, index=False, if_exists='replace')

# close the database connection
engine.dispose()

