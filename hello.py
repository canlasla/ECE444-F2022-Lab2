from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime as dt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='testtesttest'
bootstrap=Bootstrap(app)
moment=Moment(app)

class NameForms(FlaskForm):
    name=StringField('What is your name?', validators=[DataRequired()])
    submit=SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    # now=dt.now()
    # rendered_time = now.strftime("%A, %B %d, %Y %H:%M %p")
    # print(rendered_time)
    name=None
    form=NameForms()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template('index.html', current_time=dt.utcnow(), form=form, name=name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
