from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT NOT NULL,
        password BLOB NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home Route
@app.route('/')
def home():
    return redirect(url_for('login'))

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash password
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, hashed_password)
            )

            conn.commit()
            conn.close()

            flash("Registration successful! Please login.")
            return redirect(url_for('login'))

        except sqlite3.IntegrityError:
            flash("Username already exists!")

    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            stored_password = user[3]

            if bcrypt.checkpw(
                password.encode('utf-8'),
                stored_password
            ):
                session['username'] = username
                return redirect(url_for('dashboard'))

        flash("Invalid username or password!")

    return render_template('login.html')

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        username=session['username']
    )

# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)