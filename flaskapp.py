
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import cv2
import numpy as np
import os

app = Flask(__name__)

# Load your machine learning model
dic = {0: 'Normal', 1: 'Doubtful', 2: 'Mild', 3: 'Moderate', 4: 'Severe'}
img_size = 256
model = load_model('model.h5')
model.make_predict_function()


def predict_label(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (img_size, img_size))
    i = image.img_to_array(resized) / 255.0
    i = i.reshape(1, img_size, img_size, 1)
    p = np.argmax(model.predict(i), axis=-1)
    return dic[p[0]]


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("band.html")

@app.route("/about")
def about_page():
    return "Diagnosis of Knee arthritis!"

@app.route("/predict", methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        img = request.files['file']
        if img.filename == '':
            return "No selected file"
        img_path = os.path.join("uploads", img.filename)
        img.save(img_path)
        try:
            p = predict_label(img_path)
            return str(p).lower()
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)

