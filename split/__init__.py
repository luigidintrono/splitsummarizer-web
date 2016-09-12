from flask import Flask

application = Flask(__name__)
application.config.from_object('config')

from split import views

if __name__ == '__main__':
    application.run(host='0.0.0.0')
