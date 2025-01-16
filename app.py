from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 存储参与者的 IP 地址
participants = set()
total_participants = 0

@app.route('/get_involved', methods=['GET'])
def get_involved():
    global total_participants
    user_ip = request.remote_addr  # 获取用户的 IP 地址

    if user_ip in participants:
        return jsonify({"message": "You already involved!"}), 400  # 返回错误信息
    else:
        participants.add(user_ip)  # 添加 IP 地址到参与者集合
        total_participants += 1  # 增加总参与人数
        return jsonify({"message": "Thank you for getting involved!", "total": total_participants}), 200

if __name__ == '__main__':
    app.run(debug=True)