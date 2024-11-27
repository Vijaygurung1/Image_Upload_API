from flask import Flask, request, jsonify
import openai
import os

# Set your OpenAI API key
openai.api_key = "sk-6Z39CikSiBEfibOVuV3VDMyg6gNwHPtbFVd3I3TyDgT3BlbkFJ1l9xwkabT6Ef00eAH9sC6uxETYIA2DzI-EPFxbT7IA"

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Check if the uploaded file is an allowed image type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    """Welcome route."""
    return "Welcome to the Image Upload and Description API!"


@app.route('/upload', methods=['POST'])
def upload_image():
    """Endpoint to upload an image and generate descriptions."""
    # Check if file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file selected for upload"}), 400

    file = request.files['file']

    # Check if a file is selected and has a valid extension
    if file.filename == '':
        return jsonify({"error": "No file selected for upload"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed. Only PNG, JPG, JPEG files are supported."}), 400

    # Save the file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Example prompt for GPT/LLM
    prompt = f"""
    You are analyzing an image uploaded by a user. The image file name is '{file.filename}'.
    Provide three descriptions of this image:
    - A formal description
    - A humorous description
    - A critical description
    """

    try:
        # Use OpenAI's ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant that describes images in different tones."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )

        # Extract descriptions from the response
        descriptions = response['choices'][0]['message']['content'].strip().split("\n")

        # Format the response
        formatted_response = {
            "image_url": f"/uploads/{file.filename}",
            "descriptions": {
                "formal": descriptions[0] if len(descriptions) > 0 else "No formal description generated.",
                "humorous": descriptions[1] if len(descriptions) > 1 else "No humorous description generated.",
                "critical": descriptions[2] if len(descriptions) > 2 else "No critical description generated."
            }
        }

        return jsonify(formatted_response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

