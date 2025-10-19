# 选用官方 Python 基础镜像，轻量且稳定
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制应用代码到容器内
COPY app.py /app/

# 暴露 Flask 默认端口
EXPOSE 5000

# 启动应用
CMD ["python", "app.py"]
