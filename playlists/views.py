# playlists/views.py
from django.http import Http404
from django.views import View
from rest_framework import generics
from .models import Playlist, PlaylistTrack
from .serializers import PlaylistSerializer, PlaylistTrackSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from tracks.models import Track
from django.http import HttpResponseRedirect
from django.urls import reverse
import uuid
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect

# Rest API:
class PlaylistAPIView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        name = self.kwargs.get(self.lookup_field)
        obj = get_object_or_404(queryset, name=name)
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Playlist deleted successfully."}, status=204)

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def get_object(self):
        name = self.kwargs.get('name')  
        return get_object_or_404(Playlist, name=name)
    
# Views for Templates:

def landing_page(request):
    playlists = Playlist.objects.all()
    context = {'playlists': playlists}
    if request.method == 'GET':
        update_playlist_name = request.GET.get('updatePlaylistName')
        if update_playlist_name:
            return HttpResponseRedirect(reverse('update-playlist') + f'?name={update_playlist_name}')
    return render(request, 'landing_page.html', context)

    
def playlist_template(request):
    playlists = Playlist.objects.all()
    return render(request, 'all_playlist.html', {'playlists': playlists})

def single_playlist_detail(request):
    # Retrieve playlist name from the GET parameters
    playlist_name = request.GET.get('playlistName')

    # Use get_object_or_404 to retrieve the playlist based on the name
    playlist = get_object_or_404(Playlist, name=playlist_name)

    # Retrieve playlist tracks and order them
    playlist_tracks = PlaylistTrack.objects.filter(playlist=playlist).order_by('order')

    # Render the template with the playlist and playlist_tracks
    return render(request, 'playlist_details.html', {'playlist': playlist, 'playlist_tracks': playlist_tracks})

def create_playlist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        playlist_uuid = str(uuid.uuid4())
        playlist = Playlist.objects.create(uuid=playlist_uuid, name=name)
        # Redirect to the landing page after playlist creation
        return redirect('landing-page')
    
    return render(request, 'create_playlist.html')

class update_playlist(View):
    template_name = 'update_playlist.html'

    def get(self, request, *args, **kwargs):
        playlist_name = request.GET.get('updatePlaylistName')
        playlist = get_object_or_404(Playlist, name=playlist_name)
        context = {'playlist': playlist}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        playlist_name = request.POST.get('name')
        new_name = request.POST.get('new_name')
        playlist = get_object_or_404(Playlist, name=playlist_name)
        playlist.name = new_name
        playlist.save()
        messages.success(request, 'Playlist updated successfully!')
        return HttpResponseRedirect(reverse('landing-page'))

class delete_playlist(View):
    template_name = 'delete_playlist.html'

    def get(self, request, *args, **kwargs):
        playlist_name = request.GET.get('deletePlaylistName')
        playlist = get_object_or_404(Playlist, name=playlist_name)
        context = {'playlist': playlist}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        playlist_name = kwargs.get('name') 
        playlist = get_object_or_404(Playlist, name=playlist_name)
        playlist.delete()
        messages.success(request, 'Playlist deleted successfully!')
        return HttpResponseRedirect(reverse('landing-page'))