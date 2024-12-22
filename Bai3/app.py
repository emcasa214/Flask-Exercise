# mongodb+srv://qtragxinh:GvLsgZHjCroeGn9W@cluster0.deakx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# kết nối DB

# đưa connect string vào đây
mongo_uri = "mongodb+srv://qtragxinh:GvLsgZHjCroeGn9W@cluster0.deakx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# kiểm tra xem kết nối thành công chưa
try:    
    client = MongoClient(mongo_uri)
    client.server_info()
    print("Kết nối thành công")
except Exception as e:
    print("Lỗi kết nối: " + e)
    exit()

# thêm tên project và collection vừa tạo. Nếu không tồn tại, mongo sẽ tự động tạo khi thêm document đầu tiên
db = client["DemoConnect"]
# collection ở đây tương đương với table
collection = db ["users"]

@app.route("/")
def home():
    return "Flask kết nối MongoDB thành công"

if __name__ == "__main__":
    app.run(debug=True)


