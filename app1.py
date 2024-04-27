from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import pytesseract
import cv2
from predictions import getPredictions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    
    if image is None:
        return jsonify({'error': 'Failed to load image'})
    
    img_result, entities = getPredictions(image)
    
    # Save the processed image if needed
    cv2.imwrite('processed_image.jpg', img_result)
    
    return jsonify(entities)

if __name__ == '__main__':
    app.run(debug=True)