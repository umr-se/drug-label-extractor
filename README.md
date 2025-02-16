# Drug Label Extractor

A FastAPI-based backend service that extracts drug/medicine label text from images using the Gemini Flash 1.5 model. The extracted text is then provided in JSON and Excel file formats.

## Features
- Accepts drug/medicine images as input
- Uses the Gemini Flash 1.5 model for text extraction
- Requires an API key for authentication
- Outputs extracted label text in JSON and Excel formats

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- Gemini Flash 1.5 API access
- OpenAI's API key
- Pandas (for Excel file generation)

## Installation
```bash
# Clone the repository
git clone https://github.com/umr-se/drug-label-extractor.git
cd drug-label-extractor

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

## Configuration
Set up your environment variables:
```bash
export GEMINI_API_KEY="your_api_key_here"
```
On Windows (PowerShell):
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

```powershell
pip install fastapi uvicorn google-generativeai pillow pandas openpyxl
```

## Usage
### Running the FastAPI Server
```bash
uvicorn app:app --reload
```

### API Endpoints
#### Extract Label Text
```http
POST /extract-label
```
**Request:**
- `multipart/form-data` with an image file

**Response:**
```json
{
  "text": "Extracted drug label text...",
  "json_file": "output.json",
  "excel_file": "output.xlsx"
}
```

## Output
- Extracted text is returned as JSON
- An Excel file (`output.xlsx`) is also generated

## Contributing
Feel free to open issues or submit pull requests!

## Author
[umer](https://github.com/umr-se)

![drug](https://github.com/user-attachments/assets/37ed5583-0f51-4676-a976-c0aa7d960b62)
![json](https://github.com/user-attachments/assets/9ce840a5-ff1c-49dd-9086-e2170a429bd0)
![excel](https://github.com/user-attachments/assets/98bd8b7f-56ec-465f-9ef4-7bcef624d8ca)

