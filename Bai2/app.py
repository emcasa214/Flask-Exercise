from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# File để lưu trữ ghi chú
NOTES_FILE = "notes.json"

# Đọc ghi chú từ file JSON
def read_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Ghi ghi chú vào file JSON
def write_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "GET":
        return jsonify(read_notes())
    elif request.method == "POST":
        data = request.json
        notes = read_notes()
        notes.append(data)
        write_notes(notes)
        return jsonify({"message": "Note added!"}), 201

if __name__ == "__main__":
    app.run(debug=True)