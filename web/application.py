from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "You are at the index!"
    
@app.route("/sample")
def sample():
    return "You have reached the sample page!"
    
@app.route("/search")
def search():
    return render_template('search.html')