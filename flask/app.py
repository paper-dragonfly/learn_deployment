from flask import Flask, request
import psycopg2
import os
import json 
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

def get_connection_str():
    env = os.getenv('ENVIRONMENT')   
    if env == 'production':
        conn_str = os.getenv('INTERNAL_CONNECTION_STR') 
    elif env == 'dev':
        conn_str = os.getenv('EXTERNAL_CONNECTION_STR') 
    return conn_str 

CONN_STR = get_connection_str()

# connect to database
def db_connect(autocommit:bool = False):
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    conn.autocommit = autocommit
    return conn, cur

@app.route('/')
def simple_fn():
    return 'hello world!'

@app.route('/books')
def db():
    conn, cur = db_connect()
    cur.execute("SELECT * FROM books")
    book_info = cur.fetchall()
    print(book_info, type(book_info))
    cur.close()
    conn.close()
    return json.dumps({'status_code':200, 'body':book_info}, default=str) 

# if __name__ == '__main__':
#     app.run(host='localhost', port=5010, debug=True)