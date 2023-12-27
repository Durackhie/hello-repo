import unittest
from unittest.mock import patch, MagicMock
from main import MySQL

class TestMySQLMethods(unittest.TestCase):
    @patch('pymysql.connect')
    def setUp(self, mock_connect):
        # Мокируем метод cursor объекта connect
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        self.mysql = MySQL(host='mock_host', user='mock_user', password='mock_pass', database='mock_db')

    def test_execute_query(self):
        # Проверяем выполнение запроса
        query = "SELECT * FROM mock_table"
        self.mysql.execute_query(query)
        self.mysql.cursor.execute.assert_called_once_with(query)

    def tearDown(self):
        del self.mysql

if __name__ == '__main__':
    unittest.main()
