No problem! Let's create it quickly before pushing! 😊

---

## 🛠️ Create `README.md`

**File name:** `README.md`

Paste this:

```markdown
# 🌿 Crop Disease Detection System

An intelligent web-based application that detects crop diseases from leaf images using Deep Learning and Transfer Learning (MobileNetV2).

---

## 🎯 Project Overview

| Detail | Info |
|--------|------|
| **Model** | MobileNetV2 Transfer Learning |
| **Dataset** | Bangladesh Multi-Crop Disease Classification (2025) |
| **Total Images** | 123,588 |
| **Disease Classes** | 94 classes across 13 crops |
| **Accuracy** | 88.37% |
| **Backend** | Python Flask |
| **Frontend** | HTML, CSS, JavaScript |

---

## 🌿 Supported Crops & Diseases

| # | Crop | Disease Classes |
|---|------|----------------|
| 1 | 🍌 Banana | 9 |
| 2 | 🥬 Cauliflower | 4 |
| 3 | 🌽 Corn | 4 |
| 4 | 🌿 Cotton | 4 |
| 5 | 🍈 Guava | 9 |
| 6 | 🌾 Jute | 3 |
| 7 | 🥭 Mango | 8 |
| 8 | 🧡 Papaya | 8 |
| 9 | 🥔 Potato | 10 |
| 10 | 🍚 Rice | 10 |
| 11 | 🎋 Sugarcane | 5 |
| 12 | 🍵 Tea | 8 |
| 13 | 🍅 Tomato | 9 |
| | **Total** | **94 classes** |

---

### 🍌 Banana (9 diseases)
Black Pitting or Banana Rust, Crown Rot, Healthy, Fungal Disease, Leaf Banana Scab Moth, Leaf Black Sigatoka, Leaf Healthy, Leaf Black Leaf Streak, Leaf Panama Disease

### 🥬 Cauliflower (4 diseases)
Bacterial Spot Rot, Black Rot, Downy Mildew, Healthy

### 🌽 Corn (4 diseases)
Blight, Common Rust, Gray Leaf Spot, Healthy

### 🌿 Cotton (4 diseases)
Aphids, Army Worm, Bacterial Blight, Healthy

### 🍈 Guava (9 diseases)
Fruit Anthracnose, Fruit Healthy, Fruit Scab, Fruit Styler End Root, Leaf Anthracnose, Leaf Canker, Leaf Dot, Leaf Healthy, Leaf Rust

### 🌾 Jute (3 diseases)
Cescospora Leaf Spot, Golden Mosaic, Healthy Leaf

### 🥭 Mango (8 diseases)
Anthracnose, Bacterial Canker, Cutting Weevil, Gall Midge, Healthy, Powdery Mildew, Sooty Mould, Die Back

### 🧡 Papaya (8 diseases)
Anthracnose, Bacterial Spot, Curl, Healthy, Mealybug, Mite Disease, Mosaic, Ringspot

### 🥔 Potato (10 diseases)
Black Scurf, Blackleg, Blackspot Bruising, Brown Rot, Common Scab, Dry Rot, Healthy, Miscellaneous, Pink Rot, Soft Rot

### 🍚 Rice (10 diseases)
Blast, Brown Spot, Tungro, Bacterial Leaf Blight, Bacterial Leaf Streak, Bacterial Panicle Blight, Dead Heart, Downy Mildew, Hispa, Normal (Healthy)

### 🎋 Sugarcane (5 diseases)
Healthy, Mosaic, Red Rot, Rust, Yellow

### 🍵 Tea (8 diseases)
Anthracnose, Algal Leaf, Bird Eye Spot, Brown Blight, Gray Light, Healthy, Red Leaf Spot, White Spot

### 🍅 Tomato (9 diseases)
Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Healthy
---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **AI Model** | TensorFlow, Keras, MobileNetV2 |
| **Backend** | Python, Flask, Flask-CORS |
| **Frontend** | HTML, CSS, JavaScript |
| **Dataset** | Hugging Face — Bangladesh Multi-Crop 2025 |
| **Image Processing** | OpenCV, Pillow, NumPy |

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd crop-disease-detection
```

### 2. Install Python 3.11 & create virtual environment
```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Login to Hugging Face & download dataset
```bash
hf auth login
python download_dataset.py
```

### 5. Run the application
```bash
python run.py
```

### 6. Open in browser
```
http://localhost:5000
```

> 📖 For detailed setup instructions see [SETUP_GUIDE.md](SETUP_GUIDE.md)

---

## 🧪 How It Works

```
User uploads crop leaf image
           ↓
Flask API receives image
           ↓
MobileNetV2 model analyses image
           ↓
Returns disease prediction + confidence score
           ↓
Result displayed on web interface
```

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **Validation Accuracy** | 88.37% |
| **Train Accuracy** | 84.69% |
| **Total Epochs** | 20 |
| **Model Architecture** | MobileNetV2 + Custom Head |

### Training Progress

| Epoch | Val Accuracy |
|-------|-------------|
| 1 | 78.83% |
| 5 | 84.32% |
| 10 | 86.10% |
| 15 | 87.06% |
| 20 | **88.37%** |

---

## 📁 Project Structure

```
crop-disease-detection/
├── src/
│   ├── api/
│   │   ├── app.py              ← Flask API
│   │   └── predict.py          ← Prediction logic
│   ├── model/
│   │   ├── best_model.keras    ← Trained AI model (88.37%)
│   │   ├── final_model.keras   ← Final saved model
│   │   ├── class_names.json    ← 94 class mappings
│   │   └── training_history.png← Training accuracy chart
│   └── preprocessing/
│       └── preprocess.py       ← Data preprocessing
├── static/uploads/             ← User uploaded images
├── templates/
│   └── index.html              ← Web interface
├── .gitignore
├── requirements.txt
├── download_dataset.py         ← Dataset download script
├── explore_data.py             ← Dataset exploration script
├── run.py                      ← Main entry point
├── README.md                   ← You are here!
└── SETUP_GUIDE.md              ← Detailed setup guide
```

---

## ⚠️ Important Notes

- 🍃 Upload **clear close-up leaf images** for best results
- 📸 Well-lit images give higher confidence scores
- 💾 Dataset is **19.4 GB** — downloaded separately via Hugging Face
- 🖥️ Runs completely on **localhost** — no cloud needed

---

## 📚 Dataset

**Bangladesh Multi-Crop Disease Classification Dataset**
- Published: 2025
- Source: Hugging Face
- Images: 123,588
- Classes: 94 disease classes
- Crops: 13 different crops
- License: CC BY-NC-SA 4.0

---

## 📖 References

1. Saon, S. C. (2025). Bangladesh Multi-Crop Disease Classification Dataset. Hugging Face.
2. Mohanty, S. P., Hughes, D. P., & Salathé, M. (2016). Using Deep Learning for Image-Based Plant Disease Detection. Frontiers in Plant Science.
3. Barman et al. (2024). Optimized Crop Disease Identification in Bangladesh. Journal of Imaging.

---

## 🎓 Academic Info

| Detail | Info |
|--------|------|
| **Course** | MSc Computer Science — AI & Robotics |
| **University** | University of Hertfordshire |
| **Module** | 7COM1039-0509-2025 |
| **Student** | Akash Anand Amate (24178332) |

---

*Built with ❤️ using MobileNetV2 Transfer Learning*
```

