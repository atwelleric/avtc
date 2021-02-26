from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import ArtistSerializer, ArtSerializer, ArtistDetailSerializer
from .models import Artist, Art


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(RetrieveAPIView):
    queryset = Artist.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = ArtistDetailSerializer
    lookup_field = 'slug'


class ArtList(generics.ListCreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer


class ArtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    lookup_field = 'slug'


# Create your views here.
