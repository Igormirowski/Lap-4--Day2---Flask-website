from turtle import title
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    lead = "Beth"
    trainers = ['beth', 'claire', 'romer']
    title = "Home"
    return render_template("index.html", name=lead, names=trainers, title=title)


# Dynamic Route
@app.route('/students/<name>')
def student(name):
    title = "Students"
    return f"<h1>Profilepage for {name.capitalize()}</h1>,"


@app.route('/information')
def info():
    return "<h1>We are currently in lap4</h1>"


#signup page
@app.route('/signup')
def signup_form():
    title = "Signup"
    return render_template("signup.html",title=title)

#welcome page
@app.route('/welcome')
def welcome():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("welcome.html", first=first, last=last)

# handle 404
@app.errorhandler(404)
def page_not_found(e):
    path = request.path
    return render_template('errors/404.html',path=path),404



if __name__ =="__main__":
    app.run(debug=True, port=4000) # set port 4000
