"""
Model Training Script
Crop Disease Detection - Bangladesh Multi-Crop Dataset
Using MobileNetV2 Transfer Learning
"""

import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from datasets import load_dataset
from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter

# ── Suppress TF logs ──
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# ── Settings ──
IMAGE_SIZE    = (224, 224)
BATCH_SIZE    = 32
EPOCHS        = 20
LEARNING_RATE = 0.001
MODEL_DIR     = 'src/model'
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs('static/uploads', exist_ok=True)

print("="*60)
print("CROP DISEASE DETECTION — MODEL TRAINING")
print("="*60)

# ── Step 1: Load Dataset ──
print("\n[1/6] Loading dataset...")
dataset = load_dataset('Saon110/bd-crop-vegetable-plant-disease-dataset')
print("✅ Dataset loaded!")

# ── Step 2: Load Class Names ──
print("\n[2/6] Loading class mappings...")
with open(f'{MODEL_DIR}/class_names.json', 'r') as f:
    class_info = json.load(f)

class_to_idx = class_info['class_to_idx']
idx_to_class = class_info['idx_to_class']
NUM_CLASSES   = class_info['num_classes']
print(f"✅ {NUM_CLASSES} classes loaded!")

# ── Step 3: Preprocessing Function ──
def preprocess_image(image):
    image = image.resize(IMAGE_SIZE, Image.LANCZOS)
    image = image.convert('RGB')
    return np.array(image) / 255.0

# ── Step 4: Data Generator ──
print("\n[3/6] Setting up data generators...")

def data_generator(split, batch_size=BATCH_SIZE, augment=False):
    """
    Generator that yields batches of
    (images, labels) from the dataset.
    """
    data    = dataset[split]
    indices = list(range(len(data)))
    
    while True:
        np.random.shuffle(indices)
        for start in range(0, len(indices), batch_size):
            batch_idx = indices[start:start + batch_size]
            images, labels = [], []
            
            for idx in batch_idx:
                sample     = data[idx]
                img        = preprocess_image(sample['image'])
                label_name = sample['label_name']
                label_idx  = class_to_idx[label_name]
                
                # Basic augmentation for training
                if augment:
                    # Random horizontal flip
                    if np.random.random() > 0.5:
                        img = np.fliplr(img)
                    # Random vertical flip
                    if np.random.random() > 0.5:
                        img = np.flipud(img)
                    # Random brightness
                    brightness = np.random.uniform(0.8, 1.2)
                    img        = np.clip(img * brightness, 0, 1)
                
                images.append(img)
                labels.append(label_idx)
            
            yield (
                np.array(images),
                tf.keras.utils.to_categorical(labels, NUM_CLASSES)
            )

# Calculate steps
TRAIN_STEPS = len(dataset['train']) // BATCH_SIZE
VALID_STEPS = len(dataset['valid']) // BATCH_SIZE

print(f"✅ Train steps per epoch: {TRAIN_STEPS}")
print(f"✅ Valid steps per epoch: {VALID_STEPS}")

# ── Step 5: Build Model ──
print("\n[4/6] Building MobileNetV2 model...")

# Load MobileNetV2 base (pre-trained on ImageNet)
base_model = MobileNetV2(
    weights    = 'imagenet',
    include_top = False,
    input_shape = (224, 224, 3)
)

# Freeze base model layers initially
base_model.trainable = False

# Add custom classification head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = BatchNormalization()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.4)(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.3)(x)
output = Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=output)

# Compile model
model.compile(
    optimizer = Adam(learning_rate=LEARNING_RATE),
    loss      = 'categorical_crossentropy',
    metrics   = ['accuracy']
)

print("✅ Model built successfully!")
print(f"✅ Total parameters: {model.count_params():,}")
print(f"✅ Trainable parameters: {sum([tf.size(w).numpy() for w in model.trainable_weights]):,}")

# ── Step 6: Callbacks ──
print("\n[5/6] Setting up training callbacks...")

callbacks = [
    # Save best model
    ModelCheckpoint(
        filepath        = f'{MODEL_DIR}/best_model.keras',
        monitor         = 'val_accuracy',
        save_best_only  = True,
        verbose         = 1
    ),
    # Stop early if no improvement
    EarlyStopping(
        monitor   = 'val_accuracy',
        patience  = 5,
        verbose   = 1,
        restore_best_weights = True
    ),
    # Reduce learning rate if stuck
    ReduceLROnPlateau(
        monitor  = 'val_accuracy',
        factor   = 0.5,
        patience = 3,
        verbose  = 1,
        min_lr   = 1e-7
    )
]
print("✅ Callbacks ready!")

# ── Step 7: Train Model ──
print("\n[6/6] Starting training...")
print("⚠️  This will take time — please don't close the terminal!")
print("="*60)

history = model.fit(
    data_generator('train', augment=True),
    steps_per_epoch  = TRAIN_STEPS,
    epochs           = EPOCHS,
    validation_data  = data_generator('valid'),
    validation_steps = VALID_STEPS,
    callbacks        = callbacks,
    verbose          = 1
)

# ── Save Final Model ──
print("\n💾 Saving final model...")
model.save(f'{MODEL_DIR}/final_model.keras')
print(f"✅ Model saved to {MODEL_DIR}/final_model.keras")

# ── Plot Training History ──
print("\n📊 Saving training history charts...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Accuracy
ax1.plot(history.history['accuracy'],     label='Train Accuracy', color='blue')
ax1.plot(history.history['val_accuracy'], label='Val Accuracy',   color='orange')
ax1.set_title('Model Accuracy')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Accuracy')
ax1.legend()
ax1.grid(True)

# Loss
ax2.plot(history.history['loss'],     label='Train Loss', color='blue')
ax2.plot(history.history['val_loss'], label='Val Loss',   color='orange')
ax2.set_title('Model Loss')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig(f'{MODEL_DIR}/training_history.png')
print(f"✅ Training charts saved to {MODEL_DIR}/training_history.png")

print("\n" + "="*60)
print("✅ TRAINING COMPLETE!")
print("="*60)
print(f"\nFinal Results:")
print(f"  Train Accuracy: {history.history['accuracy'][-1]*100:.2f}%")
print(f"  Val Accuracy:   {history.history['val_accuracy'][-1]*100:.2f}%")
print(f"\nModel saved to: {MODEL_DIR}/best_model.keras")