from flask import Flask, request
import psycopg2
import os
import json 

app = Flask(__name__)



# connect to database
def db_connect(autocommit:bool = False):
    # params = config(db)
    conn = psycopg2.connect(
        host="postgres://ergtrack_user:Np4qF4P1vCFWwNDrdF2Qp3xOwtmD7s4Y@dpg-cchp06irrk0c3kinmukg-a/ergtrack",
        database="ergtrack",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    cur = conn.cursor()
    conn.autocommit = autocommit
    return conn, cur

@app.route('/')
def simple_fn():
    return 'hello world!'

@app.route('/books')
def db():
    page = request.args['page']
    conn, cur = db_connect()
    cur.execute("SELECT * FROM books WHERE page=%s", (f'{page}',))
    book_info = cur.fetchall()
    cur.close()
    conn.close()
    return json.dumps({'body':book_info})
