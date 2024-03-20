from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Hoodies
from .serializers import HoodiesSerializer

@api_view(['POST'])
def order_hoodies(request):
    if request.method == 'POST':
        serializer = HoodiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order placed successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class HoodiesViewSet(viewsets.ModelViewSet):
	serializer_class = HoodiesSerializer
	queryset = Hoodies.objects.all()