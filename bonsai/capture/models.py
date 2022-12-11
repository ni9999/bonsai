# Create your models here.

from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='./photos')
    date_captured = models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by = 'date_captured'
