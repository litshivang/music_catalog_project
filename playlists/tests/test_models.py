# playlists/tests/test_models.py
from django.test import TestCase
from playlists.models import  Track, Playlist
from artists.models import Artist
from tracks.models import Album

class PlaylistModelTestCase(TestCase):
    def test_playlist_creation(self):
        playlist = Playlist.objects.create(name='My Playlist')
        self.assertEqual(playlist.name, 'My Playlist')

