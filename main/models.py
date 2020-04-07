from django.db import models

# Create your models here.

class NewsItem(models.Model):
    text_content = models.CharField(max_length=300, blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)
    date_published = models.DateTimeField(auto_now=True)
