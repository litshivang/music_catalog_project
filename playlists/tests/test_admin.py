# playlists/tests/test_admin.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from playlists.models import Playlist
from django.urls import reverse  


class PlaylistAdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('admin', 'admin@example.com', 'password')
        self.client.login(username='admin', password='password')
        self.playlist = Playlist.objects.create(name='Admin Playlist')

    def test_playlist_admin_view(self):
        playlist = Playlist.objects.create(name='Test Playlist')
        url = reverse('admin:playlists_playlist_change', args=[playlist.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)