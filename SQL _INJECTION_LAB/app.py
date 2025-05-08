from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'sqli-lab'

# Initialize DB
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()

init_db()

# VULNERABLE LOGIN
@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']

        # ❌ VULNERABLE (but formatted safely to prevent crash)
        query = f"SELECT * FROM users WHERE username = '{uname}' AND password = '{passwd}'"
        print("[DEBUG] SQL Query:", query)

        try:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute(query)  # Injection may happen here
            result = c.fetchone()
            conn.close()

            if result:
                flash("✅ Logged in successfully!", "success")
            else:
                flash("❌ Invalid credentials", "danger")

        except sqlite3.OperationalError as e:
            flash(f"💥 SQL Error: {e}", "danger")
            print("SQL error:", e)

    return render_template('login.html')

# SECURE LOGIN (Uncomment to test)
"""
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']

        # ✅ SECURE QUERY (Parameterized)
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(query, (uname, passwd))
        result = c.fetchone()
        conn.close()

        if result:
            flash("✅ Logged in securely!", "success")
        else:
            flash("❌ Invalid credentials", "danger")
    return render_template('login.html')
"""

if __name__ == '__main__':
    app.run(debug=True)
