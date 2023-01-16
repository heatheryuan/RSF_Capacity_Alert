import psycopg2
from psycopg2 import extensions
import config
import sys
from datetime import datetime

def connect():
    conn = psycopg2.connect(
        user=config.db_user, password=config.db_pw, host=config.db_host, port=config.db_port
    )
    return conn

def sql_query(cmd, params=None):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(cmd, params)

    conn.commit()
    cursor.close()
    conn.close()
    

def write_data(capacity, datetime):
    insert_query = """INSERT INTO rsf_data (capacity, datetime) VALUES (%s,%s)"""
    params = (capacity, datetime)
    
    sql_query(insert_query, params)

    print('record inserted successfully')


# dt = datetime.now()
# print(dt)
# write_data(21, dt)