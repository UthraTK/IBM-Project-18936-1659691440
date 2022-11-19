from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def about():
    return render_template("about.html")
from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/mitigation")
def mitigation():
    return render_template("mitigation.html")

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/register")
def register():
    return render_template("register.html")



if _name_ == "_main_":
    app.run(host='127.0.0.4',port=5500,debug=True)
