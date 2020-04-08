from django.shortcuts import render
from .models import NewsItem, TourItem
from .serializers import LastestNewsItemsSerializer, TourItemSerializer
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
import datetime

# Create your views here.
class LatestNewsItems(views.APIView):

    def get(self, request):
        lastFiveNewsItems = NewsItem.objects.all()[:5]
        serialized_data = LastestNewsItemsSerializer(lastFiveNewsItems,  many=True).data
        return Response(serialized_data, status.HTTP_200_OK)


class TourItems(views.APIView):

    def get(self, request):
        today = datetime.datetime.now()
        AllCurrentAndFutureTourItems = TourItem.objects.filter(date__gte = date )
        serialized_data = TourItemSerializer(AllCurrentAndFutureTourItems,  many=True).data
        return Response(serialized_data, status.HTTP_200_OK)