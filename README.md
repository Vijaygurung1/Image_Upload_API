
# Image Upload and Description Generation API


This project is a Flask-based API that allows users to upload images and receive multiple descriptions of the image in different tones using OpenAI's GPT models.

The API validates uploaded images, saves them locally and processes them to generate three types of descriptions:

1.A formal description.
2.A humorous description.
3.A critical description.
The API uses OpenAI's GPT model to generate these descriptions based on the image content.

# Features :

1.Image Upload: Supports uploading image files in PNG, JPG, and JPEG formats.
2.Image Validation: Ensures only valid image files are uploaded.
3.OpenAI Integration: Utilizes OpenAI's GPT model to generate different types of image descriptions.
4.JSON Response: Returns a structured JSON response with the image URL and descriptions categorized by tone (formal, humorous, and critical).

# Requirement.txt 

flask~=3.1.0
pillow~=11.0.0
openai~=1.55.1
werkzeug~=3.1.3


# env. 

I have kept my "OpenAI API key" inside my Python Code, which should not be shared publicly. However, you can check inside my code that I have shared.


# Technologies Used

1.Flask: A lightweight WSGI web application framework for Python.
2.OpenAI GPT: Used to generate descriptions for uploaded images in different tones.
3.Pillow: A Python Imaging Library used for image validation.
4.Python 3: The programming language used to build this project.

# How the Application Works

- User uploads an image via the /upload endpoint. To expeiment this I have used the "Postman" to see the outcome or result.
- The server validates the file type and size (only PNG, JPG, JPEG allowed).
- The image is saved locally in the uploads/ directory.
- The image description is generated using OpenAI’s GPT-3 model with three descriptions: formal, humorous, and critical.
- The server responds with the uploaded image URL and the generated descriptions.


# To Run the Application

- Use  [ python app.py ] inside the terminal 
