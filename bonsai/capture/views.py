from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect
from capture.models import Photo
from django.urls import reverse
from django.http import HttpResponseRedirect
from text import views


class index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        photo = Photo(image=request.FILES['image'])
        photo.save()


        # Redirect the request to the URL
        return redirect('/text')































# import os
# from django.shortcuts import render
# from PIL import Image
# from time import time

# def index(request):
#     if request.method == 'POST':
#         # Get the camera selection and photo data from the form
#         camera = request.POST.get('camera')
#         photo = request.FILES.get('photo')

#         # Create a filename for the photo using the current time
#         filename = str(time()) + '.jpg'

#         # Save the photo to the server
#         with open(filename, 'wb') as f:
#             f.write(photo.read())

#         # Open the photo using the PIL library
#         img = Image.open(filename)

#         # Do any necessary processing on the photo here

#         # Save the processed photo
#         img.save(filename)

#         # Render a template with the processed photo
#         return render(request, 'photo.html', {'photo': filename})

#     return render(request, 'index.html')
