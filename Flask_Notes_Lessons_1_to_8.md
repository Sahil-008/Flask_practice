# Flask Notes (Lessons 1--8)

## Introduction

Flask is a lightweight Python web framework used to build websites, web
applications, and REST APIs.

A web framework handles requests, responses, routing, and server
management so you can focus on your application.

------------------------------------------------------------------------

# Lesson 1 -- Flask

-   Flask is a Python web framework.
-   It is lightweight and beginner-friendly.
-   Common uses:
    -   Websites
    -   REST APIs
    -   Machine Learning deployment

------------------------------------------------------------------------

# Lesson 2 -- First Flask App

``` python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
```

### Keywords

-   `from` → import specific objects.
-   `import` → bring external code.
-   `Flask` → class used to create the app.
-   `app` → Flask application object.
-   `__name__` → tells Flask where the application is located.
-   `@app.route()` → connects a URL with a function.
-   `def` → defines a function.
-   `return` → sends a response.
-   `app.run()` → starts the server.
-   `debug=True` → auto reload + detailed errors.

------------------------------------------------------------------------

# Lesson 3 -- Routing

Routes map URLs to functions.

Dynamic route:

``` python
@app.route("/user/<name>")
```

------------------------------------------------------------------------

# Lesson 4 -- Templates

Store HTML inside a folder named `templates`.

Render HTML:

``` python
return render_template("index.html")
```

Variables:

``` html
{{ name }}
```

------------------------------------------------------------------------

# Lesson 5 -- Jinja2

Variables:

``` html
{{ variable }}
```

Logic:

``` html
{% if condition %}
{% endif %}
```

Loops:

``` html
{% for item in items %}
{{ item }}
{% endfor %}
```

------------------------------------------------------------------------

# Lesson 6 -- Forms

Read form values:

``` python
request.form["username"]
```

GET displays pages.

POST sends data.

------------------------------------------------------------------------

# Lesson 7 -- Static Files

Store CSS, JavaScript and images inside `static`.

Example:

``` html
{{ url_for('static', filename='style.css') }}
```

------------------------------------------------------------------------

# Lesson 8 -- SQLite

``` python
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
```

-   `conn` = database connection
-   `cursor` = executes SQL
-   `execute()` = runs SQL command
-   `commit()` = permanently save
-   `close()` = close connection

------------------------------------------------------------------------

# Current Project

Completed: - Flask setup - Routing - Templates - Jinja2 - Forms - Static
files - SQLite setup - Insert user into database

Next: Display users, update, delete and build CRUD.
