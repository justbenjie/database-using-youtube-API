import csv
import pandas as pd
import mysql.connector as mysql
import mysql.connector.errors as errors
df = pd.read_csv('channel_info.csv', index_col=0)
username = "root"
password = "philippnesterov3"
host = "localhost"
database = "channel_info"


def connect_to_db(username, password, host, database):
    try:
        conn = mysql.connect(user=username, password=password, host=host, database=database)
    except errors.OperationalError as e:
        raise e
    else:
        print('Connected')
    return conn


conn = connect_to_db(username, password, host, database)