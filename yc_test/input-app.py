from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to the home page of the test application'

# this asked for input in the terminal
# @app.route('/input_maybe')
# def input_maybe():
    # age = int(input("What is your age?"))
    # return f"Are you {age} years old?"



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
