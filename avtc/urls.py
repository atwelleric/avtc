from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<slug>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('gallery/', views.ArtList.as_view(), name=('art_list')),
    path('gallery/<slug>', views.ArtDetail.as_view(), name='art_detail'),
]
