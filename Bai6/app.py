from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route chính trả về trang HTML
@app.route('/')
def index():
    return render_template('index.html')

# API xử lý AJAX request
@app.route('/process', methods=['POST'])
def process_data():
    # Lấy dữ liệu từ AJAX
    data = request.json.get('data')
    if data:
        response = f"Bạn vừa gửi dòng chữ: {data}"
        return jsonify({"success": True, "response": response})
    return jsonify({"success": False, "response": "No data received"})

if __name__ == '__main__':
    app.run(debug=True)
