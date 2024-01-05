#Import libraries
import os

import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.environ["PALM_API_KEY"])


# genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)



image = PIL.Image.open('WIN_20240104_18_20_40_Pro.jpg') 
vision_model = genai.GenerativeModel('gemini-pro-vision')






response = vision_model.generate_content(["What is this ID card ? and what name and address in this id ?",image])

response.resolve()

print(response.text)
