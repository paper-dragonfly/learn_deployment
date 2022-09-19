from flask import Flask, request
import psycopg2
import os
import json 

app = Flask(__name__)

# connect to database
def db_connect(autocommit:bool = False):
    # params = config(db)
    conn = psycopg2.connect('postgres://ergtrack_user:Np4qF4P1vCFWwNDrdF2Qp3xOwtmD7s4Y@dpg-cchp06irrk0c3kinmukg-a/ergtrack')
    cur = conn.cursor()
    conn.autocommit = autocommit
    return conn, cur

@app.route('/')
def simple_fn():
    return 'hello world!'

@app.route('/books')
def db():
    # page = request.args['page']
    conn, cur = db_connect()
    cur.execute("SELECT * FROM books")
    book_info = cur.fetchall()
    print(book_info, type(book_info))
    cur.close()
    conn.close()
    return json.dumps({'status_code':200, 'body':book_info}, default=str) 

# if __name__ == '__main__':
#     app.run(host='localhost', port=5010, debug=True)