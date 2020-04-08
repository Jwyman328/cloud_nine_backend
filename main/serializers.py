from rest_framework import serializers
from .models import NewsItem, TourItem

class LastestNewsItemsSerializer(serializers.ModelSerializer):

     class Meta:
        model = NewsItem
        fields =  "__all__"


class TourItemSerializer(serializers.ModelSerializer):

     class Meta:
        model = TourItem
        fields =  "__all__"

