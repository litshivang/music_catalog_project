# playlists/serializers.py
from rest_framework import serializers
from .models import Playlist, PlaylistTrack

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['uuid', 'name']

class PlaylistTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistTrack
        fields = ['playlist', 'track', 'order']
