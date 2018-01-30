"""
    1/29/18    CF
    Create a Flask web app to write notes to a database
        Tutorial: Part 1
            https://medium.com/python-flask-django-tutorials-and-tips/how-to-build-a-crud-application-using-flask-python-framework-3a398b04c3c6
        Git Projet Repository
            https://github.com/basco-johnkevin/note-taking-app/blob/master/part1/main.py
        Flask Documentation

        SQLAlchemy Documentation
            http://docs.sqlalchemy.org/en/latest/core/type_basics.html#generic-types
"""
# Import modules
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os

# Declare and create the Flask and SQLAlchemy app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

# Create a Note model to CRUD operations
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route("/")
def home():
    return render_template("home.html")
