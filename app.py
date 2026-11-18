
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    table = []
    number = None

    if request.method == "POST":
        number = int(request.form["number"])
        table = [number * i for i in range(1, 11)]

    return render_template("index.html", table=table, number=number)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
