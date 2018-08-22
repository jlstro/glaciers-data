from flask_frozen import Freezer
from app import app, Glacier

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def glacier():
    for glacier in Glacier.query.all():
        yield { 'index': glacier.index }

if __name__ == '__main__':
    freezer.freeze()
