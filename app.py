import google.generativeai as genai
import PIL.Image
import json
import pandas as pd
from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

# Set your API key "" 
genai.configure(api_key="") 

def extract_text_from_image(image_path):
    """Extracts text from an image using Gemini 1.5 Flash Model"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    image = PIL.Image.open(image_path)
    response = model.generate_content([image, "Extract the text from this image in a simple 'key: value' format without any special characters like * and without introductory phrases."])
    return response.text if response else "No text extracted."

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    extracted_text = extract_text_from_image(file.filename)
    
    # Format extracted text into key-value pairs
    output_data = {}
    lines = extracted_text.split("\n")
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.replace("*", "").strip()
            value = value.replace("*", "").strip()
            output_data[key] = value
    
    # Save extracted text to a JSON file
    with open("extracted_text.json", "w") as json_file:
        json.dump(output_data, json_file, indent=4)
    
    # Save extracted text to an Excel file
    df = pd.DataFrame(list(output_data.items()))
    df.to_excel("extracted_text.xlsx", index=False, header=False)
    
    return {"message": "Text extracted successfully", "data": output_data}
