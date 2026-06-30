"""
Explore Dataset Script
Crop Disease Detection - Bangladesh Multi-Crop Dataset
"""

from datasets import load_dataset
import matplotlib.pyplot as plt
from collections import Counter

print("Loading dataset...")
dataset = load_dataset('Saon110/bd-crop-vegetable-plant-disease-dataset')

train_data = dataset['train']

# 1. Basic Info
print("\n" + "="*50)
print("DATASET OVERVIEW")
print("="*50)
print(f"Total training images: {len(train_data)}")
print(f"Total classes: {len(set(train_data['label']))}")

# 2. Show first sample
print("\n" + "="*50)
print("SAMPLE DATA POINT")
print("="*50)
sample = train_data[0]
print(f"Label (number): {sample['label']}")
print(f"Label (name): {sample['label_name']}")
print(f"Image type: {type(sample['image'])}")
print(f"Image size: {sample['image'].size}")

# 3. Class distribution (top 10 and bottom 10)
print("\n" + "="*50)
print("CLASS DISTRIBUTION")
print("="*50)
label_counts = Counter(train_data['label_name'])
sorted_counts = sorted(label_counts.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 most common classes:")
for name, count in sorted_counts[:10]:
    print(f"  {name}: {count} images")

print("\nBottom 10 least common classes:")
for name, count in sorted_counts[-10:]:
    print(f"  {name}: {count} images")

# 4. Save a sample image to view
print("\n" + "="*50)
print("SAVING SAMPLE IMAGE")
print("="*50)
sample_image = train_data[0]['image']
sample_image.save("sample_leaf.png")
print(f"Saved sample image as 'sample_leaf.png' — labeled as: {sample['label_name']}")

# 5. Plot class distribution graph
plt.figure(figsize=(12, 6))
names = [x[0] for x in sorted_counts[:20]]
counts = [x[1] for x in sorted_counts[:20]]
plt.barh(names, counts, color='green')
plt.xlabel('Number of Images')
plt.title('Top 20 Classes by Image Count')
plt.tight_layout()
plt.savefig('class_distribution.png')
print("Saved class distribution chart as 'class_distribution.png'")

print("\n✅ Exploration complete! Check the generated images in your project folder.")