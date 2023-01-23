from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['Secret_password'] = 'D33znuts'

class BookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    description = StringField('Description')
    release_date = IntegerField('Release date', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template('index.html')
