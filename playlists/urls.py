# playlists/urls.py
from django.urls import path
from  playlists import views
from .views import PlaylistAPIView, PlaylistDetailView, create_playlist, delete_playlist, playlist_template, single_playlist_detail, update_playlist

# I have Kept Rest and Template Individual 
# Template API you can directly access on "http://127.0.0.1:8000/"

urlpatterns = [

    #Rest-API
    path('playlists/', PlaylistAPIView.as_view(), name='All-Playlist'), #http://127.0.0.1:8000/api/playlists/
    path('playlists/create/', PlaylistAPIView.as_view(), name='playlist-list-create'), #http://127.0.0.1:8000/api/playlists/create/
    path('playlists-update/<str:name>/', PlaylistAPIView.as_view(), name='playlist-update' ), #http://127.0.0.1:8000/api/playlists-update/Hollywood/
    path('playlists-delete/<str:name>/', PlaylistAPIView.as_view(), name='playlist-delete' ), #http://127.0.0.1:8000/api/playlists-delete/Hollywood/
    path('playlists/<str:name>/', PlaylistDetailView.as_view(), name='playlist-detail'),  #http://127.0.0.1:8000/api/playlists/Hollywood/

    #Template-API
    path('', views.landing_page, name='landing-page'), # http://127.0.0.1:8000/

    path('playlists-tmp/', views.playlist_template, name='playlist-list'), 
    path('playlists-tmp-detail/', views.single_playlist_detail, name='playlist-tmp-detail'),   
    path('playlists-create/', views.create_playlist, name='create-playlist'), 
    path('update-playlist/<str:name>/', update_playlist.as_view(), name='update-playlist'),  
    path('playlist-tmp-update/', update_playlist.as_view(), name='update-playlist-tmp'),
    path('delete-playlist/<str:name>/', delete_playlist.as_view(), name='delete-playlist'),
    path('playlist-tmp-delete/', delete_playlist.as_view(), name='delete-playlist-tmp'),

]

