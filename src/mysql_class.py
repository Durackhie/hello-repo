import logging
import pymysql

class MySQL:
    def __init__(self, host, user, password, database):
        logging.basicConfig(filename='mysql_class.log', level=logging.DEBUG)
        logging.info('Инициализация подключения к MySQL')
        try:
            self.connection = pymysql.connect(
                host='127.0.0.1',
                user='Durackhie',
                password='Valera1124',
                database='DurackhieBase'
            )
            self.cursor = self.connection.cursor()
            logging.info('Соединение с MySQL установлено')
        except Exception as e:
            logging.error(f'Ошибка инициализации подключения к MySQL: {e}')

    def execute_query(self, query):
        logging.info(f'Выполнение запроса: {query}')
        try:
            self.cursor.execute(query)  # Убедимся, что метод execute вызывается
            self.connection.commit()
            logging.info('Запрос успешно выполнен')
        except Exception as e:
            logging.error(f'Ошибка выполнения запроса: {e}')

    def __del__(self):
        try:
            self.connection.close()
            logging.info('Соединение с MySQL закрыто')
        except Exception as e:
            logging.error(f'Ошибка закрытия соединения с MySQL: {e}')
