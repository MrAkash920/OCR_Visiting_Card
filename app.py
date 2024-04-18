from flask import Flask, request, jsonify, render_template
import pytesseract
import pytesseract
from PIL import Image
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')



# Create API endpoint
@app.route('/upload', methods=['POST'])
def process_card():
    # Check if request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    # Check image file format
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if file and allowed_file(file.filename):
        image_path = 'uploaded_image.jpg'
        file.save(image_path)

        # Use Tesseract OCR to extract text from the image
        extracted_text = pytesseract.image_to_string(Image.open(image_path))

        # Parse extracted text to get necessary info
        name = extract_name(extracted_text)
        company_name = extract_company_name(extracted_text)
        designation = extract_designation(extracted_text)
        email = extract_email(extracted_text)
        contact_numbers = extract_contact_numbers(extracted_text)
        address = extract_address(extracted_text)
        website = extract_website(extracted_text)

        response_data = {
            'name': name,
            'company_name': company_name,
            'designation': designation,
            'email': email,
            'contact_numbers': contact_numbers,
            'address': address,
            'website': website
        }

        return jsonify(response_data), 200
    else:
        return jsonify({'error': 'Unsupported file format'}), 400

# Check file format
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

#Functions to extract information using regular expression

def extract_name(text):
    name_pattern = re.compile(r'Name: (.+)', re.IGNORECASE)
    match = name_pattern.search(text)
    if match:
        return match.group(1).strip()
    else:
        return None

def extract_company_name(text):
    company_pattern = re.compile(r'Company: (.+)', re.IGNORECASE)
    match = company_pattern.search(text)
    if match:
        return match.group(1).strip()
    else:
        return None

def extract_designation(text):
    designation_pattern = re.compile(r'Designation: (.+)', re.IGNORECASE)
    match = designation_pattern.search(text)
    if match:
        return match.group(1).strip()
    else:
        return None

def extract_email(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = email_pattern.findall(text)
    if emails:
        return emails[0]
    else:
        return None

def extract_contact_numbers(text):
    phone_pattern = re.compile(r'(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?(\d{3}[\s.-]?\d{4})')
    contact_numbers = phone_pattern.findall(text)
    numbers = [number[0] + number[1] + number[2] for number in contact_numbers]
    return ', '.join(numbers)

def extract_address(text):
    address_pattern = re.compile(r'Address: (.+)', re.IGNORECASE)
    match = address_pattern.search(text)
    if match:
        return match.group(1).strip()
    else:
        return None

import re

def extract_website(text):
    website_pattern = re.compile(r'\b(www\.)?([a-zA-Z0-9-]+\.){1,2}[a-zA-Z]{2,}(/\S*)?\b')
    match = website_pattern.search(text)
    
    if match:
        return match.group()
    else:
        return None


if __name__ == '__main__':
     app.run(debug=True)

