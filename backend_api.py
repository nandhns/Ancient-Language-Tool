# backend_api.py

from flask import Flask, request, jsonify
from PIL import Image
import io
import google.generativeai as genai
import os
import tensorflow as tf
import numpy as np
import cv2
from ocr_model import model, preprocess_image, decode_predictions

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
gemini_model = genai.GenerativeModel('gemini-pro')

# ... (image_to_text, detect_script, translate_text, predict_text functions remain the same)

def generate_tags(text):
    # Placeholder: Replace with your actual tag generation logic
    return {
        "demographic": "Example Demographic",
        "era": "Example Era"
    }

@app.route('/translate', methods=['POST'])
def translate_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    try:
        img = Image.open(io.BytesIO(image_file.read()))
    except Exception as e:
        return jsonify({'error': f"Error opening image: {e}"}), 400

    try:
        extracted_text = image_to_text(img)
        detected_script = detect_script(extracted_text)
        translated_text = translate_text(extracted_text)
        predicted_text = predict_text(extracted_text)
        tags = generate_tags(extracted_text) # Generate tags

        return jsonify({
            'script': detected_script,
            'extracted_text': extracted_text,
            'translated_text': translated_text,
            'predicted_text': predicted_text,
            'demographic': tags.get('demographic'), #add demographic
            'era': tags.get('era') #add era.
        })
    except Exception as e:
        return jsonify({'error': f"Processing error: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)