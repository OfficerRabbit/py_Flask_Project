"""
    1/29/18    CF
    Create a Flask web app to write notes to a database
        Tutorial
        Part 1
            https://medium.com/python-flask-django-tutorials-and-tips/how-to-build-a-crud-application-using-flask-python-framework-3a398b04c3c6
        Part 2
            http://tutorialsfordevs.com/tutorials/part-2-of-build-a-crud-web-app-with-flask-python-framework/
        Git Projet Repository
            https://github.com/basco-johnkevin/note-taking-app/blob/master/part1/main.py
        Flask Documentation

        SQLAlchemy Documentation
            http://docs.sqlalchemy.org/en/latest/core/type_basics.html#generic-types

    To Start App
        Start Flask_Venv Virtual Environment
           .\flask_venv\Scripts\activate.ps1
        Run Script Main.py
            python main.py
        Go to local host, port: 5000
            http://localhost:5000
"""
from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import NoteSearchForm
import os

# Start the Flask app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

# Create the Note table model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)


# Set the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Create the app route for the create note page
# This will utilize HTTP GET and POST
@app.route('/notes/create', methods=['GET', 'POST'])
def create_note():
    if request.method == 'GET':
        return render_template('create_note.html')
    else:
        title = request.form['title']
        body = request.form['body']

        note = Note(title=title, body=body)

        db.session.add(note)
        db.session.commit()

        return redirect('/notes/create')


# View all the written notes
@app.route('/notes/view', methods = ['GET'])
def get_notes():
    notes = Note.query.all()

    all_notes = []

    for note in notes:
        note_json = {"title": note.title,
                     "body": note.body}
        
        all_notes.append(note_json)
        
    return render_template('view_note.html', title = 'View Notes', all_notes = all_notes)


# This will allow you to view one post by choosing from a dropdown and searching
@app.route('/notes/search_note', methods = ['GET', 'POST'])
def view_one():
    search = NoteSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('search_note.html', form=search)

# This will show all the results from the previous search query
@app.route('/notes/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        #qry = db_session.query(Note)
        #results = qry.all()
        results = Note.query.all()
 
    if not results:
        flash('No results found!')
        return redirect('/notes/search_note')
    else:
        # display results
        return render_template('results.html', table = table)


# This will allow you to search through the list of post titles and delete one

if __name__ == "__main__":
    app.secret_key = "secret"
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug = True)

