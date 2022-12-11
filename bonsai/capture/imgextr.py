# Import the necessary libraries
import cv2
import pytesseract
import gensim
import cohere
from cohere.classify import Example








# Read the image and convert it to grayscale
image = cv2.imread('../photos/Capture.PNG')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Run Tesseract OCR on the image
text = pytesseract.image_to_string(gray)









API_KEY = 'iXbaxWJMktSqYSwl0aM9sOD4667ynUu59I8iBi3m'  # API key from the Cohere dashboard
co = cohere.Client(API_KEY)

prompt = text

response = co.generate( 
    model='medium', 
    prompt = prompt,
    # "This program generates a startup idea and name given the industry.  Industry: Workplace   Startup Idea: A platform that generates slide deck contents automatically based on a given outline   Startup Name: Deckerize   --   Industry: Home Decor   Startup Idea: An app that calculates the best position of your indoor plants for your apartment   Startup Name: Planteasy --   Industry: Healthcare   Startup Idea: A hearing aid for the elderly that automatically adjusts its levels and with a battery lasting a whole week   Startup Name: Hearspan  --   Industry: Education   Startup Idea: An online school that lets students mix and match their own curriculum based on their interests and goals   Startup Name: Prime Age  --   Industry: Productivity   Startup Idea:",
    max_tokens=40, 
    temperature=0.8,
    stop_sequences=["--"])

summary = response.generations[0].text

# Print the extracted text
print(text)
print("***************************************************")
# print(summary)
