# Getting Started Guide

## 🚀 Quick Setup

This guide will help you set up your development environment for the AI Learning paths.

## 📋 Prerequisites

Before starting, ensure you have:
- Computer with Windows, macOS, or Linux
- Internet connection for downloading tools
- At least 4GB RAM (8GB recommended for AI/ML work)
- 5GB free disk space

## 🐍 Python Installation

### Step 1: Download Python
1. Go to [python.org](https://python.org)
2. Download Python 3.9 or higher
3. **Important**: Check "Add Python to PATH" during installation

### Step 2: Verify Installation
Open terminal/command prompt and run:
```bash
python --version
pip --version
```

You should see version numbers displayed.

### Alternative: Using Anaconda (Recommended for Data Science)
1. Download [Anaconda](https://www.anaconda.com/products/distribution)
2. Install with default settings
3. Anaconda includes Python, Jupyter, and many data science packages

## 🛠 Development Environment Setup

### Option 1: VS Code (Recommended for Beginners)
1. Download [Visual Studio Code](https://code.visualstudio.com/)
2. Install these extensions:
   - Python (Microsoft)
   - Jupyter (Microsoft)
   - Python Docstring Generator
   - Code Runner

### Option 2: PyCharm Community Edition
1. Download [PyCharm](https://www.jetbrains.com/pycharm/)
2. Choose Community Edition (free)
3. Configure Python interpreter during setup

### Option 3: Jupyter Notebook
```bash
pip install jupyter notebook
jupyter notebook
```

## 📦 Package Management

### Creating Virtual Environments
Always use virtual environments to avoid package conflicts:

```bash
# Create virtual environment
python -m venv myproject-env

# Activate (Windows)
myproject-env\Scripts\activate

# Activate (macOS/Linux)
source myproject-env/bin/activate

# Deactivate when done
deactivate
```

### Installing Packages
```bash
# Basic data science stack
pip install numpy pandas matplotlib seaborn jupyter

# Machine learning essentials
pip install scikit-learn tensorflow opencv-python

# Web development
pip install flask streamlit

# Save installed packages
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

## 🎯 Learning Path Setup

### For Python Fundamentals Path
```bash
# Create project directory
mkdir python-learning
cd python-learning

# Create virtual environment
python -m venv python-env
source python-env/bin/activate  # Windows: python-env\Scripts\activate

# Install basic packages
pip install jupyter matplotlib pandas
```

### For AI/ML Paths
```bash
# Create ML environment
mkdir ai-ml-learning
cd ai-ml-learning

# Create virtual environment
python -m venv ml-env
source ml-env/bin/activate  # Windows: ml-env\Scripts\activate

# Install ML packages
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
pip install tensorflow keras opencv-python nltk spacy

# For GPU support (optional)
pip install tensorflow-gpu torch torchvision
```

## ☁️ Cloud Options

### Google Colab (Free)
- No installation required
- Free GPU access
- Go to [colab.research.google.com](https://colab.research.google.com)
- Great for AI/ML experiments

### Kaggle Notebooks (Free)
- No installation required
- Free GPU and TPU access
- Built-in datasets
- Go to [kaggle.com/code](https://kaggle.com/code)

## 🔧 Git Setup (Recommended)

```bash
# Install Git
# Windows: Download from git-scm.com
# macOS: brew install git
# Linux: apt install git

# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Create repository
git init my-ai-learning
cd my-ai-learning
git add .
git commit -m "Initial commit"
```

## 🧪 Testing Your Setup

### Test Python Installation
Create `test_setup.py`:
```python
import sys
print(f"Python version: {sys.version}")

# Test basic packages
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    print("✅ Basic packages working!")
except ImportError as e:
    print(f"❌ Missing package: {e}")

# Test ML packages (for ML paths)
try:
    import sklearn
    import tensorflow as tf
    print("✅ ML packages working!")
    print(f"TensorFlow version: {tf.__version__}")
except ImportError as e:
    print(f"❌ Missing ML package: {e}")
```

Run it:
```bash
python test_setup.py
```

## 📚 Recommended Directory Structure

```
ai-learning/
├── python-fundamentals/
│   ├── week1-basics/
│   ├── week2-data-structures/
│   └── projects/
├── ai-ml-beginner/
│   ├── week1-foundations/
│   ├── week2-supervised/
│   └── projects/
├── ai-ml-intermediate/
│   ├── deep-learning/
│   ├── nlp/
│   └── computer-vision/
├── datasets/
├── notebooks/
└── utils/
```

## 🚨 Common Issues and Solutions

### Issue: Python not found
**Solution**: Ensure Python is in your PATH. Reinstall with "Add to PATH" option.

### Issue: Package installation fails
**Solutions**:
- Update pip: `python -m pip install --upgrade pip`
- Use virtual environment
- Check internet connection
- Try: `pip install --user package_name`

### Issue: Jupyter doesn't start
**Solutions**:
- Ensure Jupyter is installed: `pip install jupyter`
- Try: `jupyter notebook --ip=0.0.0.0`
- Check firewall settings

### Issue: Import errors
**Solutions**:
- Verify package installation: `pip list`
- Check virtual environment is activated
- Reinstall package: `pip uninstall package_name && pip install package_name`

## 🎯 Next Steps

1. **Choose Your Path**: Start with Python Fundamentals if new to programming
2. **Set Up Environment**: Follow setup instructions for your chosen path
3. **Start First Project**: Begin with provided project templates
4. **Join Community**: Connect with other learners online
5. **Practice Daily**: Consistency is key to success!

## 📞 Getting Help

- **Documentation**: Check official docs for Python, libraries
- **Stack Overflow**: Search for error messages and solutions
- **Reddit**: r/learnpython, r/MachineLearning
- **Discord**: Join Python and AI learning servers
- **GitHub Issues**: Report problems with specific projects

---

**You're all set!** 🚀 Your development environment is ready for an amazing learning journey in AI and programming!