# playlists/views.py
from rest_framework import generics
from .models import Playlist, PlaylistTrack
from .serializers import PlaylistSerializer, PlaylistTrackSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import render



class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_object(self):
        # Use uuid.UUID to properly handle UUID conversion
        uuid = self.kwargs.get('pk')
        return get_object_or_404(Playlist, uuid=uuid)

class PlaylistTrackListCreateView(generics.ListCreateAPIView):
    queryset = PlaylistTrack.objects.all()
    serializer_class = PlaylistTrackSerializer


def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/playlist_list.html', {'playlists': playlists})

def playlist_detail(request, uuid):
    playlist = Playlist.objects.get(uuid=uuid)
    playlist_tracks = PlaylistTrack.objects.filter(playlist=playlist)
    return render(request, 'playlists/playlist_detail.html', {'playlist': playlist, 'playlist_tracks': playlist_tracks})