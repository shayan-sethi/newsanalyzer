import re
from newspaper import Article
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment_analyzer = pipeline("sentiment-analysis")
tokenizer = AutoTokenizer.from_pretrained("premsa/political-bias-prediction-allsides-DeBERTa")
model = AutoModelForSequenceClassification.from_pretrained("premsa/political-bias-prediction-allsides-DeBERTa")
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def extract_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text.strip()

def clean_article(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'Advertisement.*', '', text)
    return text.strip()

def summarize_text(text):
    if not text or len(text.strip()) == 0:
        return "No content to summarize."
    try:
        shortened = text[:2000].strip().replace('\n', ' ')
        summary = summarizer(shortened, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Summarization failed: {str(e)}"

def analyze_sentiment(cleaned_text):
    if not cleaned_text or len(cleaned_text.strip()) == 0:
        return "No content to analyze."
    try:
        input_text = cleaned_text[:512]
        result = sentiment_analyzer(input_text)[0]
        return result['label'].lower()
    except Exception as e:
        return f"Sentiment analysis failed: {str(e)}"

def detect_bias(cleaned_text):
    if not cleaned_text or len(cleaned_text.strip()) == 0:
        return "No content to analyze."
    try:
        input_text = cleaned_text[:512]
        result = classifier(input_text)[0]
        label = result['label']
        score = round(result['score'] * 100, 2)
        label_map = {
            "LABEL_0": "LEFT",
            "LABEL_1": "CENTER",
            "LABEL_2": "RIGHT"
        }
        bias_label = label_map.get(label, "UNKNOWN")
        return f"{bias_label} ({score}%)"
    except Exception as e:
        return f"Bias detection failed: {str(e)}"
