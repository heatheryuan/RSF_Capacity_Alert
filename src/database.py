import psycopg2
from psycopg2 import extensions
import config
import sys

def connect():
    conn = psycopg2.connect(
        user=config.db_user, password=config.db_pw, host=config.db_host, port=config.db_port
    )
    print('successfully connected')
    return conn

# def create_database():
#     conn = connect()
#     autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
#     conn.set_isolation_level(autocommit)
#     cursor = conn.cursor()

#     cursor.execute("""CREATE TABLE rsf_data (
#             capacity integer,
#             datetime timestamp
#             )""")

#     try:
#         cursor.execute("""CREATE TABLE rsf_data (
#             capacity INT,
#             datetime DATETIME
#             )""")
#     except:
#         print("ERROR: database already exists!")

#     cursor.close()
#     conn.close()

connect().close()