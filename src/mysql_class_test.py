import unittest
from unittest.mock import MagicMock
from mysql_class import MySQL

class TestMySQLMethods(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = MagicMock()
        self.mock_connection = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor

        self.mysql = MySQL(host='127.0.0.1', user='Durackhie', password='Valera1124', database='DurackhieBase')
        self.mysql.connection = self.mock_connection

    def test_execute_query_success(self):
        query = "SELECT * FROM table_name"
        self.mysql.execute_query(query)
        self.mock_cursor.execute.assert_called_once_with(query)
        self.mock_connection.commit.assert_called_once()

    def test_execute_query_failure(self):
        query = "SELECT * FROM table_name"
        self.mock_cursor.execute.side_effect = Exception("Моделируемое исключение")
        
        with self.assertRaises(Exception) as context:
            self.mysql.execute_query(query)

        self.assertEqual(str(context.exception), "Моделируемое исключение")

    def tearDown(self):
        del self.mysql

if __name__ == '__main__':
    unittest.main()
