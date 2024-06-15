from flask import *


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/brand")
def brand():
    return render_template("brand.html")
@app.route("/audi")
def audi():
    return render_template("Audi.html")
@app.route("/bmw")
def bmw():
    return render_template("BMW.html")
@app.route("/skoda")
def skoda():
    return render_template("Skoda.html")
@app.route("/volkswagen")
def volkswagen():
    return render_template("Volkswagen.html")
@app.route("/mazda")
def mazda():
    return render_template("Mazda.html")
@app.route("/volvo")
def volvo():
    return render_template("Volvo.html")
@app.route("/opel")
def opel():
    return render_template("Opel.html")
@app.route("/toyota")
def toyota():
    return render_template("Toyota.html")



app.run()