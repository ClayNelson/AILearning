# AI/ML Beginner Learning Path

## 🎯 Overview
This path introduces you to the exciting world of Artificial Intelligence and Machine Learning. Perfect for those who have completed the Python Fundamentals path or have equivalent programming experience.

## 📋 Prerequisites
- Solid Python fundamentals (variables, functions, data structures, OOP basics)
- Basic understanding of mathematics (algebra, basic statistics)
- Familiarity with data manipulation (pandas recommended)
- 8-12 hours per week commitment

## 🧠 What You'll Learn
By the end of this path, you'll understand core ML concepts and be able to build your own predictive models!

## 🚀 Setup Instructions

### 1. Install Required Libraries
```bash
# Create a virtual environment
python -m venv ml-env
source ml-env/bin/activate  # On Windows: ml-env\Scripts\activate

# Install core libraries
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
pip install tensorflow keras  # For deep learning section
```

### 2. Download Practice Datasets
We'll work with real datasets throughout this course. Popular sources:
- Kaggle.com (create free account)
- UCI Machine Learning Repository
- Built-in scikit-learn datasets

### 3. Set Up Jupyter Environment
```bash
# Install and run Jupyter
pip install jupyter notebook
jupyter notebook
```

## 📚 Week 1-2: AI Foundations

### Understanding AI, ML, and Deep Learning
```
Artificial Intelligence (AI)
├── Machine Learning (ML)
│   ├── Supervised Learning
│   ├── Unsupervised Learning
│   └── Reinforcement Learning
└── Deep Learning (DL)
    ├── Neural Networks
    ├── CNNs (Computer Vision)
    └── RNNs (Natural Language)
```

### Key Concepts to Master:
- [ ] **What is Machine Learning?**
  - Algorithms that learn from data
  - Difference from traditional programming
  - Real-world applications

- [ ] **Types of Machine Learning:**
  - **Supervised**: Learning with labeled examples (input → output)
  - **Unsupervised**: Finding patterns in unlabeled data
  - **Reinforcement**: Learning through interaction and rewards

### Python Libraries Overview
```python
import numpy as np          # Numerical computing
import pandas as pd         # Data manipulation
import matplotlib.pyplot as plt  # Basic plotting
import seaborn as sns       # Statistical visualization
from sklearn import datasets, model_selection, metrics
```

### Data Preprocessing Fundamentals
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load data
df = pd.read_csv('data.csv')

# Explore data
print(df.head())
print(df.info())
print(df.describe())

# Handle missing values
df.fillna(df.mean(), inplace=True)  # For numerical
df.fillna(df.mode().iloc[0], inplace=True)  # For categorical

# Encode categorical variables
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# Scale numerical features
scaler = StandardScaler()
df[['feature1', 'feature2']] = scaler.fit_transform(df[['feature1', 'feature2']])
```

**Week 1-2 Project: Exploratory Data Analysis**

Choose a dataset and perform comprehensive EDA:
- Data cleaning and preprocessing
- Statistical summaries
- Visualizations to understand patterns
- Identify potential features for ML models

## 📚 Week 3-4: Supervised Learning

### Linear Regression
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Prepare data
X = df[['feature1', 'feature2']]  # Features
y = df['target']                  # Target variable

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse:.2f}, R²: {r2:.2f}")
```

### Logistic Regression
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Binary classification
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")
print(classification_report(y_test, y_pred))
```

### Decision Trees and Random Forests
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Cross-validation
cv_scores = cross_val_score(rf_model, X, y, cv=5)
print(f"CV Score: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
```

### Model Evaluation Techniques
```python
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# ROC Curve for binary classification
from sklearn.metrics import roc_curve, auc
fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

**Week 3-4 Project: House Price Prediction**

Build a regression model to predict house prices:
- Use real estate dataset
- Feature engineering (creating new features)
- Compare multiple algorithms
- Optimize hyperparameters
- Evaluate model performance

## 📚 Week 5-6: More ML Algorithms & Unsupervised Learning

### Support Vector Machines (SVM)
```python
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

# SVM with hyperparameter tuning
param_grid = {
    'C': [0.1, 1, 10],
    'gamma': ['scale', 'auto', 0.1, 1],
    'kernel': ['rbf', 'linear']
}

svm_model = SVC()
grid_search = GridSearchCV(svm_model, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.3f}")
```

### K-Nearest Neighbors (KNN)
```python
from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Find optimal k value
k_values = range(1, 21)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5)
    accuracies.append(scores.mean())

# Plot results
plt.plot(k_values, accuracies)
plt.xlabel('k Value')
plt.ylabel('Cross-Validation Accuracy')
plt.title('Finding Optimal k Value')
plt.show()
```

### Clustering (K-Means)
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Find optimal number of clusters
inertias = []
silhouette_scores = []
k_range = range(2, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))

# Elbow method
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(k_range, inertias, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')

plt.subplot(1, 2, 2)
plt.plot(k_range, silhouette_scores, marker='o')
plt.title('Silhouette Score')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.show()

# Apply K-means
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
cluster_labels = kmeans.fit_predict(X)

# Visualize clusters
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
           marker='x', s=300, linewidths=3, color='red')
plt.title('K-Means Clustering Results')
plt.show()
```

### Feature Selection and Engineering
```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import PolynomialFeatures

# Feature selection
selector = SelectKBest(score_func=f_classif, k=5)
X_selected = selector.fit_transform(X, y)
selected_features = selector.get_support()

# Feature engineering - polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Feature importance from tree-based models
rf_model.fit(X, y)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance)
```

**Week 5-6 Project: Customer Segmentation Analysis**

Use unsupervised learning to segment customers:
- Apply K-means clustering
- Analyze customer behavior patterns
- Create customer personas
- Provide business insights

## 📚 Week 7-8: Introduction to Deep Learning

### Neural Network Fundamentals
```python
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler

# Prepare data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Build neural network
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')  # For binary classification
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
history = model.fit(
    X_scaled, y,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# Plot training history
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.legend()
plt.show()
```

### Simple Image Classification
```python
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize pixel values
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Convert labels to categorical
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Build CNN model
model = Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=32,
    validation_data=(x_test, y_test)
)
```

**Week 7-8 Project: Image Classification with Neural Networks**

Build a neural network to classify images:
- Use a real image dataset (flowers, animals, etc.)
- Implement data augmentation
- Compare simple neural network vs CNN
- Evaluate model performance

## 🎯 Key Learning Outcomes

After completing this path, you will be able to:

### Technical Skills
- [ ] Understand the difference between AI, ML, and Deep Learning
- [ ] Preprocess and clean real-world datasets
- [ ] Implement supervised learning algorithms (regression & classification)
- [ ] Apply unsupervised learning techniques (clustering)
- [ ] Evaluate model performance using appropriate metrics
- [ ] Perform feature selection and engineering
- [ ] Build basic neural networks with TensorFlow/Keras
- [ ] Create simple image classification models

### Practical Skills
- [ ] Choose appropriate algorithms for different problem types
- [ ] Avoid common pitfalls (overfitting, data leakage)
- [ ] Interpret model results and communicate findings
- [ ] Use cross-validation and hyperparameter tuning
- [ ] Work with real datasets from start to finish

## 🎓 Next Steps

After completing this path, you're ready for:
- **AI/ML Intermediate Path** - Advanced techniques and specialized domains
- **Deep Learning Specialization** - Neural networks, CNNs, RNNs
- **Data Science Track** - Advanced statistics and analytics
- **MLOps and Deployment** - Production machine learning systems

## 📚 Essential Resources

### Books
- "Hands-On Machine Learning" by Aurélien Géron
- "Introduction to Statistical Learning" by James, Witten, Hastie, Tibshirani
- "Pattern Recognition and Machine Learning" by Christopher Bishop

### Online Courses
- Andrew Ng's Machine Learning Course (Coursera)
- Fast.ai Machine Learning for Coders
- edX MIT Introduction to Machine Learning

### Practice Platforms
- Kaggle Competitions and Learn Modules
- Google Colab for free GPU access
- Papers With Code for latest research

### Communities
- r/MachineLearning (Reddit)
- ML Twitter community
- Kaggle Forums
- Stack Overflow

---

Remember: Machine Learning is both an art and a science. Focus on understanding concepts deeply rather than just memorizing algorithms. The goal is to solve real problems, not just achieve high accuracy scores!