
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = keras.models.load_model('model.h5')

def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def classify_image(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions[0])
    return predicted_class

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if 'image' not in request.files:
        return "No image uploaded"
    image = request.files['image']
    image = Image.open(image)
    predicted_class = classify_image(image)
    return f"Predicted class: {predicted_class}"

if __name__ == '__main__':
    app.run()
