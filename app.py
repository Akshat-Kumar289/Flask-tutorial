from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "hello akshat"


if __name__ == '__main__':
    # print("im inside if")
    app.run(host = '0.0.0.0', debug= True)