from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os, json, time
import requests

# Application factory pattern
ROOT = os.path.abspath(os.curdir)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = os.urandom(16),
        DATABASE = os.path.join(ROOT, 'data/warehouse.db'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .auth import bp
    from .warehouse import bp
    from .tower_status import bp

    app.register_blueprint(auth.bp)
    app.register_blueprint(warehouse.bp)
    app.register_blueprint(tower_status.bp)

    @app.route('/')
    def index():
        return redirect(url_for("tower_status.index"))

    return app













# app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY', "super-secret-dev-key")

# warehouse_data = 'data_warehouse.json'
# weather_data = 'https://api.met.no/weatherapi/locationforecast/2.0/compact.json'

# tickets = [
#         {
#             'id': 12,
#             'summary': 'Ipsum Lorem minim fugiat deserunt velit voluptate et reprehenderit velit laboris Lorem eu laboris consectetur.',
#             'associated_locations': 2
#         },
#         {
#             'id': 1,
#             'summary': 'Ipsum Lorem minim fugiat deserunt velit voluptate et reprehenderit velit laboris Lorem eu laboris consectetur.',
#             'associated_locations': 1
#         }
#     ]

# def search_tickets(site_id='all'):
#     if site_id == 'all':
#         return tickets
#     else:
#         site_id = int(site_id)

#         # print(tickets)

#         for ticket in tickets:
#             if site_id == ticket['associated_locations']:
#                 return ticket



# def search_site(site_id='all'):
#     if site_id == 'all':
#         with open(warehouse_data) as json_file:
#             data = json.load(json_file)
#             return data
#     else:
#         site_id = int(site_id)

#         with open(warehouse_data) as json_file:
#             data = json.load(json_file)

#             for s in data:
#                 for k, v in s.items():
#                     if v == site_id:
#                         return s

# def get_weather(lat, long, delay=0):
#     if delay > 0:
#         print(f"Weather Request delayed by: {delay} seconds")

#     r = requests.get(weather_data + f"?lat={lat}&lon={long}")
#     if r.status_code == 200:
#         time.sleep(delay)
#         return r.json()
#     else:
#         return None

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == "POST":
#         site = request.form['site']
        
#         return redirect(url_for("site_status", site=site))

#     if "user" in session:
#         user = session["user"]

#         return render_template('index.html', user=user)

#     return render_template('index.html')
    

# @app.route('/site_report')
# def site_status():
#     if "user" in session:
#         user = session["user"]

#         args = request.args

#         site = search_site(args['site'])

#         if type(site) != dict:
#             return '<p>Unknown Site</p>'
        
#         lat = site["location"]["lat"]
#         long = site["location"]["long"]

#         weather = get_weather(lat, long)

#         if site != None:
#             return render_template('site.html', user=user, site=site, weather=weather)
            
    
#     return redirect(url_for("index"))

# @app.route('/site_report/__tickets', methods=['POST'])
# def __tickets():
#     incoming = request.get_json()

#     data = search_tickets(incoming['site_id'])
#     print(request.get_json())

#     time.sleep(2)
#     return jsonify(data)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user = request.form["user"]
#         password = request.form['password']

#         session["user"] = user

#         # TODO: After logging in, redirect to the route the user originally requested, ?next=/site_report
#         return redirect(url_for("index", user=user))
    
#     return render_template('login.html')

# @app.route('/logout', methods=['POST'])
# def logout():
    # print('logouts')