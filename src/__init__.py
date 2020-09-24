from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', "super-secret-dev-key")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        site = request.form['site']
        return redirect(url_for("site_status", site=site))

    if "user" in session:
        user = session["user"]
        return render_template('index.html', user=user)

    return render_template('index.html')
    

@app.route('/<site>')
def site_status(site):
    if "user" in session:
        user = session["user"]
        return render_template('site.html', site=site, user=user)
    
    return redirect(url_for("index"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form["user"]
        password = request.form['password']

        session["user"] = user

        return redirect(url_for("index", user=user))
    
    return render_template('login.html')