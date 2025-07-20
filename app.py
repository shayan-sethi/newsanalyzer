from flask import Flask, render_template, request
from news_scraper import analyze_news

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form['url']
    result = analyze_news(url)
    return result  # or jsonify(result) if it's a dict
