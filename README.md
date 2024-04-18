# Visiting Card OCR API

This is a Flask application that provides an API endpoint for extracting information from visiting card images using Optical Character Recognition (OCR). The extracted information includes Name, Company Name, Designation, Email, Contact Numbers, Address, and Website.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/MrAkash920/OCR_Visiting_Card
   ```
2. Navigate to the project directory:
   ```
   cd OCR_Visiting_Card
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```
2. Access the API endpoint using a tool like cURL or Postman, or integrate it into your application. The API endpoint is `http://localhost:5000/upload`.

## API Endpoint

### `POST /upload`

- **Description**: Uploads a visiting card image and extracts information using OCR.
- **Request Body**: Form-data with a file field named `file` containing the visiting card image.
- **Response**: JSON object containing the extracted information.

Example:
```
curl -X POST -F "file=@/path/to/visiting_card.jpg" http://localhost:5000/upload
```

## Regular Expression Functions

- `extract_name(text)`: Extracts the name from OCR text using a regular expression pattern.
- `extract_company_name(text)`: Extracts the company name from OCR text using a regular expression pattern.
- `extract_designation(text)`: Extracts the designation from OCR text using a regular expression pattern.
- `extract_email(text)`: Extracts the email address from OCR text using a regular expression pattern.
- `extract_contact_numbers(text)`: Extracts the contact numbers from OCR text using a regular expression pattern.
- `extract_address(text)`: Extracts the address from OCR text using a regular expression pattern.
- `extract_website(text)`: Extracts the website URL from OCR text using a regular expression pattern.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

