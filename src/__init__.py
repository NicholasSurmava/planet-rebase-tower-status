from flask import Flask, render_template, request, redirect, url_for, session
import os, json, time

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', "super-secret-dev-key")

warehouse_data = 'data_warehouse.json'
weather_data = ' '

def search_site(site_id='all'):
    if site_id == 'all':
        with open(warehouse_data) as json_file:
            data = json.load(json_file)
            return data
    else:
        site_id = int(site_id)

        with open(warehouse_data) as json_file:
            data = json.load(json_file)
            for s in data:
                for k, v in s.items():
                    if v == site_id:
                        return s

def get_weather(site_id='all'):
    time.sleep(3)
    return 'hot'

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

        site = search_site(site)
        weather = get_weather()

        if site != None:
            return render_template('site.html', user=user, site=site, weather=weather)
        else:
            return '<p>Unknown Site</p>'
    
    return redirect(url_for("index"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form["user"]
        password = request.form['password']

        session["user"] = user

        return redirect(url_for("index", user=user))
    
    return render_template('login.html')