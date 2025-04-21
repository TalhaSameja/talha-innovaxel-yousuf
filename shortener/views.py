from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create_short_url(request):
    serializer = ShortURLSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_original_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    url.access_count += 1
    url.save()
    return Response(ShortURLSerializer(url).data)

@api_view(['PUT'])
def update_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    serializer = ShortURLSerializer(url, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    url.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_stats(request, code):
    url = get_object_or_404(ShortURL, short_code=code)
    return Response({
        "short_code": url.short_code,
        "original_url": url.original_url,
        "access_count": url.access_count,
        "created_at": url.created_at,
        "updated_at": url.updated_at
    })
@api_view(['GET'])
def index(request):
    return render(request, 'index.html')
