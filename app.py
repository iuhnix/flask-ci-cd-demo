from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # 这是一个简单的文字输出，符合我们从文字内容开始学习的目标
    return 'Hello, CI/CD Pipeline is Working! This is the new version.'

if __name__ == '__main__':
    # 默认运行在 5000 端口
    app.run(host='0.0.0.0', port=5000)
