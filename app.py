import os
from flask import Flask, render_template, request, redirect, url_for, session
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'secretkey123'  # Needed for session storage
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def process_image(path, operation, kernel_size):
    img = cv2.imread(path)
    if img is None:
        return None

    k = max(int(kernel_size), 2)
    kernel = np.ones((k, k), np.uint8)

    if operation == 'Erosion':
        result = cv2.erode(img, kernel)
    elif operation == 'Dilation':
        result = cv2.dilate(img, kernel)
    elif operation == 'Opening':
        result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    elif operation == 'Closing':
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    elif operation == 'Hit':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        # Hit: match foreground structure (white 255)
        result = cv2.morphologyEx(binary, cv2.MORPH_ERODE, kernel)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
    elif operation == 'Miss':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
        # Miss: match background structure (black 0)
        result = cv2.morphologyEx(binary, cv2.MORPH_ERODE, kernel)
        result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
    else:
        result = img

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
    cv2.imwrite(output_path, result)
    return output_path


@app.route('/', methods=['GET', 'POST'])
def index():
    result_path = None
    original_path = session.get('image_path')
    operation = request.form.get('operation', 'Erosion')
    kernel = request.form.get('kernel_size', 3)

    # If a new image is uploaded
    file = request.files.get('image')
    if file and file.filename:
        filename = secure_filename(file.filename)
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(original_path)
        session['image_path'] = original_path

    if original_path:
        result_path = process_image(original_path, operation, kernel)

    return render_template('index.html',
                           uploaded=bool(original_path),
                           original=original_path,
                           result=result_path,
                           operation=operation,
                           kernel=kernel)

@app.route('/reset')
def reset():
    session.pop('image_path', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
