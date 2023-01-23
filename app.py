from flask import Flask, render_template, url_for, redirect, request
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

@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        description = form.description.data
        release_date = form.release_date.data
        
        return redirect(url_for('books'))
    return render_template('add_book.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search_book():
    form = BookForm()
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        search_result = []
        for book in books:
            if title.lower() in book['title'].lower() or author.lower() in book['author'].lower():
                search_result.append(book)
        return render_template('search.html', form=form, books=search_result)
    return render_template('search.html', form=form)

