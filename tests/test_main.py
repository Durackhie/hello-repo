import unittest
from unittest.mock import MagicMock
from main import MySQL

class TestMySQLMethods(unittest.TestCase):
    def setUp(self):
        # Мокируем объект MySQL для тестирования без реального подключения к базе данных
        self.mysql = MySQL(host='mock_host', user='mock_user', password='mock_pass', database='mock_db')

    def test_execute_query(self):
        # Проверяем выполнение запроса
        query = "SELECT * FROM mock_table"
        self.mysql.cursor.execute = MagicMock(return_value=True)
        self.mysql.execute_query(query)
        self.mysql.cursor.execute.assert_called_once_with(query)

    # Добавьте другие тесты по необходимости

if __name__ == '__main__':
    unittest.main()

