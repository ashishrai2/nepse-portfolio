from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    portfolio = [
        {"symbol": "NABIL", "shares": 100, "price": 520},
        {"symbol": "NRIC", "shares": 50, "price": 980},
        {"symbol": "NIFRA", "shares": 200, "price": 210},
    ]
    return render_template("index.html", portfolio=portfolio)

if __name__ == "__main__":
    app.run(debug=True)
