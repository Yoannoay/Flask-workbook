
from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Customers(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable= False)

     


if __name__ == '__main__':
    app.run(debug==True, host = '0.0.0.0')