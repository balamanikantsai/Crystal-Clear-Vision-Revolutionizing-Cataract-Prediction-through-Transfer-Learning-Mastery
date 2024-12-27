from flask import Flask, request, render_template, redirect, url_for
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.xception import preprocess_input
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

# Load your pre-trained model (make sure to load it only once)
model = load_model('VGG19.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pred')
def pred():
    return render_template('details.html')

@app.route('/output', methods=['POST'])
def output():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read the file content into memory
            file_content = file.read()
            image = Image.open(io.BytesIO(file_content))
            image = image.resize((224, 224))
            img_array = img_to_array(image)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # Predict using the pre-trained model
            preds = model.predict(img_array)
            print(preds[0])
            print(preds[0][0])

            result = 'Cataract was found, kindly consult a doctor.' if preds[0][0] < 0.5 else 'Congrats, Eye is normal.'
            print(result)
            return render_template("resu.html", result=result)
        else:
            return "No file uploaded", 400

if __name__ == '__main__':
    app.run(debug=True)
