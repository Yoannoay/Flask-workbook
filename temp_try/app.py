from flask import Flask, render_template

app = Flask(__name__)

@app.route('/names')
def names():
    names = ["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template('names.html', name_a=names)


if __name__ == "__main__":
      app.run(debug=True, host='0.0.0.0')