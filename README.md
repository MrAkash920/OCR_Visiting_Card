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




# Nanonets OCR API Client

This Python script sends an image file to the Nanonets OCR API endpoint for optical character recognition (OCR) processing.

## Installation

1. Make sure you have Python installed on your system.
2. Install the requests library using pip:
   ```
   pip install requests
   ```

## Usage

1. Replace the placeholder values in the script:
   - Replace `'https://app.nanonets.com/api/v2/OCR/Model/7742b5db-8793-42a5-b9a3-3da16b65fd41/LabelFile/?async=false'` with the actual URL of your Nanonets OCR API endpoint.
   - Replace `'data/data1.jpg'` with the path to the image file you want to process.
   - Replace `'b536c623-fd51-11ee-9882-9e1dbec10b66'` with your actual Nanonets API key.

2. Run the script:
   ```
   python request.py
   ```

## Dependencies

- [requests](https://pypi.org/project/requests/): Used to send HTTP requests to the Nanonets OCR API endpoint.

## Notes

- Make sure your Nanonets API key is valid and has the necessary permissions to access the OCR model.
- Ensure that the image file path provided (`data/data1.jpg` in this example) is correct and the file exists.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

