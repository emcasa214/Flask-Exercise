from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Để sử dụng session

# Route để xử lý đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lấy thông tin đăng nhập từ form
        username = request.form.get('username')
        # Lưu thông tin đăng nhập vào session
        session['logged_in_user'] = username
        # Xử lý chuyển hướng sau khi đăng nhập
        next_page = request.args.get('next')
        return redirect(next_page if next_page else url_for('dashboard'))
    return '''
        <form method="post">
            <h1> Mời Đăng Nhập Để Tiếp Tục Sử Dụng </h1>
            <label>Username: <input type="text" name="username"></label>
            <button type="submit">Login</button>
        </form>
    '''

# Route logout
@app.route('/logout')
def logout():
    # Xóa thông tin đăng nhập khỏi session
    session.pop('logged_in_user', None)
    return redirect(url_for('dashboard'))

# Decorator yêu cầu đăng nhập
def require_authentication(func):
    def wrapper(*args, **kwargs):
        if 'logged_in_user' in session:  # Kiểm tra nếu đã đăng nhập
            return func(*args, **kwargs)
        else:
            # Chuyển hướng đến trang login với tham số next
            return redirect(url_for('login', next=request.url))
    wrapper.__name__ = func.__name__
    return wrapper

# Route Dashboard (hiển thị tin tức và trạng thái đăng nhập)
@app.route('/dashboard')
def dashboard():
    news = [
        {"title": "Tin tức 1", "content": "Đông nghịt người trải nghiệm metro Bến Thành - Suối Tiên"},
        {"title": "Tin tức 2", "content": "Khánh thành khu tái định cư Làng Nủ"},
    ]
    logged_in_user = session.get('logged_in_user')  # Lấy thông tin từ session
    logout_link = f'<a href="{url_for("logout")}">Đăng xuất</a>' if logged_in_user else ''
    return f"""
        <h1>Dashboard</h1>
        <h2>Tin tức:</h2>
        <ul>
            {''.join(f'<li><strong>{item["title"]}</strong>: {item["content"]}</li>' for item in news)}
        </ul>
        <a href="{url_for('special_function')}">Xem nguồn tin tức</a>
        {logout_link}
    """


# Route chức năng đặc biệt yêu cầu đăng nhập
@app.route('/special-function')
@require_authentication
def special_function():
    logged_in_user = session.get('logged_in_user')  # Lấy thông tin từ session
    return f"""
        <h1>Chào {logged_in_user}!</h1>
        <p>Các tin tức được lấy từ VNExpress</p>
        <a href="{url_for('dashboard')}">Quay lại Dashboard</a>
    """

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
