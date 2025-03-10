from django.urls import path, include
from django.conf.urls.static import static
from .views import SongList, SongDetail, CostumeSignUp
from music_player import settings

urlpatterns = [
    path(route='', view=SongList.as_view(), name='song-list'),
    path(route='<int:pk>/', view=SongDetail.as_view(), name='song-detail'),
    path(route='', view=include('allauth.urls')),
    path(route='signup/', view=CostumeSignUp.as_view(), name='account_signup'),
]

