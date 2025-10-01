
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def connect_db():
    connection = mysql.connector.connect(
            host = 'db',
            user = 'root',
            password = '1234',
            database = 'test_db'
        )
    return connection

@app.route('/')
def index():
    return render_template("index.html", title = "My App")


@app.route('/hello')
def hello_world():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT 'This is a simple Flask App!'")
    result = cursor.fetchone()
    connection.close()
    return str(result[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0')

