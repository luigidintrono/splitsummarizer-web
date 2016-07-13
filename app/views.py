from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Home")

@app.route('/summary')
def summary():
    summary = {
    "text": 
    """
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    }
    return render_template("summary.html", title="Summary", summary=summary)
