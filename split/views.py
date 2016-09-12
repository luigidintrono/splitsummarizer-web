from flask import render_template
from flask import request

from split import application
import summarize

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_text = request.form['source_text']
        summary = summarize.get_summary(source_text)
        return render_template("index.html", title="Summary", summary=summary)
    return render_template("index.html", title="Home")
