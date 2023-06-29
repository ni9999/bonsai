# Bonsai - Text Extraction and Summarization Webapp
Welcome to Bonsai, a webapp that takes in photos containing text and provides a summary or completes the text.

This webapp is made with Django and uses pytessaract for text extraction and cohere API for summarization and text completion.

Simply upload a photo containing text and Bonsai will do the rest. The summary or completed text will be displayed on the screen for you to review and copy.

# Project in devpost - [Click here](https://devpost.com/software/bonsai-t4md50)

To run locally 

pip install -r requirements.txt
sudo apt install libgl1-mesa-glx

And then add your url/host to ALLOWED_HOSTS in settings.py

