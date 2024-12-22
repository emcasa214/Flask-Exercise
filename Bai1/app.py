from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# api đưa thông tin cho FE
@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/hello", methods = ["POST"])
def hello():
    data = request.json
    name = data.get("name")
    return jsonify(message = f"Xin Chào {name}!")

if __name__ == "__main__":
    app.run(debug=True)
