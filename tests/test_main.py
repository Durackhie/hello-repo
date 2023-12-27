import unittest
from unittest.mock import patch
from main import MySQL

class TestMySQLMethods(unittest.TestCase):
    def setUp(self):
        self.mysql = MySQL(host='mock_host', user='mock_user', password='mock_pass', database='mock_db')

    @patch.object(MySQL, 'execute_query')
    def test_execute_query(self, mock_execute_query):
        # Мокируем объект cursor внутри метода execute_query
        mock_cursor = self.mysql.connection.cursor.return_value
        self.mysql.execute_query("SELECT * FROM mock_table")
        mock_cursor.execute.assert_called_once_with("SELECT * FROM mock_table")

    def tearDown(self):
        del self.mysql

if __name__ == '__main__':
    unittest.main()
