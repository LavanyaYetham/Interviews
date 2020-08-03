#!/root/Interviews/Flask/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/')
def home():
    return "<h1>Hello World!!</h1>"
if __name__=="__main__":
    app.run(host="192.168.1.108",port="9090",debug=True)
