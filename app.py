# app.py
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="PHW#84#jeor",
        database="washnwear"
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transactions')
def transactions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('transactions.html', transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    if request.method == 'POST':
        # get data from form
        data = request.form
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (column1, column2) VALUES (%s, %s)", (data['value1'], data['value2']))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('transactions'))
