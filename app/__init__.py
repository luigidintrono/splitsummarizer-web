from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, Link

nav = Nav()

@nav.navigation()
def frontend_top():
    return Navbar(
        'Split Summarizer',
        Link('Home', '/index/'),
        Link('About', '/about/'),
        Link('Contact', '/contact/')
        )


app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

from app import views
nav.init_app(app)
