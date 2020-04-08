from django.contrib import admin

# Register your models here.
from .models import NewsItem, TourItem

admin.site.register(NewsItem)
admin.site.register(TourItem)
