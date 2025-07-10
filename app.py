from flask import Flask, render_template, request, jsonify
from news_scraper import extract_article, summarize_text, analyze_sentiment, detect_bias

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')

    article = extract_article(url)
    summary = summarize_text(article)
    sentiment = analyze_sentiment(article)
    bias = detect_bias(article)

    return jsonify({
        'summary': summary,
        'sentiment': sentiment,
        'bias': bias
    })

if __name__ == '__main__':
    app.run()
from flask import request
import os
import signal

@app.route("/shutdown", methods=["POST"])
def shutdown():
    pid = os.getpid()
    os.kill(pid, signal.SIGTERM)
    return "Shutting down..."