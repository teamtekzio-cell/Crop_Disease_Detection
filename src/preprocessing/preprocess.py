"""
Data Preprocessing Script
Crop Disease Detection - Bangladesh Multi-Crop Dataset
"""

import numpy as np
from datasets import load_dataset
from PIL import Image
import json
import os

# ── Settings ──
IMAGE_SIZE = (224, 224)  # Standard size for CNN models
BATCH_SIZE = 32

print("="*50)
print("PREPROCESSING STARTED")
print("="*50)

# ── Step 1: Load Dataset ──
print("\n[1/4] Loading dataset from cache...")
dataset = load_dataset('Saon110/bd-crop-vegetable-plant-disease-dataset')
print("✅ Dataset loaded!")

# ── Step 2: Extract Class Names ──
print("\n[2/4] Extracting class names...")
label_names = dataset['train']['label_name']
unique_classes = sorted(list(set(label_names)))
num_classes = len(unique_classes)

# Create label to index mapping
class_to_idx = {cls: idx for idx, cls in enumerate(unique_classes)}
idx_to_class = {idx: cls for cls, idx in class_to_idx.items()}

print(f"✅ Found {num_classes} classes")

# ── Step 3: Save Class Mappings ──
print("\n[3/4] Saving class mappings...")

# Create src/model folder if not exists
os.makedirs('src/model', exist_ok=True)

# Save to JSON file — we'll use this later in Flask app
with open('src/model/class_names.json', 'w') as f:
    json.dump({
        'class_to_idx': class_to_idx,
        'idx_to_class': idx_to_class,
        'num_classes': num_classes,
        'image_size': IMAGE_SIZE
    }, f, indent=2)

print("✅ Class mappings saved to src/model/class_names.json")

# ── Step 4: Test Preprocessing on One Sample ──
print("\n[4/4] Testing preprocessing on a sample image...")

def preprocess_image(image):
    """
    Preprocess a single image:
    - Resize to 224x224
    - Convert to RGB (in case of grayscale)
    - Normalize pixel values to [0, 1]
    """
    # Resize
    image = image.resize(IMAGE_SIZE, Image.LANCZOS)
    # Convert to RGB
    image = image.convert('RGB')
    # Convert to numpy array
    img_array = np.array(image)
    # Normalize to [0, 1]
    img_array = img_array / 255.0
    return img_array

# Test on first sample
sample = dataset['train'][0]
processed = preprocess_image(sample['image'])

print(f"✅ Original image size: {sample['image'].size}")
print(f"✅ Processed image shape: {processed.shape}")
print(f"✅ Pixel value range: [{processed.min():.2f}, {processed.max():.2f}]")
print(f"✅ Label: {sample['label_name']}")

print("\n" + "="*50)
print("✅ PREPROCESSING SETUP COMPLETE!")
print("="*50)
print(f"\nReady to train with:")
print(f"  - Image size: {IMAGE_SIZE}")
print(f"  - Number of classes: {num_classes}")
print(f"  - Train samples: {len(dataset['train'])}")
print(f"  - Valid samples: {len(dataset['valid'])}")
print(f"  - Test samples: {len(dataset['test'])}")