from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    title = "Tower Status Checker"

    if request.method == "POST":
        site = request.form['site']
        print(site)
        return redirect(url_for("site_status", site=site))

    return render_template('index.html', title=title)

@app.route('/<site>')
def site_status(site):
    return render_template('site.html', site=site)
