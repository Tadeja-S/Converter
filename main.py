from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    value = request.form.get("unit")
    input = float(request.form.get("number"))

    if value == "km to miles":
        miles = input * 0.621371
        return render_template("result.html", value=value, input=input, result=miles)
    
    elif value == "miles to km":
        km = input * 1.60934
        return render_template("result.html", value=value, input=input, result=km)

    elif value == "C° to F°":
        F = (input * 9/5) + 32
        return render_template("result.html", value=value, input=input, result=F)

    elif value == "F° to C°":
        C = (input - 32) * 5/9
        return render_template("result.html", value=value, input=input, result=C)

    elif value == "EUR to USD":
        USD = input * 1.07729
        return render_template("result.html", value=value, input=input, result=USD)

    elif value == "USD to EUR":
        EUR = input * 0.928482
        return render_template("result.html", value=value, input=input, result=EUR)
    
    elif value == "kg to lbs":
        pounds = input * 2.20462
        return render_template("result.html", value=value, input=input, result=pounds)
    
    elif value == "lbs to kg":
        kilogrammes = input * 0.453592
        return render_template("result.html", value=value, input=input, result=kilogrammes)

if __name__ == "__main__":
    app.run(use_reloader=True)