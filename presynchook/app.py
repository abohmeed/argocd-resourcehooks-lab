from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Use environment variables to configure the MySQL connection
MYSQL_HOST = os.getenv('MYSQL_HOST', 'default-hostname')
MYSQL_USER = os.getenv('MYSQL_USER', 'default-user')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'default-password')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'default-database')

@app.route('/')
def hello_world():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM sample_table')
    row_count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return f'Row count in sample_table: {row_count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)