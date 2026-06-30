"""
Download Dataset Script
Crop Disease Detection - Bangladesh Multi-Crop Dataset
"""

from datasets import load_dataset

print("Starting dataset download...")
print("This may take a while depending on your internet speed (~19.4 GB)")

dataset = load_dataset('Saon110/bd-crop-vegetable-plant-disease-dataset')

print("\n✅ Dataset downloaded successfully!")
print(dataset)

print("\n📊 Dataset Summary:")
print(f"Train images: {len(dataset['train'])}")
print(f"Validation images: {len(dataset['valid'])}")
print(f"Test images: {len(dataset['test'])}")