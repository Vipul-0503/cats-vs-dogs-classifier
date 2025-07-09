from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained CNN model
model = load_model('cats_vs_dogs_cnn.keras')

# Define upload folder path
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route – display the upload form
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_url = None

    if request.method == 'POST':
        # Get the uploaded image file
        file = request.files['file']
        if file:
            # Save the file to the uploads folder
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Load and preprocess the image
            img = image.load_img(filepath, target_size=(150, 150))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

            # Make prediction
            result = model.predict(img_array)[0][0]

            # Interpret the result
            prediction = "It's a 🐶 Dog!" if result > 0.5 else "It's a 🐱 Cat!"
            image_url = filepath

    return render_template('index.html', prediction=prediction, image_url=image_url)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
