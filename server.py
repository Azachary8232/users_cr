from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("read(all).html")

if __name__ == "__main__":
    app.run(debug = True)