from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    return"<h1 style='color:red'>Hello Igor</h1>"


# Dynamic Route
@app.route('/students/<name>')
def student(name):
    return f"<h1 style='color:red'>Profilepage for {name.capitalize()}</h1>"


if __name__ =="__main__":
    app.run(debug=True, port=4000) # set port 4000
