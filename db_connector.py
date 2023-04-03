from sqlalchemy import create_engine


class Database:

    def __init__(self, database_url):
        self.database_url = database_url
        self.engine = create_engine(self.database_url)

    def write_to_database(self, data_frame, table_name):
        data_frame.to_sql(table_name, self.engine, if_exists='replace', index=False)
