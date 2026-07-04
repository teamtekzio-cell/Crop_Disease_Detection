"""
Prediction Logic
Crop Disease Detection System
"""

import numpy as np
import json
import os
from PIL import Image
import tensorflow as tf

# ── Suppress TF logs ──
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# ── Paths ──
MODEL_PATH      = 'src/model/best_model.keras'
CLASS_INFO_PATH = 'src/model/class_names.json'
IMAGE_SIZE      = (224, 224)

# ── Load Model & Class Names Once ──
print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model loaded!")

with open(CLASS_INFO_PATH, 'r') as f:
    class_info = json.load(f)

idx_to_class = {int(k): v for k, v in class_info['idx_to_class'].items()}
print(f"✅ {len(idx_to_class)} classes loaded!")


def preprocess_image(image_path):
    """
    Load and preprocess image for prediction
    """
    img = Image.open(image_path).convert('RGB')
    img = img.resize(IMAGE_SIZE, Image.LANCZOS)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def predict_disease(image_path):
    """
    Predict crop disease from image path
    Returns top 3 predictions with confidence scores
    """
    # Preprocess
    img_array = preprocess_image(image_path)

    # Predict
    predictions = model.predict(img_array, verbose=0)
    pred_probs  = predictions[0]

    # Get top 3 predictions
    top3_indices = np.argsort(pred_probs)[::-1][:3]

    results = []
    for idx in top3_indices:
        class_name   = idx_to_class[idx]
        confidence   = float(pred_probs[idx]) * 100

        # Format class name nicely
        # e.g. "Tomato_Early_Blight" → "Tomato — Early Blight"
        parts        = class_name.split('_', 1)
        crop         = parts[0]
        condition    = parts[1].replace('_', ' ') if len(parts) > 1 else ''

        # Check if healthy
        is_healthy   = 'healthy' in class_name.lower() or 'Healthy' in class_name

        results.append({
            'class_name'  : class_name,
            'crop'        : crop,
            'condition'   : condition,
            'confidence'  : round(confidence, 2),
            'is_healthy'  : is_healthy
        })

    return {
        'top_prediction' : results[0],
        'top3'           : results,
        'success'        : True
    }