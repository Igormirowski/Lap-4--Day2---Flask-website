from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    return"<h1>Hello Igor</h1>"

if __name__ =="__main__":
    app.run(debug=True, port=4000) # set port 4000
