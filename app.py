from flask import Flask
app = Flask(__name__)
from utils import execute_query

@app.route('/names/')
def firstName():
    query = 'SELECT DISTINCT FirstName FROM customers'
    return str(execute_query(query))

@app.route('/tracks/')
def tracks_number():
    query = 'SELECT COUNT(TrackId) FROM tracks'
    return str(execute_query(query))

@app.route('/tracks_sec/')
def tracks_sec():
    query = 'SELECT Name, Milliseconds/1000 FROM tracks'
    return str(execute_query(query))

if __name__ == '__main__':
    app.run()
