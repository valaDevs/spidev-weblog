from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    names = ["vala",'ali',"reza","gholi"]
    foods = ["pizza", "burger","salad","pasta","sandwich",12]
    rnd = random.choice(names)
    stuff = "this is a <b>bold</b> text "
    
    return render_template('index.html',names = rnd, stuff=stuff, foods = foods)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name = name)

# create custom error pages
@app.errorhandler(404)
def not_found(e):
    return render_template("error_404.html"), 404
    
@app.errorhandler(500)
def not_found(e):
    return render_template("error_500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)