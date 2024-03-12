from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id":1,
        "title": "data engineering",
        "location": "bengaluru, India"
    },
    {
        "id":2,
        "title": "data science",
        "location": "bengaluru, India"
    },
    {
        "id":3,
        "title": "data excel",
        "location": "bengaluru, India"
    },
    {
        "id":4,
        "title": "data play",
        "location": "bengaluru, India"
    }
]


@app.route("/")
def hello_word():
    return render_template('home.html', jobs = JOBS, cn = "akshat")

@app.route("/api/cool")
def x():
    return jsonify(JOBS)


if __name__ == '__main__':
    # print("im inside if")
    app.run(host = '0.0.0.0', debug= True)