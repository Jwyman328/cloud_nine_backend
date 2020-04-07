from django.shortcuts import render
from .models import NewsItem
from .serializers import LastestNewsItemsSerializer
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class LatestNewsItems(views.APIView):

    def get(self, request):
        lastFiveNewsItems = NewsItem.objects.all()[:5]
        serialized_data = LastestNewsItemsSerializer(lastFiveNewsItems,  many=True).data
        return Response(serialized_data, status.HTTP_200_OK)