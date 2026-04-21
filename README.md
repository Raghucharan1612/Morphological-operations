# Morphological Image Processor

This is a simple web-based application built using Flask and OpenCV that allows users to apply basic morphological operations on images. It provides an easy interface where you can upload an image, choose an operation, and instantly see the processed result.

## Features

* Upload any image from your system
* Apply morphological operations like:

  * Erosion
  * Dilation
  * Opening
  * Closing
  * Hit
  * Miss
* Adjustable kernel size for different effects
* Displays original and processed images side by side
* Reset option to try with a new image

## Tech Stack

* Python (Flask)
* OpenCV
* NumPy
* HTML, CSS (Frontend)

## How to Run

1. Clone the repository:

   ```
   git clone https://github.com/your-username/Morphological-operations.git
   ```

2. Navigate to the project folder:

   ```
   cd Morphological-operations
   ```

3. Install dependencies:

   ```
   pip install flask opencv-python numpy
   ```

4. Run the application:

   ```
   python app.py
   ```

5. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
morph_webapp/
│
├── static/
│   └── uploads/        # Stores uploaded and processed images
│
├── templates/
│   └── index.html      # Frontend UI
│
├── app.py              # Flask backend
└── README.md
```

## Notes

* Uploaded images are stored temporarily in the `static/uploads` folder.
* Make sure the folder exists before running the app.
* Kernel size should be between 2 and 20 for best results.

## Future Improvements

* Add more image processing operations
* Improve UI design
* Allow downloading processed images
* Add support for multiple file formats

---

This project was created as part of learning image processing and web integration using Flask.
