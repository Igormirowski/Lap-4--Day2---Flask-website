from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lead = "Beth"
    trainers = ['beth', 'claire', 'romer']
    return render_template("index.html", name=lead, name=trainers)

# Dynamic Route
@app.route('/students/<name>')
def student(name):
    return f"<h1>Profilepage for {name.capitalize()}</h1>"


@app.route('/information')
def info():
    return "<h1>We are currently in lap4</h1>"


#signup page
@app.route('/signup')
def signup_form():
    return render_template("signup.html")

#welcome page
@app.route('/welcome')
def welcome():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("welcome.html", first=first, last=last)

# #welcome page access logi data 


# # handle 404
#  @app.errorhandler(404)
#  def page_not_found(e)
#  path = request.path
#     return render_template('error/404.html',path=path),404




if __name__ =="__main__":
    app.run(debug=True, port=4000) # set port 4000
