from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import random

app = Flask(__name__)

app.config["SECRET_KEY"] = "supersecret001"

# Create Form Class
class NamerForm(FlaskForm):
    name = StringField("What is your name : " , validators=[DataRequired()])
    submit = SubmitField("submit")
    
    
@app.route('/')
def index():
    names = ["vala",'ali',"reza","gholi"]
    foods = ["pizza", "burger","salad","pasta","sandwich",12]
    rnd = random.choice(names)
    flash("Welcome to our website ! ")
    stuff = "this is a <b>bold</b> text "
    
    return render_template('index.html',names = rnd, stuff=stuff, foods = foods)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name = name)

# create custom error pages
@app.errorhandler(404)
def not_found(e):
    return render_template("error_404.html"), 404
    
@app.errorhandler(500)
def not_found(e):
    return render_template("error_500.html"), 500

@app.route("/name",methods=["GET","POST"])
def name():
    
    name = None 
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash(" Form submitted Successfuly ! ")
        
    return render_template('name.html', name = name , form = form)

if __name__ == "__main__":
    app.run(debug=True)