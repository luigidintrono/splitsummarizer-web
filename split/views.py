from flask import abort
from flask import render_template
from flask import request

from split import application
import summarize

@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title="Home")

@application.route('/summarize/', methods=['GET', 'POST'])
def summarizer():
    if request.method == 'POST':
        source_text = request.form['source_text']
        summary = summarize.get_summary(source_text)
        return render_template("summary.html",
                                title="Summary",
                                summary=summary)
    return render_template("summary_form.html", title="Summarize")

@application.route('/about/')
def about():
    return render_template("index.html", title="About")

@application.route('/contact/')
def contact():
    return render_template("contact.html", title="Contact us")
