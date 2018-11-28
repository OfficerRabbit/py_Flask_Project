from flask_table import Table, Col
 
class Results(Table):
    id = Col('Id', show=False)
    title = Col('Title')
    body = Col('Body')
