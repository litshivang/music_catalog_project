# playlists/tests/test_api.py
from rest_framework.test import APITestCase
from django.urls import reverse
from playlists.models import Playlist

class PlaylistAPITestCase(APITestCase):
    def setUp(self):
        self.playlist = Playlist.objects.create(name='API Playlist')

    def test_playlist_api_detail(self):
        url = reverse('playlist-detail', args=[self.playlist.name]) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'API Playlist') 