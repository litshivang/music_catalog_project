# playlists/admin.py
from django.contrib import admin
from .models import Playlist, PlaylistTrack

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid']  # Add 'uuid' to the list_display

admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(PlaylistTrack)
