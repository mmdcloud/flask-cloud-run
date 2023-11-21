from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h6>Hello from Flask</h6>'


if __name__ == "__main__":
    app.run(debug=True)
