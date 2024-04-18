import requests

# URL of the Nanonets OCR API endpoint
url = 'https://app.nanonets.com/api/v2/OCR/Model/7742b5db-8793-42a5-b9a3-3da16b65fd41/LabelFile/?async=false'

data = {'file': open('data/data1.jpg', 'rb')}

# Sending a POST request to the Nanonets OCR API endpoint
response = requests.post(
    url,
    auth=requests.auth.HTTPBasicAuth('b536c623-fd51-11ee-9882-9e1dbec10b66', ''),
    files=data
)

print(response.text)
