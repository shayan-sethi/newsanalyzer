# News Analyzer — Summary, Sentiment & Political Bias Detector
A minimal web-based tool that fetches any news article URL, summarizes its core content, and analyzes both the sentiment and political bias using state-of-the-art NLP models.

## Features
- Automatic article scraping via URL
- Text summarization using `facebook/bart-large-cnn`
- Sentiment analysis using `distilbert-base-uncased-finetuned-sst-2-english`
- Political bias classification with `premsa/political-bias-prediction-allsides-DeBERTa`
- One-click shutdown button (no need to hit Ctrl+C)

## How It Works

Paste a URL from any valid news site.

Click Analyze.

Behind the scenes:
- Article is downloaded and cleaned
- Summarizer extracts key points
- Sentiment and political bias are detected from the raw article

Results are displayed in real time on the page.

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/shayan-sethi/newsanalyzer
cd newsanalyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

If `newspaper3k` gives issues, try:
```bash
pip install newspaper3k --force-reinstall
```

### 3. Run the app
```bash
python start_app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Models Used
- `facebook/bart-large-cnn` — summarization
- `distilbert-base-uncased-finetuned-sst-2-english` — sentiment
- `premsa/political-bias-prediction-allsides-DeBERTa` — bias classification

