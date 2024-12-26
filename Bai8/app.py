from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# TEST = 'jquery'
TEST = 'vue'

# Thông tin tài khoản mẫu (giả lập)
USERS = {
    "admin": "1",
    "user": "2"
}


@app.route('/', methods=['GET', 'POST'])
def login():
    print('method', request.method)

    if request.method == 'GET':
        # Render trang HTML cho người dùng đăng nhập
        return render_template(f'login_{TEST}.html')
    # POST =========================================

    if TEST == 'vue':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
    else:  # Jquery
        # Lấy dữ liệu từ form
        username = request.form.get('username')
        password = request.form.get('password')
    print('Check', username, password)

    # Kiểm tra thông tin tài khoản
    if username in USERS and USERS[username] == password:
        return jsonify({"success": True,
                        "message": "Đăng nhập thành công!"})
    return jsonify({"success": False,
                    "message": "Tài khoản hoặc mật khẩu không chính xác."})


if __name__ == '__main__':
    app.run(debug=True)
