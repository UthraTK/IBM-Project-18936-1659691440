from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['upload']
      f.save(secure_filename(f.filename))
      x=image.img_to_array(f)
      x=np.expand_dims(x,axis=0)
      predicted=np.argmax(model.predict(x))
      Prediction_category=['Cyclone','Earthquake','Flood']
      Prediction_category[predicted]
      a=predicted
      return redirect(url_for("report"))

@app.route("/report")
def report():
    return render_template("report.html")





    

#@app.route("/upload", methods=["POST"])
#def process_image():
 #   file = request.files['image']
    # Read the image via file.stream
    


@app.route("/mitigation")
def mitigation():
    return render_template("mitigation.html")

@app.route("/statistics")
def statistics():
    return render_template("statistics.html")

@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host='127.0.0.7',port=8070,debug=True)
