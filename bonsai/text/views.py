from django.shortcuts import render

import cohere

import os
import numpy as np
import cv2
import pytesseract
from PIL import Image

from capture.models import Photo



# Create your views here.
def extract(request):
    # Returns latest added picture in database
    lastphotoobject = Photo.objects.latest()

    with lastphotoobject.image.open() as f:
        data = f.read()

    # Convert the image data to a numpy array
    array = np.frombuffer(data, dtype=np.uint8)

    # Read the image and convert it to grayscale
    imag = cv2.imdecode(array, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)

    # Run Tesseract OCR on the image.
    text = pytesseract.image_to_string(gray)

    request.session['text'] = text
    context = {
        'text': text,
    }
    return render(request, 'extract.html', context)

def direct(request):
    return render(request, 'direct.html')

def options(request):
    # text = request.POST.get('text')
    # print(text)
    if request.method == 'POST':
        text = request.POST.get('text')
        print(text)
        request.session['text'] = text
    return render(request, 'options.html')

def output(request):
    # API key from the Cohere dashboard
    API_KEY = 'iXbaxWJMktSqYSwl0aM9sOD4667ynUu59I8iBi3m'
    co = cohere.Client(API_KEY)
    additionalprompt = request.POST.get('additionalprompt')
    
    prompt = request.session.get('text')


    if 'summary' in request.POST:
        prompt = "get the summary of this article." + additionalprompt +"\n"+prompt
    else:
        prompt = "complete the following text." + additionalprompt +"\n"+prompt


    response = co.generate( 
        model='medium', 
        prompt = prompt,
        max_tokens=400, 
        temperature=0.8,
        stop_sequences=["--"])

    out = response.generations[0].text
    context = {
        'prompt':prompt,
        'out':out,
    }
    return render(request, 'output.html', context)



