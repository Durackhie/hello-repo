import logging
from mysql_class.py import MySQL

logging.basicConfig(filename='main.log', level=logging.DEBUG)

try:
    # Создаем объект MySQL
    mysql = MySQL(host='127.0.0.1', user='Durackhie', password='Valera1124', database='DurackhieBase')

    # Примеры запросов
    create_table_query = "CREATE TABLE shop (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), price DECIMAL(10, 2))"
    add_item_query = "INSERT INTO shop (item, price) VALUES ('example_item', 10.99)"
    delete_item_query = "DELETE FROM shop WHERE item = 'example_item'"
    delete_table_query = "DROP TABLE IF EXISTS shop"

    # Выполняем запросы
    mysql.execute_query(create_table_query)
    mysql.execute_query(add_item_query)
    mysql.execute_query(delete_item_query)
    mysql.execute_query(delete_table_query)

except Exception as e:
    logging.error(f'Error in main script: {e}')

finally:
    # Убеждаемся, что соединение закрыто при завершении скрипта
    del mysql
