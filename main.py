from scraper import FootballData
from db_connector import Database

if __name__ == '__main__':
    url = 'https://www.pro-football-reference.com/years/2022/fantasy.htm'
    database_url = 'postgresql://postgres:databasetestwsc@localhost:5432/postgres'
    table_name = 'nfl_fantasy_players'

    fd = FootballData(url)
    fd.read_table()
    fd.clean_players()

    db = Database(database_url)
    db.write_to_database(fd.players_df, table_name) hgj
