import os  
import sqlite3
from sqlite3 import Error
import subprocess


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db/database.sqlite')

def create_connection(db_file = DEFAULT_PATH):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
def show_tables_by_query(conn):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';") 
    return cur.fetchall()

def list_tables_by_shell():
    subprocess.call(["sqlite3", DEFAULT_PATH, ".table"
    ])


def show_tables_by_shell():
    subprocess.call(["sqlite3", DEFAULT_PATH, ".schema"
    ])

def select_all_columns(conn, table_name):
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM {}'.format(table_name))
 
    return cur.fetchall()


def select_all_columns_by_shell(table_name):

    process = subprocess.Popen(["sqlite3", DEFAULT_PATH, "SELECT * FROM {}".format(table_name)], stdout=subprocess.PIPE)
    return process.communicate()[0]



def show_all_columns_by_shell(table_name):
    return subprocess.call(["sqlite3", DEFAULT_PATH, ".schema {}".format(table_name)
    ])


# This is useful to choose variables
def select_column_from_table_by_shell(table_name, column_name):
    process = subprocess.Popen(["sqlite3", DEFAULT_PATH, "SELECT {} FROM {}".format(column_name, table_name)], stdout=subprocess.PIPE)
    return process.communicate()[0].decode('utf-8').strip().split('\n')


def select_limited_var_from_table_by_shell(table_name, column_name_var, column_name_limit, greater_than, under_than):
    process = subprocess.Popen(["sqlite3", DEFAULT_PATH, "SELECT {} FROM {} WHERE {} BETWEEN {} AND {}".format(column_name_var, table_name, column_name_limit, greater_than, under_than)], stdout=subprocess.PIPE)
    return process.communicate()[0].decode('utf-8').strip().split('\n')


conn = create_connection()
# with conn:
#     show_tables_by_shell()
#     print '-----------------------------------------'
#     show_all_columns_by_shell('Team')
    
#     print '-----------------------------------------'
#print select_column_from_table_by_shell('Player', 'height')

        
          

