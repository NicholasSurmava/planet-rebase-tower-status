from flask import Flask, render_template

# TODO: Below is temp
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    title = "Tower Status Checker"

    return render_template('index.html', title=title)
    
if __name__ == '__main__':
    serve(app)