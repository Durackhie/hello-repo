import unittest
from unittest.mock import patch
from mysql_class import MySQL
from main import create_table_query, add_item_query, delete_item_query, delete_table_query

class TestMySQLQueries(unittest.TestCase):
    def setUp(self):
        self.mysql = MySQL(host='127.0.0.1', user='Durackhie', password='Valera1124', database='DurackhieBase')

    def tearDown(self):
        del self.mysql

    def test_create_table_query(self):
        with patch.object(self.mysql, 'execute_query') as mock_execute_query:
            self.mysql.execute_query(create_table_query)
            mock_execute_query.assert_called_once_with(create_table_query)

    def test_add_item_query(self):
        with patch.object(self.mysql, 'execute_query') as mock_execute_query:
            self.mysql.execute_query(add_item_query)
            mock_execute_query.assert_called_once_with(add_item_query)

    def test_delete_item_query(self):
        with patch.object(self.mysql, 'execute_query') as mock_execute_query:
            self.mysql.execute_query(delete_item_query)
            mock_execute_query.assert_called_once_with(delete_item_query)

    def test_delete_table_query(self):
        with patch.object(self.mysql, 'execute_query') as mock_execute_query:
            self.mysql.execute_query(delete_table_query)
            mock_execute_query.assert_called_once_with(delete_table_query)

if __name__ == '__main__':
    unittest.main()

