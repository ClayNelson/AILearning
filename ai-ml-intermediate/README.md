# AI/ML Intermediate Learning Path

## 🎯 Overview
Take your AI/ML skills to the next level! This path covers advanced topics, specialized domains, and real-world applications. Perfect for those who have completed the beginner path or have equivalent experience.

## 📋 Prerequisites
- Solid understanding of basic ML algorithms (regression, classification, clustering)
- Experience with Python, pandas, scikit-learn, and basic TensorFlow/Keras
- Familiarity with linear algebra and statistics concepts
- Completed at least 2-3 ML projects
- 12-15 hours per week commitment

## 🧠 Advanced Topics You'll Master
- Deep Learning architectures (CNNs, RNNs, Transformers)
- Natural Language Processing and Computer Vision
- Generative AI fundamentals
- Model deployment and MLOps
- AI Ethics and Responsible AI

## 🚀 Setup Instructions

### Advanced Environment Setup
```bash
# Create advanced ML environment
python -m venv advanced-ml
source advanced-ml/bin/activate

# Core libraries
pip install numpy pandas matplotlib seaborn scikit-learn
pip install tensorflow torch torchvision transformers
pip install opencv-python pillow
pip install nltk spacy gensim
pip install streamlit flask fastapi
pip install mlflow wandb tensorboard

# For deployment
pip install docker-compose
pip install boto3 google-cloud-storage azure-storage-blob
```

### GPU Setup (Recommended)
```bash
# For TensorFlow GPU
pip install tensorflow-gpu

# For PyTorch GPU (check pytorch.org for your system)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## 📚 Week 1-2: Advanced Deep Learning

### Convolutional Neural Networks (CNNs) Deep Dive
```python
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Advanced CNN Architecture
def create_advanced_cnn(input_shape, num_classes):
    model = models.Sequential([
        # First conv block
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.BatchNormalization(),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Second conv block
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Third conv block
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),
        
        # Classifier
        layers.GlobalAveragePooling2D(),
        layers.Dense(512, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Data Augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1./255)

# Advanced callbacks
callbacks = [
    callbacks.EarlyStopping(patience=10, restore_best_weights=True),
    callbacks.ReduceLROnPlateau(factor=0.2, patience=5),
    callbacks.ModelCheckpoint('best_model.h5', save_best_only=True)
]
```

### Transfer Learning and Fine-tuning
```python
from tensorflow.keras.applications import ResNet50, VGG16, InceptionV3

# Load pre-trained model
base_model = ResNet50(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze base model
base_model.trainable = False

# Add custom classifier
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(num_classes, activation='softmax')
])

# Compile and train
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Initial training
history1 = model.fit(train_data, validation_data=val_data, epochs=10)

# Fine-tuning: unfreeze some layers
base_model.trainable = True
for layer in base_model.layers[:-10]:
    layer.trainable = False

# Use lower learning rate for fine-tuning
model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Continue training
history2 = model.fit(train_data, validation_data=val_data, epochs=10)
```

### Recurrent Neural Networks (RNNs, LSTMs, GRU)
```python
from tensorflow.keras.layers import LSTM, GRU, Bidirectional, Embedding

# Text classification with LSTM
def create_text_classifier(vocab_size, embedding_dim, max_length, num_classes):
    model = models.Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        Bidirectional(LSTM(64, dropout=0.3, recurrent_dropout=0.3)),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Time series prediction with GRU
def create_time_series_model(n_features, n_timesteps):
    model = models.Sequential([
        GRU(50, return_sequences=True, input_shape=(n_timesteps, n_features)),
        layers.Dropout(0.2),
        GRU(50, return_sequences=True),
        layers.Dropout(0.2),
        GRU(50),
        layers.Dropout(0.2),
        layers.Dense(1)
    ])
    return model

# Advanced sequence-to-sequence model
def create_seq2seq_model(encoder_vocab_size, decoder_vocab_size, embedding_dim):
    # Encoder
    encoder_inputs = layers.Input(shape=(None,))
    encoder_embedding = Embedding(encoder_vocab_size, embedding_dim)(encoder_inputs)
    encoder_lstm = LSTM(256, return_state=True)
    encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding)
    encoder_states = [state_h, state_c]
    
    # Decoder
    decoder_inputs = layers.Input(shape=(None,))
    decoder_embedding = Embedding(decoder_vocab_size, embedding_dim)
    decoder_lstm = LSTM(256, return_sequences=True, return_state=True)
    decoder_dense = layers.Dense(decoder_vocab_size, activation='softmax')
    
    decoder_embedding_layer = decoder_embedding(decoder_inputs)
    decoder_outputs, _, _ = decoder_lstm(decoder_embedding_layer, initial_state=encoder_states)
    decoder_outputs = decoder_dense(decoder_outputs)
    
    model = models.Model([encoder_inputs, decoder_inputs], decoder_outputs)
    return model
```

**Week 1-2 Project: Advanced Image Classification System**

Build a state-of-the-art image classifier:
- Use transfer learning with multiple architectures
- Implement advanced data augmentation
- Apply ensemble methods
- Deploy model with web interface

## 📚 Week 3-4: Natural Language Processing

### Text Preprocessing and Feature Engineering
```python
import nltk
import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

class TextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
    
    def clean_text(self, text):
        # Remove HTML tags
        text = re.sub(r'<.*?>', '', text)
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def tokenize_and_lemmatize(self, text):
        doc = nlp(text)
        tokens = [token.lemma_ for token in doc 
                 if not token.is_stop and not token.is_punct and len(token.text) > 2]
        return ' '.join(tokens)
    
    def preprocess(self, texts):
        processed_texts = []
        for text in texts:
            clean = self.clean_text(text)
            lemmatized = self.tokenize_and_lemmatize(clean)
            processed_texts.append(lemmatized)
        return processed_texts

# Usage
preprocessor = TextPreprocessor()
processed_texts = preprocessor.preprocess(raw_texts)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))
X_tfidf = tfidf.fit_transform(processed_texts)
```

### Word Embeddings (Word2Vec, GloVe, FastText)
```python
from gensim.models import Word2Vec, FastText
import numpy as np

# Train Word2Vec model
sentences = [text.split() for text in processed_texts]
w2v_model = Word2Vec(
    sentences=sentences,
    vector_size=300,
    window=5,
    min_count=1,
    workers=4,
    sg=1  # Skip-gram
)

# Get word vectors
def get_word_vector(word):
    try:
        return w2v_model.wv[word]
    except KeyError:
        return np.zeros(300)

# Document embeddings using averaging
def document_vector(doc):
    vectors = [get_word_vector(word) for word in doc.split()]
    return np.mean(vectors, axis=0)

# Using pre-trained embeddings
def load_glove_embeddings(glove_file):
    embeddings = {}
    with open(glove_file, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.array(values[1:], dtype='float32')
            embeddings[word] = vector
    return embeddings

# Create embedding matrix for neural networks
def create_embedding_matrix(tokenizer, embeddings_dict, embedding_dim):
    vocab_size = len(tokenizer.word_index) + 1
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    
    for word, i in tokenizer.word_index.items():
        embedding_vector = embeddings_dict.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
    
    return embedding_matrix
```

### Sentiment Analysis with Deep Learning
```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Advanced sentiment analysis model
class SentimentAnalyzer:
    def __init__(self, max_features=10000, maxlen=500):
        self.max_features = max_features
        self.maxlen = maxlen
        self.tokenizer = Tokenizer(num_words=max_features)
        
    def preprocess_texts(self, texts):
        self.tokenizer.fit_on_texts(texts)
        sequences = self.tokenizer.texts_to_sequences(texts)
        return pad_sequences(sequences, maxlen=self.maxlen)
    
    def build_model(self, embedding_matrix=None):
        model = models.Sequential()
        
        if embedding_matrix is not None:
            model.add(Embedding(
                input_dim=self.max_features,
                output_dim=embedding_matrix.shape[1],
                weights=[embedding_matrix],
                input_length=self.maxlen,
                trainable=False
            ))
        else:
            model.add(Embedding(self.max_features, 128, input_length=self.maxlen))
        
        model.add(Bidirectional(LSTM(64, dropout=0.3, recurrent_dropout=0.3)))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(1, activation='sigmoid'))
        
        model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        return model

# Attention mechanism implementation
class AttentionLayer(layers.Layer):
    def __init__(self):
        super(AttentionLayer, self).__init__()
    
    def build(self, input_shape):
        self.attention_weights = self.add_weight(
            name='attention_weights',
            shape=(input_shape[-1], 1),
            initializer='random_normal',
            trainable=True
        )
        super(AttentionLayer, self).build(input_shape)
    
    def call(self, inputs):
        attention_scores = tf.nn.tanh(tf.matmul(inputs, self.attention_weights))
        attention_weights = tf.nn.softmax(attention_scores, axis=1)
        context_vector = tf.reduce_sum(inputs * attention_weights, axis=1)
        return context_vector
```

### Named Entity Recognition (NER)
```python
import spacy
from spacy.training import Example

# Custom NER training
def train_custom_ner(nlp, train_data, iterations=100):
    # Add the NER pipe to the model if it doesn't exist
    if 'ner' not in nlp.pipe_names:
        ner = nlp.add_pipe('ner', last=True)
    else:
        ner = nlp.get_pipe('ner')
    
    # Add labels to the NER pipe
    for _, annotations in train_data:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])
    
    # Training the model
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            losses = {}
            for text, annotations in train_data:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], losses=losses, drop=0.5)
    
    return nlp

# Extract entities from text
def extract_entities(text, nlp_model):
    doc = nlp_model(text)
    entities = []
    for ent in doc.ents:
        entities.append({
            'text': ent.text,
            'label': ent.label_,
            'start': ent.start_char,
            'end': ent.end_char
        })
    return entities
```

**Week 3-4 Project: Chatbot or Sentiment Analyzer**

Build an intelligent text processing application:
- Implement multiple NLP techniques
- Create a conversational interface
- Add context understanding
- Deploy as a web application

## 📚 Week 5-6: Computer Vision

### Advanced Image Processing
```python
import cv2
import numpy as np
from skimage import filters, morphology, segmentation
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self):
        pass
    
    def enhance_image(self, image):
        # Histogram equalization
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(gray)
        
        # Noise reduction
        denoised = cv2.bilateralFilter(equalized, 9, 75, 75)
        
        # Sharpening
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpened = cv2.filter2D(denoised, -1, kernel)
        
        return sharpened
    
    def detect_edges(self, image, method='canny'):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        if method == 'canny':
            edges = cv2.Canny(gray, 50, 150)
        elif method == 'sobel':
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            edges = np.sqrt(sobelx**2 + sobely**2)
        
        return edges
    
    def segment_image(self, image, method='watershed'):
        if method == 'watershed':
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray, 0, 255, 
                                      cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            
            # Remove noise
            kernel = np.ones((3,3), np.uint8)
            opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
            
            # Sure background area
            sure_bg = cv2.dilate(opening, kernel, iterations=3)
            
            # Sure foreground area
            dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
            ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
            
            # Unknown region
            sure_fg = np.uint8(sure_fg)
            unknown = cv2.subtract(sure_bg, sure_fg)
            
            # Marker labelling
            ret, markers = cv2.connectedComponents(sure_fg)
            markers = markers + 1
            markers[unknown == 255] = 0
            
            markers = cv2.watershed(image, markers)
            image[markers == -1] = [255, 0, 0]  # Mark boundaries in red
            
            return image
```

### Object Detection with YOLO
```python
import cv2
import numpy as np

class YOLODetector:
    def __init__(self, weights_path, config_path, classes_path):
        self.net = cv2.dnn.readNet(weights_path, config_path)
        with open(classes_path, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]
        
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] 
                            for i in self.net.getUnconnectedOutLayers()]
        
        # Generate random colors for each class
        self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
    
    def detect_objects(self, image, confidence_threshold=0.5, nms_threshold=0.4):
        height, width, channels = image.shape
        
        # Prepare image for detection
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)
        
        # Process detections
        boxes = []
        confidences = []
        class_ids = []
        
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > confidence_threshold:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        # Apply non-max suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
        
        # Draw bounding boxes
        if len(indices) > 0:
            for i in indices.flatten():
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                confidence = confidences[i]
                color = self.colors[class_ids[i]]
                
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                cv2.putText(image, f"{label} {confidence:.2f}", (x, y - 10),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        return image, boxes, confidences, class_ids
```

### Image Classification with Custom CNN
```python
# Advanced CNN with attention mechanism
class AttentionCNN(tf.keras.Model):
    def __init__(self, num_classes):
        super(AttentionCNN, self).__init__()
        
        # Feature extraction layers
        self.conv1 = layers.Conv2D(32, (3, 3), activation='relu')
        self.bn1 = layers.BatchNormalization()
        self.pool1 = layers.MaxPooling2D((2, 2))
        
        self.conv2 = layers.Conv2D(64, (3, 3), activation='relu')
        self.bn2 = layers.BatchNormalization()
        self.pool2 = layers.MaxPooling2D((2, 2))
        
        self.conv3 = layers.Conv2D(128, (3, 3), activation='relu')
        self.bn3 = layers.BatchNormalization()
        self.pool3 = layers.MaxPooling2D((2, 2))
        
        # Attention mechanism
        self.attention_conv = layers.Conv2D(1, (1, 1), activation='sigmoid')
        
        # Classification layers
        self.global_pool = layers.GlobalAveragePooling2D()
        self.fc1 = layers.Dense(128, activation='relu')
        self.dropout = layers.Dropout(0.5)
        self.fc2 = layers.Dense(num_classes, activation='softmax')
    
    def call(self, x):
        # Feature extraction
        x = self.pool1(self.bn1(self.conv1(x)))
        x = self.pool2(self.bn2(self.conv2(x)))
        x = self.pool3(self.bn3(self.conv3(x)))
        
        # Attention mechanism
        attention_weights = self.attention_conv(x)
        x = x * attention_weights  # Apply attention
        
        # Classification
        x = self.global_pool(x)
        x = self.fc1(x)
        x = self.dropout(x)
        x = self.fc2(x)
        
        return x

# Model training with advanced techniques
def train_advanced_model(model, train_data, val_data, epochs=50):
    # Advanced callbacks
    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(factor=0.2, patience=5, min_lr=1e-7),
        tf.keras.callbacks.ModelCheckpoint('best_model.h5', save_best_only=True)
    ]
    
    # Compile model
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Train model
    history = model.fit(
        train_data,
        validation_data=val_data,
        epochs=epochs,
        callbacks=callbacks
    )
    
    return history
```

**Week 5-6 Project: Real-time Object Detection Application**

Create a computer vision application:
- Implement real-time object detection
- Add face recognition capabilities
- Create a GUI with OpenCV/Tkinter
- Process video streams from webcam

## 📚 Week 7-8: Advanced Topics & Generative AI

### Introduction to Generative Adversarial Networks (GANs)
```python
# Simple GAN implementation
class Generator(tf.keras.Model):
    def __init__(self, latent_dim):
        super(Generator, self).__init__()
        self.latent_dim = latent_dim
        
        self.dense1 = layers.Dense(7 * 7 * 256, use_bias=False)
        self.bn1 = layers.BatchNormalization()
        self.leaky_relu1 = layers.LeakyReLU()
        
        self.reshape = layers.Reshape((7, 7, 256))
        
        self.conv_transpose1 = layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), 
                                                    padding='same', use_bias=False)
        self.bn2 = layers.BatchNormalization()
        self.leaky_relu2 = layers.LeakyReLU()
        
        self.conv_transpose2 = layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), 
                                                    padding='same', use_bias=False)
        self.bn3 = layers.BatchNormalization()
        self.leaky_relu3 = layers.LeakyReLU()
        
        self.conv_transpose3 = layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), 
                                                    padding='same', use_bias=False, 
                                                    activation='tanh')
    
    def call(self, x):
        x = self.dense1(x)
        x = self.bn1(x)
        x = self.leaky_relu1(x)
        
        x = self.reshape(x)
        
        x = self.conv_transpose1(x)
        x = self.bn2(x)
        x = self.leaky_relu2(x)
        
        x = self.conv_transpose2(x)
        x = self.bn3(x)
        x = self.leaky_relu3(x)
        
        x = self.conv_transpose3(x)
        
        return x

class Discriminator(tf.keras.Model):
    def __init__(self):
        super(Discriminator, self).__init__()
        
        self.conv1 = layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same')
        self.leaky_relu1 = layers.LeakyReLU()
        self.dropout1 = layers.Dropout(0.3)
        
        self.conv2 = layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same')
        self.leaky_relu2 = layers.LeakyReLU()
        self.dropout2 = layers.Dropout(0.3)
        
        self.flatten = layers.Flatten()
        self.dense = layers.Dense(1)
    
    def call(self, x):
        x = self.conv1(x)
        x = self.leaky_relu1(x)
        x = self.dropout1(x)
        
        x = self.conv2(x)
        x = self.leaky_relu2(x)
        x = self.dropout2(x)
        
        x = self.flatten(x)
        x = self.dense(x)
        
        return x

# GAN training loop
class GAN:
    def __init__(self, latent_dim):
        self.latent_dim = latent_dim
        self.generator = Generator(latent_dim)
        self.discriminator = Discriminator()
        
        self.gen_optimizer = tf.keras.optimizers.Adam(1e-4)
        self.disc_optimizer = tf.keras.optimizers.Adam(1e-4)
    
    @tf.function
    def train_step(self, real_images):
        batch_size = tf.shape(real_images)[0]
        
        # Generate random noise
        noise = tf.random.normal([batch_size, self.latent_dim])
        
        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            generated_images = self.generator(noise, training=True)
            
            real_output = self.discriminator(real_images, training=True)
            fake_output = self.discriminator(generated_images, training=True)
            
            gen_loss = self.generator_loss(fake_output)
            disc_loss = self.discriminator_loss(real_output, fake_output)
        
        gradients_of_generator = gen_tape.gradient(gen_loss, self.generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(disc_loss, self.discriminator.trainable_variables)
        
        self.gen_optimizer.apply_gradients(zip(gradients_of_generator, self.generator.trainable_variables))
        self.disc_optimizer.apply_gradients(zip(gradients_of_discriminator, self.discriminator.trainable_variables))
        
        return gen_loss, disc_loss
    
    def generator_loss(self, fake_output):
        return tf.keras.losses.BinaryCrossentropy(from_logits=True)(tf.ones_like(fake_output), fake_output)
    
    def discriminator_loss(self, real_output, fake_output):
        real_loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)(tf.ones_like(real_output), real_output)
        fake_loss = tf.keras.losses.BinaryCrossentropy(from_logits=True)(tf.zeros_like(fake_output), fake_output)
        total_loss = real_loss + fake_loss
        return total_loss
```

### Model Deployment and MLOps
```python
# Model serving with Flask
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        probability = model.predict_proba(features).max()
        
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': float(probability),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 400

# Model deployment with Docker
dockerfile_content = """
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
"""

# MLflow for experiment tracking
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient

def log_experiment(model, X_test, y_test, params):
    with mlflow.start_run():
        # Log parameters
        for key, value in params.items():
            mlflow.log_param(key, value)
        
        # Log metrics
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        mlflow.log_metric("accuracy", accuracy)
        
        # Log model
        mlflow.sklearn.log_model(model, "model")
        
        return mlflow.active_run().info.run_id

# A/B Testing framework
class ABTestFramework:
    def __init__(self, models):
        self.models = models
        self.traffic_split = len(models)
    
    def predict(self, features, user_id=None):
        # Route traffic based on user_id hash
        model_index = hash(str(user_id)) % self.traffic_split
        model = self.models[model_index]
        
        prediction = model.predict(features)
        
        # Log for analysis
        self.log_prediction(user_id, model_index, features, prediction)
        
        return prediction
    
    def log_prediction(self, user_id, model_index, features, prediction):
        # Log to database or file for later analysis
        pass
```

### AI Ethics and Bias Detection
```python
# Bias detection toolkit
from sklearn.metrics import confusion_matrix
import pandas as pd

class BiasDetector:
    def __init__(self, model, sensitive_features):
        self.model = model
        self.sensitive_features = sensitive_features
    
    def detect_demographic_parity(self, X, y, predictions):
        results = {}
        
        for feature in self.sensitive_features:
            groups = X[feature].unique()
            positive_rates = {}
            
            for group in groups:
                mask = X[feature] == group
                positive_rate = predictions[mask].mean()
                positive_rates[group] = positive_rate
            
            # Calculate parity difference
            max_rate = max(positive_rates.values())
            min_rate = min(positive_rates.values())
            parity_diff = max_rate - min_rate
            
            results[feature] = {
                'positive_rates': positive_rates,
                'parity_difference': parity_diff,
                'fair': parity_diff < 0.1  # 10% threshold
            }
        
        return results
    
    def detect_equalized_odds(self, X, y, predictions):
        results = {}
        
        for feature in self.sensitive_features:
            groups = X[feature].unique()
            tpr_fpr = {}
            
            for group in groups:
                mask = X[feature] == group
                y_true_group = y[mask]
                y_pred_group = predictions[mask]
                
                tn, fp, fn, tp = confusion_matrix(y_true_group, y_pred_group).ravel()
                tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
                fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
                
                tpr_fpr[group] = {'tpr': tpr, 'fpr': fpr}
            
            results[feature] = tpr_fpr
        
        return results
    
    def generate_fairness_report(self, X, y, predictions):
        demographic_parity = self.detect_demographic_parity(X, y, predictions)
        equalized_odds = self.detect_equalized_odds(X, y, predictions)
        
        report = {
            'demographic_parity': demographic_parity,
            'equalized_odds': equalized_odds,
            'overall_accuracy': (predictions == y).mean(),
            'recommendations': self.generate_recommendations(demographic_parity)
        }
        
        return report
    
    def generate_recommendations(self, demographic_parity):
        recommendations = []
        
        for feature, results in demographic_parity.items():
            if not results['fair']:
                recommendations.append(
                    f"Consider rebalancing data or using fairness constraints for {feature}"
                )
        
        return recommendations

# Explainable AI with LIME
from lime.lime_tabular import LimeTabularExplainer

class ModelExplainer:
    def __init__(self, model, X_train, feature_names):
        self.model = model
        self.explainer = LimeTabularExplainer(
            X_train,
            feature_names=feature_names,
            class_names=['Class 0', 'Class 1'],
            mode='classification'
        )
    
    def explain_instance(self, instance, num_features=5):
        explanation = self.explainer.explain_instance(
            instance, 
            self.model.predict_proba, 
            num_features=num_features
        )
        return explanation
    
    def explain_batch(self, X_test, num_samples=10):
        explanations = []
        for i in range(min(num_samples, len(X_test))):
            exp = self.explain_instance(X_test[i])
            explanations.append(exp)
        return explanations
```

**Week 7-8 Project: Deploy ML Model as Web Service**

Create a complete ML deployment pipeline:
- Train and validate a model
- Implement bias detection and explainability
- Create REST API with Flask/FastAPI
- Add model monitoring and logging
- Deploy with Docker

## 📚 Week 9-10: Capstone Project

### Project Ideas
1. **Multi-modal AI Assistant**: Combines text, image, and audio processing
2. **Real-time Recommendation System**: Uses multiple ML techniques
3. **Computer Vision Security System**: Object detection, face recognition, anomaly detection
4. **Natural Language Understanding Platform**: NER, sentiment analysis, question answering
5. **Automated Trading System**: Time series analysis, reinforcement learning

### Project Requirements
- [ ] Use at least 3 different ML techniques learned in this path
- [ ] Implement proper data pipeline and preprocessing
- [ ] Include model evaluation and bias detection
- [ ] Create user-friendly interface (web app or mobile)
- [ ] Deploy to cloud platform (AWS, GCP, or Azure)
- [ ] Document code and create presentation

### Presentation Guidelines
- Problem statement and motivation
- Data exploration and preprocessing approach
- Model architecture and training process
- Results and evaluation metrics
- Ethical considerations and bias analysis
- Future improvements and scalability

## 🎯 Learning Outcomes

Upon completion, you will have:

### Advanced Technical Skills
- [ ] Deep understanding of neural network architectures
- [ ] Expertise in computer vision and NLP applications
- [ ] Knowledge of generative AI and GANs
- [ ] Experience with model deployment and MLOps
- [ ] Understanding of AI ethics and bias detection

### Professional Skills
- [ ] Ability to lead ML projects from conception to deployment
- [ ] Experience with cloud platforms and containerization
- [ ] Knowledge of A/B testing and model monitoring
- [ ] Skills in explaining AI models to non-technical stakeholders
- [ ] Understanding of responsible AI practices

## 🎓 Career Paths

This path prepares you for roles such as:
- **Machine Learning Engineer**
- **AI Research Scientist**
- **Computer Vision Engineer**
- **NLP Engineer**
- **Data Scientist (Advanced)**
- **AI Product Manager**

## 📚 Advanced Resources

### Research Papers & Conferences
- arXiv.org for latest research papers
- NeurIPS, ICML, ICLR conference proceedings
- Papers With Code for implementations

### Advanced Courses
- Stanford CS229 Machine Learning
- MIT 6.034 Artificial Intelligence
- Fast.ai Deep Learning for Coders Part 2

### Professional Development
- Kaggle competitions
- Open source contributions
- AI conference presentations
- Technical blog writing

---

**Congratulations on completing the Advanced AI/ML Path!** You're now equipped with cutting-edge skills in artificial intelligence and ready to tackle the most challenging problems in the field.