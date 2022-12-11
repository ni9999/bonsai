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

    sum = f"""summarize shortly these passage. If you want to finish use '--'. {additionalprompt}:
    
Passage: Is Wordle getting tougher to solve? Players seem to be convinced that the game has gotten harder in recent weeks ever since The New York Times bought it from developer Josh Wardle in late January. The Times has come forward and shared that this likely isn't the case. That said, the NYT did mess with the back end code a bit, removing some offensive and sexual language, as well as some obscure words There is a viral thread claiming that a confirmation bias was at play. One Twitter user went so far as to claim the game has gone to "the dusty section of the dictionary" to find its latest words.

TLDR: Wordle has not gotten more difficult to solve.
--
Passage: ArtificialIvan, a seven-year-old, London-based payment and expense management software company, has raised $190 million in Series C funding led by ARG Global, with participation from D9 Capital Group and Boulder Capital. Earlier backers also joined the round, including Hilton Group, Roxanne Capital, Paved Roads Ventures, Brook Partners, and Plato Capital.

TLDR: ArtificialIvan has raised $190 million in Series C funding.
--
Passage: {prompt}

TLDR:"""

    if 'summary' in request.POST:
        prompt = sum
        response = co.generate( 
            model='xlarge', 
            prompt = prompt,
            max_tokens=80, 
            temperature=0.8,
            stop_sequences=["--"])
    
    else:
        prompt = "complete the following story." + additionalprompt +". \nstory:"+prompt
        response = co.generate(  
            model='xlarge',  
            prompt = prompt,  
            max_tokens=200,  
            temperature=0.6,  
            stop_sequences=["--"])


    out = response.generations[0].text
    context = {
        'prompt':prompt,
        'out':out,
    }
    return render(request, 'output.html', context)



