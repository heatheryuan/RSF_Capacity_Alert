import psycopg2
from psycopg2 import extensions
import info

def connect():
    try:
        conn = psycopg2.connect(
            user=info.db_user, password=info.db_pw, host=info.db_host, port=info.db_port
        )
    except:
        sys.exit("ERROR: can't connect")
    return conn

def create_database(conn):
    conn = connect()
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    conn.set_isolation_level(autocommit)
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE rsf_data (
            capacity INT,
            datetime DATETIME
            )""")

    try:
        cursor.execute("""CREATE TABLE rsf_data (
            capacity INT,
            datetime DATETIME
            )""")
    except:
        print("ERROR: database already exists!")

    cursor.close()
    conn.close()