from flask import Flask 
from flask_sqlalchemy import SQLALchemy
from os import getenv


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLALchemy(app)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False)
    orders = db.relationship('Orders', backref='products')

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable= False)
    orders = db.relationship('Orders', backref="customers")

class Orders(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('Product.id'))
    customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'))

if __name__ == '__main__':
    app.run(debug==True, host = '0.0.0.0')

