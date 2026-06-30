# Setup Guide

Here's the complete step-by-step guide.

------------------------------------------------------------------------


### Step 1 --- Install Git (if not already installed)

Download from: https://git-scm.com/downloads

------------------------------------------------------------------------

### Step 2 --- Clone the Repository

Open terminal (VS Code or Command Prompt), run:

``` bash
git clone <your-github-repo-link>
```

### Step 3 --- Open the Project Folder

``` bash
cd crop-disease-detection
```

Then open it in VS Code:

``` bash
code .
```

------------------------------------------------------------------------

### Step 4 --- Install Python 3.11

Open terminal in VS Code, run:

``` bash
py install 3.11
```

If you see the same alias/launcher prompts, enable the required App
Execution Aliases or uninstall the old Python Launcher if needed.

------------------------------------------------------------------------

### Step 5 --- Create Virtual Environment

``` bash
py -3.11 -m venv venv
```

### Step 6 --- Activate Virtual Environment

``` bash
venv\Scripts\activate
```

You should see `(venv)` appear in the terminal.

------------------------------------------------------------------------

### Step 7 --- Install All Required Libraries

``` bash
pip install -r requirements.txt
```

This installs everything automatically using the versions specified in
`requirements.txt`.

------------------------------------------------------------------------

### Step 8 --- Create a Hugging Face Account

Visit:

https://huggingface.co/join

Create a free account using your own email.

------------------------------------------------------------------------

### Step 9 --- Login to Hugging Face

``` bash
hf auth login
```

-   Choose **"Log in with your browser"**
-   Complete the login in your browser
-   Return to the terminal and verify it shows **"Login successful"**

------------------------------------------------------------------------

### Step 10 --- Download the Dataset

``` bash
python download_dataset.py
```

> **Note:** The dataset is approximately **19.4 GB**, so download time
> depends on your internet connection.

------------------------------------------------------------------------

### Step 11 --- Verify Everything Works

``` bash
python explore_data.py
```

This verifies the dataset and generates sample images.

------------------------------------------------------------------------

## 📋 Quick Summary

  Step   Command
  ------ -----------------------------------
  1      `git clone <repo-link>`
  2      `py install 3.11`
  3      `py -3.11 -m venv venv`
  4      `venv\Scripts\activate`
  5      `pip install -r requirements.txt`
  6      `hf auth login`
  7      `python download_dataset.py`
  8      `python explore_data.py`
