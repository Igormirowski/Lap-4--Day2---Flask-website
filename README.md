# DAY 2 Flask part 2 Build basic website 

- `pipenv shell`
- `pipenv install flask`
- create app.py
- copy stuff from [link](https://palletsprojects.com/p/flask/)
```
from flask import Flask, escape, request

app = Flask(__name__)
```
- Check name of your virtual environment`pipenv --venv` / `pipenv --where`
- COMMAND + Shift + P : > reload windown
- COMMAND + Shift + P (interpreter pick from link venv(vid22))

```
if __name__ =="__main__":
    app.run(debug=True, port=4000) # set port 4000
```
- `pipenv install --dev pep8 autopep8` (not mandatory)
- add route
```
@app.route('/')
def index():
    return"<h1>Hello Igor</h1>"
```
- `python app.py` (see port 4000)
- we can add style 
- add dynamic route 
- check for dynamic value`http://localhost:4000/students/Igor`
- create information route
- create folder templates 
- do index.html there 
- create base/layout.html (add bootstrap)
- add navbar
- add block
```
{% block content %}
data
{% endblock %}
```
- Jinja extension to see colors in block
- index.html: 
```
{% extends "base.html" %}
{% block content %}
{% endblock %}
```
- connect app.py to templates:
`render_template` and replate in return routes
```
@app.route('/')
def index():
    return render_template('index.html')
```

- block in base into container
- create route signup and create signup.html
- add stuff inputs in signup.html
- check `http://localhost:4000/signup`
- create welcome route and page so when signed up we can see name with welcome msg
- modify index route to see Beth name in front page
- remember to import requerst
- change href in base in nav to link to hompage
` <a class="navbar-brand text-white ms-3" href=" {{ url_for('index') }}`
- add img
- create static folder -> img folder -> add img
- add trainers names printed

- 404 handle:
- create 404 route and errors folder with 404.html
- add page titles


USEFUL LINKS 
- https://jinja.palletsprojects.com/en/3.0.x/templates/#synopsis

