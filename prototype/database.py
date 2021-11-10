# conexión a base de datos

import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
import private

# poner a True para ver mensajes debug
DEBUG = True


class DB:
    def __init__(self, connection: MySQLConnection, cursor: MySQLCursor):
        self.connection = connection
        self.cursor = cursor

    @staticmethod
    def connect(database=None):
        connect_kwargs = {
            'host': 'localhost',
            'port': '3306',
            'user': private.DATABASE_USER_NAME,
            'password': private.DATABASE_USER_PASSWORD
        }
        if database is not None:
            connect_kwargs['database'] = database
        connection = mysql.connector.connect(**connect_kwargs)

        cursor = connection.cursor()

        return DB(connection, cursor)

    # ejecutar SQL
    def execute(self, sql, *params, multi=False):
        if not multi:
            try:
                self.cursor.execute(sql, params, multi)
            finally:
                if DEBUG:
                    self._print_last_sql_statement()
        else:
            res = self.cursor.execute(sql, params, multi)
            for _ in res:
                # la iteración realiza las operaciones
                if DEBUG:
                    self._print_last_sql_statement()

    # imprimir la última sentencia SQL ejecutada
    def _print_last_sql_statement(self):
        sql = str(self.cursor.statement)
        sql_lines = sql.split('\n')
        print('[DB QUERY]')
        for sql_line in sql_lines:
            print(f' : {sql_line}')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()


# conectarse a la BD Rentacar
def connect_rentacar_database():
    return DB.connect('rentacar')
