from flask import flash, redirect, render_template, session, url_for
from flask_login import login_required
from flask import current_app as app



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Homepage - goFarm")



@app.route('/dashboard')
@login_required
def dashboard():
    # return render_template('dashboard.html', title='Dashboard')
    return render_template('/dashboard/dashboard.html',title='Dashboard - goFarm')

@app.route('/logo')
def logo():
    # return render_template('dashboard.html', title='Dashboard')
    return render_template('/new/logo.html'  )

