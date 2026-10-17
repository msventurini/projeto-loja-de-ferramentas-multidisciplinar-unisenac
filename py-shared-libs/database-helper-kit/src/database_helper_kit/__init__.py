from mysql.connector import connect
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from contextlib import contextmanager


def hello() -> str:
    return "Hello from database-helper-kit!"


def get_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    return connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="",
        database="tool_repair_shop"
    )

# def get_unpooled_connection() -> MySQLConnectionAbstract:
#     return connect(
#         host="127.0.0.1",
#         port="3306",
#         user="root",
#         password="",
#         database="tool_repair_shop"
#     )

