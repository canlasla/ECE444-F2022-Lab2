from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime as dt

app = Flask(__name__)
bootstrap=Bootstrap(app)
moment=Moment(app)

@app.route('/')
def index():
    # now=dt.now()
    # rendered_time = now.strftime("%A, %B %d, %Y %H:%M %p")
    # print(rendered_time)
    return render_template('index.html', current_time=dt.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

