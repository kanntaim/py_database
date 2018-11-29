import mysql.connector


class Database:
    def __init__(self, database, host='localhost', user='root', password=''):
        self.connection = self.login(database, host, user, password)

    def login(self, database, host='localhost', user='root', password=''):
        try:
            connection = mysql.connector.connect(host, database, user, password)
        except mysql.connector.Error as e:
            print(e.with_traceback())
        return connection

    def close_connection(self):
        self.connection.close()

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
