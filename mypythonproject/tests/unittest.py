import unittest
from mysql_class import MySQL

class TestMySQLClass(unittest.TestCase):
    def setUp(self):
        # Создаем объект MySQL для тестирования
        self.mysql = MySQL(host='127.0.0.1', user='test_user', password='test_password', database='test_database')

    def test_connection(self):
        # Проверяем, установлено ли соединение
        self.assertIsNotNone(self.mysql.connection, "Connection not established")

    def test_execute_query(self):
        # Проверяем выполнение запроса
        query = "CREATE TABLE test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
        self.mysql.execute_query(query)

        # Проверяем, что таблица создана
        check_query = "SHOW TABLES LIKE 'test_table'"
        self.mysql.execute_query(check_query)
        result = self.mysql.cursor.fetchone()
        self.assertIsNotNone(result, "Table creation failed")

    def tearDown(self):
        # Удаляем тестовую таблицу и закрываем соединение после каждого теста
        drop_query = "DROP TABLE IF EXISTS test_table"
        self.mysql.execute_query(drop_query)
        del self.mysql

if __name__ == '__main__':
    unittest.main()

