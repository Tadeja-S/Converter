from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    km = float(request.form.get("km"))
    miles = km * 0.62

    return render_template("result.html", km=km, miles=miles) # Templatu sporočimo, katere spremenljivke bomo uporabili na tej html strani!

if __name__ == "__main__":
    app.run(use_reloader=True)