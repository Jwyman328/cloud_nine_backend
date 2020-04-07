from django.shortcuts import render
from .models import NewsItem
from .serializers import LastestNewsItemsSerializer
# Create your views here.
class LatestNewsItems(views.APIView):

    def get(self, request):
        user = request.user
        lastFiveNewsItems = NewsItem.objects.all()[:5]
        serialized_data = LastestNewsItemsSerializer(lastFiveNewsItems,  many=True).data
        return Response(serialized_data, status.HTTP_200_OK)