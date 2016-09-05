from flask import render_template
from flask import flash
from flask import redirect
from . import app

import summarize

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    form = summarize.SourceTextGrabber()
    if form.validate_on_submit():
        return summarized(source_text = form.source_text.data)
    return render_template("index.html", title="Home", form=form)

@app.route('/about/', methods=['GET', 'POST'])
def about():
    return render_template("incomplete.html", title="About")

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    return render_template("incomplete.html", title="Contact")

@app.route('/summary')
def summarized(source_text=None, compression_factor=3):
    summary = summarize.get_summary(source_text, compression_factor)
    return render_template("summary.html",
            title="Summary",
            summary=summary)
