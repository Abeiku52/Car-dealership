from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import json

app = Flask(__name__)
CORS(app)

# Simple sentiment analysis using keyword-based approach
POSITIVE_WORDS = [
    'excellent', 'amazing', 'fantastic', 'great', 'wonderful', 'awesome', 
    'outstanding', 'superb', 'brilliant', 'perfect', 'love', 'best', 
    'incredible', 'satisfied', 'happy', 'pleased', 'good', 'nice',
    'helpful', 'friendly', 'professional', 'recommend', 'quality'
]

NEGATIVE_WORDS = [
    'terrible', 'awful', 'horrible', 'bad', 'worst', 'hate', 'disappointed',
    'poor', 'rude', 'unprofessional', 'slow', 'expensive', 'overpriced',
    'dishonest', 'fraud', 'scam', 'waste', 'regret', 'avoid', 'never',
    'problem', 'issue', 'complaint', 'angry', 'frustrated'
]

def analyze_sentiment(text):
    """
    Analyze sentiment of given text
    Returns: positive, negative, or neutral
    """
    if not text:
        return 'neutral'
    
    # Convert to lowercase and remove punctuation
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    words = clean_text.split()
    
    positive_score = 0
    negative_score = 0
    
    for word in words:
        if word in POSITIVE_WORDS:
            positive_score += 1
        elif word in NEGATIVE_WORDS:
            negative_score += 1
    
    # Determine sentiment based on scores
    if positive_score > negative_score:
        return 'positive'
    elif negative_score > positive_score:
        return 'negative'
    else:
        return 'neutral'

@app.route('/analyze', methods=['POST'])
def analyze_review():
    """
    Endpoint to analyze sentiment of review text
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'error': 'Missing text field in request'
            }), 400
        
        text = data['text']
        sentiment = analyze_sentiment(text)
        
        return jsonify({
            'text': text,
            'sentiment': sentiment,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'sentiment-analysis'
    })

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with service information"""
    return jsonify({
        'service': 'Car Dealership Sentiment Analysis API',
        'version': '1.0.0',
        'endpoints': {
            'analyze': 'POST /analyze - Analyze sentiment of text',
            'health': 'GET /health - Health check'
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)