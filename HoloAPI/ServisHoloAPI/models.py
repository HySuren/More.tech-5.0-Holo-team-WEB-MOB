import psycopg2
from read import Conf
from psycopg2 import Error
from django.http import HttpResponse

conf = Conf()

class DatabaseInterface:
    def create_db(self):
        pass

class PostgresConnectExecute(DatabaseInterface):
    def __init__(self, db_name, user, password):
        self.db_name = db_name
        self.user = user
        self.password = password

    def create_db(self):
        connect = None
        try:
            connect = psycopg2.connect(f"dbname={self.db_name} user={self.user} password={self.password}")
            print('Connect complide...')
            cursor = connect.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS "User" ("id" SERIAL PRIMARY KEY,'
                '"login" varchar(155) NOT NULL,'
                '"email" varchar(155) NOT NULL, '
                '"password" varchar(155) NOT NULL);')
            connect.commit()
            cursor.close()
        except (Exception, Error) as error:
            return HttpResponse(content=error,content_type='application/json')
        finally:
            if connect:
                connect.close()



db = PostgresConnectExecute(conf.NAME, conf.USER, conf.PASSWORD)
db.create_db()
