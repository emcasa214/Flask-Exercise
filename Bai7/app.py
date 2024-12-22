from flask import Flask, render_template, request, redirect, session, flash
import pyotp
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Đặt secret key cho session
app.config['SESSION_TYPE'] = 'filesystem'

# Cấu hình email (sử dụng Gmail trong ví dụ này)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'qtragxinh@gmail.com'  
app.config['MAIL_PASSWORD'] = 'pzfv umvy ebzt uphe'    

mail = Mail(app)

# Tạo tài khoản người dùng giả định
users = {
    "testuser": {
        "password": "password123",  # Mật khẩu
        "email": "qtragxinh@gmail.com",  # Email để gửi OTP
    }
}

# Route trang đăng nhập
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Kiểm tra thông tin đăng nhập
        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username  # Lưu thông tin người dùng vào session

            # Tạo OTP và gửi email
            session['otp'] = pyotp.TOTP(pyotp.random_base32()).now()
            send_otp_email(user['email'], session['otp'])

            return redirect('/verify')
        else:
            flash('Invalid username or password!')
    return render_template('login.html')

# Route xác minh OTP
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if 'username' not in session:
        return redirect('/')

    if request.method == 'POST':
        otp = request.form.get('otp')

        # Kiểm tra OTP
        if otp == session.get('otp'):
            return redirect('/success')
        else:
            flash('Invalid OTP!')
    return render_template('verify.html')

# Route thành công sau khi xác thực
@app.route('/success')
def success():
    if 'username' not in session:
        return redirect('/')
    return render_template('success.html')

# Hàm gửi email OTP
def send_otp_email(recipient_email, otp):
    msg = Message('Your OTP Code', sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])
    msg.body = f'Your OTP code is: {otp}'
    mail.send(msg)

# Route logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
