# from flask import Flask, render_template, g
# import sqlite3

# app = Flask(__name__)
# DATABASE = 'database.db'

# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(DATABASE)
#     return g.db

# @app.teardown_appcontext
# def close_db(error):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()

# def init_db():
#     db = sqlite3.connect(DATABASE)
#     cursor = db.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT
#         )
#     ''')
#     db.commit()
#     db.close()

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return "Welcome to the about section"

# if __name__ == '__main__':
#     init_db()  # initialize DB safely
#     app.run(debug=True)

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['username']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        return "User Added Successfully!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)