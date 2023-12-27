import logging
import pymysql

class MySQL:
    def __init__(self, host, user, password, database):
        logging.basicConfig(filename='mysql_class.log', level=logging.DEBUG)
        logging.info('Initializing MySQL connection')
        try:
            self.connection = pymysql.connect(
                host='127.0.0.1',
                user='Durackhie',
                password='Valera1124',
                database='DurackhieBase'
            )
            self.cursor = self.connection.cursor()
            logging.info('MySQL connection established')
        except Exception as e:
            logging.error(f'Error initializing MySQL connection: {e}')

    def execute_query(self, query):
        logging.info(f'Executing query: {query}')
        try:
            self.cursor.execute(query)
            self.connection.commit()
            logging.info('Query executed successfully')
        except Exception as e:
            logging.error(f'Error executing query: {e}')

    def __del__(self):
        try:
            self.connection.close()
            logging.info('MySQL connection closed')
        except Exception as e:
            logging.error(f'Error closing MySQL connection: {e}')
