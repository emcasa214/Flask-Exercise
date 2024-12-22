from flask import Flask, render_template, request, jsonify
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Lưu trữ mật khẩu mã hóa
stored_password_hash = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    global stored_password_hash
    data = request.get_json()
    client_hashed_password = data.get('hashed_password')

    # Hash thêm ở phía server
    if client_hashed_password:
        server_hashed_password = bcrypt.generate_password_hash(client_hashed_password).decode('utf-8')
        stored_password_hash = server_hashed_password
        return jsonify({'message': 'Password successfully registered!'})
    return jsonify({'error': 'Invalid data'}), 400

@app.route('/login', methods=['POST'])
def login():
    global stored_password_hash
    data = request.get_json()
    client_hashed_password = data.get('hashed_password')

    if stored_password_hash and client_hashed_password:
        # So sánh mật khẩu đã mã hóa
        is_valid = bcrypt.check_password_hash(stored_password_hash, client_hashed_password)
        if is_valid:
            return jsonify({'message': 'Login successful!'})
        return jsonify({'error': 'Invalid credentials'}), 401
    return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
