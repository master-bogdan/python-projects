from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html')

@app.get('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

@app.post('/submit-form')
def submit_form():
    return redirect('/thankyou.html')
