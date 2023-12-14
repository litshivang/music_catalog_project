# playlists/urls.py
from django.urls import path
from .views import PlaylistListCreateView, PlaylistDetailView, PlaylistTrackListCreateView, playlist_detail, playlist_list

urlpatterns = [
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list-create'),
    path('playlists/<uuid:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),  # Use <uuid:pk>
    path('playlist-tracks/', PlaylistTrackListCreateView.as_view(), name='playlisttrack-list-create'),
    path('playlists-tmp/', playlist_list, name='playlist-tmp-list'),
    path('playlists-tmp/<uuid:uuid>/', playlist_detail, name='playlist-tmp-detail'),
]

# http://127.0.0.1:8000/api/playlists/  to list and create playlists.
# http://127.0.0.1:8000/api/playlists/<uuid>/ to view, update, or delete a specific playlist.
# http://127.0.0.1:8000/api/playlist-tracks/ to list and create playlist tracks.