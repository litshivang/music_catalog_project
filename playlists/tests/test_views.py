# playlists/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from albums.models import Album
from playlists.models import Playlist
from artists.models import Artist
from tracks.models import Track

class PlaylistViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.playlist = Playlist.objects.create(name='Test Playlist')

    def test_playlist_detail_view(self):
        def test_playlist_detail_view(self):
            playlist = Playlist.objects.create(name='Test Playlist')
            url = reverse('playlist-detail', args=[playlist.name])  
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
