from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Dynamic Route
@app.route('/students/<name>')
def student(name):
    return f"<h1>Profilepage for {name.capitalize()}</h1>"


@app.route('/information')
def info():
    return "<h1>We are currently in lap4</h1>"



if __name__ =="__main__":
    app.run(debug=True, port=4000) # set port 4000
