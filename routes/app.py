from flask import Flask
from random import randint


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page :)'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/squared/<int:number>')
def squared(number):
    return str(number*number)

@app.route('/random')
def random_num():
    random = randint(1,1000)
    return f"Your number is: {random}"








if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)