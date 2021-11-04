from flask import Flask, render_template, redirect, request
from model_users import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("read(all).html", users=User.get_all())

@app.route('/users/new')
def create_user():
    return render_template("create.html")

@app.route('/users/create', methods = ['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug = True)