from flask import render_template,url_for
from . import app


@app.route('/')
@app.route('/home')
def home():
    return render_template ('home.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/contact')
def contact():
    return render_template ('contact.html')

@app.route('/services')
def services():
    return render_template ('services.html')