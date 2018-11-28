from wtforms import Form, StringField, SelectField

# Create the Note search class
class NoteSearchForm(Form):
    choices = [('Title', 'Title'),
               ('Body', 'Body')]

    select = SelectField('Search for Note Title:', choices = choices)
    search = StringField('')
