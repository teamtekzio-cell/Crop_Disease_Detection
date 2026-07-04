"""
Flask Backend API
Crop Disease Detection System
"""

import os
import uuid
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.api.predict import predict_disease

# ── App Setup ──
app = Flask(
    __name__,
    template_folder='../../templates',
    static_folder='../../static'
)
CORS(app)

# ── Upload Folder ──
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ── Allowed File Types ──
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Routes ──

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict crop disease from uploaded image
    Expects: multipart/form-data with 'image' field
    Returns: JSON with prediction results
    """
    # Check if image was sent
    if 'image' not in request.files:
        return jsonify({
            'success': False,
            'error'  : 'No image uploaded'
        }), 400

    file = request.files['image']

    # Check if file was selected
    if file.filename == '':
        return jsonify({
            'success': False,
            'error'  : 'No file selected'
        }), 400

    # Check file type
    if not allowed_file(file.filename):
        return jsonify({
            'success': False,
            'error'  : 'Invalid file type. Please upload PNG, JPG or JPEG'
        }), 400

    try:
        # Save uploaded file with unique name
        ext      = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4().hex}.{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Run prediction
        result = predict_disease(filepath)

        # Add image URL to result
        result['image_url'] = f"/static/uploads/{filename}"

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            'success': False,
            'error'  : f'Prediction failed: {str(e)}'
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status' : 'running',
        'model'  : 'MobileNetV2',
        'classes': 94
    }), 200


# ── Run App ──
if __name__ == '__main__':
    app.run(
        host  = '0.0.0.0',
        port  = 5000,
        debug = True
    )