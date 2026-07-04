Let's create the complete Setup Guide now! 🚀

---

## 🛠️ Create the Setup Guide

Open your existing `SETUP_GUIDE.md` file in VS Code and **replace everything** with this:

```markdown
# 🌿 Crop Disease Detection System
## Setup Guide for New Users

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project** | Crop Disease Detection System |
| **Model** | MobileNetV2 Transfer Learning |
| **Dataset** | Bangladesh Multi-Crop Disease Classification (2025) |
| **Classes** | 94 disease classes across 13 crops |
| **Accuracy** | 88.37% |
| **Backend** | Python Flask |
| **Frontend** | HTML, CSS, JavaScript |

---

## ⚙️ Requirements

Make sure your laptop has:
- Windows 10 or above
- At least **25 GB free disk space** (for dataset)
- Good internet connection (for first time dataset download)
- Python 3.11 installed (steps below)

---

## 🛠️ Step by Step Setup

### Step 1 — Install Git
Download and install Git from:
👉 https://git-scm.com/downloads

---

### Step 2 — Clone the Repository
Open terminal (Command Prompt or VS Code terminal) and run:
```
git clone <your-github-repo-link>
```
Then open the folder:
```
cd crop-disease-detection
```

---

### Step 3 — Install Python 3.11

#### Option A — If you have NO Python installed:
Download and install Python 3.11 directly from:
👉 https://www.python.org/downloads/release/python-3117/

Scroll down to Files section → Click:
**Windows installer (64-bit)**

During installation:
- ✅ Check "Add python.exe to PATH"
- Click "Install Now"

#### Option B — If you already have Python installed:
Open terminal and run:

```
py install 3.11
```

If you see any prompts about:
- **App execution aliases** → Open Settings → Enable both Python entries
- **Python Launcher conflict** → Type `y` → Uninstall old Python Launcher

Verify installation:
```
py list
```
You should see Python 3.11 in the list.

---

### Step 4 — Create Virtual Environment
```
py -3.11 -m venv venv
```

---

### Step 5 — Activate Virtual Environment
```
venv\Scripts\activate
```
You should see **(venv)** appear at the start of your terminal line.

---

### Step 6 — Upgrade pip
```
python -m pip install --upgrade pip
```

---

### Step 7 — Install All Required Libraries
```
pip install -r requirements.txt
```
⚠️ This will take a few minutes — TensorFlow is large (~500MB)

---

### Step 8 — Create Hugging Face Account
Go to: 👉 https://huggingface.co/join
- Sign up with your email (free, takes 1 minute)
- Verify your email

---

### Step 9 — Login to Hugging Face
```
hf auth login
```
- Select **"Log in with your browser"**
- Login with your Hugging Face account in the browser
- Terminal will show **"Login successful"**

---

### Step 10 — Download the Dataset
```
python download_dataset.py
```
⚠️ **Important:**
- Dataset size is **19.4 GB**
- Make sure you have good internet connection
- Do NOT close the terminal while downloading
- This step only needs to be done **once** — it caches automatically

---

### Step 11 — Verify Dataset
```
python explore_data.py
```
You should see:
```
Total training images: 86467
Total classes: 94
✅ Exploration complete!
```

---

### Step 12 — Run the Application
```
python run.py
```
You should see:
```
✅ Model loaded!
✅ 94 classes loaded!
🌿 Crop Disease Detection System
Starting server...
Open your browser at: http://localhost:5000
```

---

### Step 13 — Open in Browser
Open your browser and go to:
👉 **http://localhost:5000**

---

## 🧪 How to Use the Application

1. Click **"Choose Image"**
2. Upload a **clear crop leaf photo** (JPG, PNG, JPEG, WEBP)
3. Click **"🔍 Detect Disease"**
4. View the result:
   - ✅ **HEALTHY CROP** — crop is healthy
   - ⚠️ **DISEASE DETECTED** — shows disease name and confidence

---

## 🌿 Supported Crops

| # | Crop | # | Crop |
|---|------|---|------|
| 1 | Banana | 8 | Rice |
| 2 | Cauliflower | 9 | Sugarcane |
| 3 | Corn | 10 | Tea |
| 4 | Cotton | 11 | Tomato |
| 5 | Guava | 12 | Wheat |
| 6 | Jute | 13 | Papaya |
| 7 | Mango | | |

---

## ⚠️ Important Notes

| Note | Detail |
|------|--------|
| 🍃 **Leaf images only** | Upload clear close-up leaf photos for best results |
| 📸 **Image quality** | Well-lit, clear images give higher confidence |
| 🌐 **Internet** | Only needed for first-time dataset download |
| 💻 **Localhost only** | App runs locally — no internet needed after setup |
| 🔄 **Dataset cache** | After first download, dataset loads instantly from cache |

---

## 🐛 Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| `venv\Scripts\activate` not working | Run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` |
| `hf` command not found | Run: `pip install huggingface_hub` |
| Model not found error | Make sure `src/model/best_model.keras` exists |
| Port 5000 already in use | Change port in `run.py` to 5001 |
| Low prediction confidence | Use clearer, close-up leaf images |

---

## 📁 Project Structure

```
crop-disease-detection/
├── src/
│   ├── api/
│   │   ├── app.py              ← Flask API
│   │   └── predict.py          ← Prediction logic
│   ├── model/
│   │   ├── best_model.keras    ← Trained AI model
│   │   ├── final_model.keras   ← Final model
│   │   └── class_names.json    ← 94 class names
│   └── preprocessing/
│       └── preprocess.py       ← Data preprocessing
├── static/uploads/             ← Uploaded images stored here
├── templates/
│   └── index.html              ← Web interface
├── .gitignore
├── requirements.txt            ← All required libraries
├── download_dataset.py         ← Dataset download script
├── explore_data.py             ← Dataset exploration script
└── run.py                      ← Main entry point
```
