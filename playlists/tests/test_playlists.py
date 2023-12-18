from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from albums.models import Album
from artists.models import Artist
from playlists.models import Playlist, Track
from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class PlaylistTests(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name='Artist')
        self.album = Album.objects.create(title='Album', artist=self.artist, release_date='2024-1-1')
        self.track = Track.objects.create(title='Track', duration=timedelta(minutes=3), album=self.album)

    def test_delete_playlist(self):
        playlist = Playlist.objects.create(name='Test Playlist')
        playlist.tracks.add(self.track)

        url = reverse('playlist-detail', args=[playlist.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Playlist.DoesNotExist):
            Playlist.objects.get(name='Test Playlist')

    def test_get_playlist_detail(self):
        playlist = Playlist.objects.create(name='Test Playlist')
        playlist.tracks.add(self.track)

        url = reverse('playlist-detail', args=[playlist.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Playlist')

    def test_get_playlist_detail(self):
        playlist = Playlist.objects.create(name='Test Playlist')
        playlist.tracks.add(self.track)

        url = reverse('playlist-detail', args=[playlist.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Playlist')

