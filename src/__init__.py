from flask import Flask, render_template, request, redirect, url_for, session
import os, json, time
import requests

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', "super-secret-dev-key")

warehouse_data = 'data_warehouse.json'
weather_data = 'https://api.met.no/weatherapi/locationforecast/2.0/compact.json'

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
                        # print(v)
                        # print(site_id)
                        return s

def get_weather(lat, long, delay=0):
    if delay > 0:
        print(f"Weather Request delayed by: {delay} seconds")

    r = requests.get(weather_data + f"?lat={lat}&lon={long}")
    if r.status_code == 200:
        time.sleep(delay)
        return r.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        site = request.form['site']
        
        return redirect(url_for("site_status", site=site))

    if "user" in session:
        user = session["user"]

        return render_template('index.html', user=user)

    return render_template('index.html')
    

@app.route('/site_report')
def site_status():
    if "user" in session:
        user = session["user"]

        args = request.args

        site = search_site(args['site'])

        if type(site) != dict:
            return '<p>Unknown Site</p>'
        
        lat = site["location"]["lat"]
        long = site["location"]["long"]

        weather = get_weather(lat, long)

        if site != None:
            return render_template('site.html', user=user, site=site, weather=weather)
            
    
    return redirect(url_for("index"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form["user"]
        password = request.form['password']

        session["user"] = user

        return redirect(url_for("index", user=user))
    
    return render_template('login.html')