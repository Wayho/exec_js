# 使用官方Python基础镜像
FROM python:3.8.10

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装依赖
RUN pip install -r requirements.txt

# 暴露应用端口
EXPOSE 5000

# 启动应用
CMD ["python", "app.py"]