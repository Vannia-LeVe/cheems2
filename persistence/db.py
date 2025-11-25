import pymysql


def get_connection():
    return pymysql.connect(
        host=' 127.0.0.1',
        port= 3307,
        user='root',
        password= 'admin',
        database= 'cheems'
    )