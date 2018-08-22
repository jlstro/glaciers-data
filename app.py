from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///glaciers.db'
db = SQLAlchemy(app)

class Glacier(db.Model):
  __tablename__ = 'glaciers'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  index = db.Column(db.Integer, primary_key=True)


@app.route("/")
def landing():
    glaciers = Glacier.query.all()
    return render_template("list.html", glaciers=glaciers)

@app.route("/glaciers/<index>/")
def glacier(index):
    glacier = Glacier.query.filter_by(index=index).first()
    return render_template("show.html", glacier=glacier)

if __name__ == '__main__':
  app.run(debug=True)
