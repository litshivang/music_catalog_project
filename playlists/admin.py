# playlists/admin.py
from django.contrib import admin
from .models import Playlist, PlaylistTrack

class PlaylistTrackInline(admin.TabularInline):
    model = PlaylistTrack
    extra = 9

class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistTrackInline]
    list_display = ('name', 'track_count','uuid')
    search_fields = ('name', 'uuid')

    def track_count(self, obj):
        return obj.tracks.count()  # Use the correct attribute name

    track_count.short_description = 'Number of Tracks'

admin.site.register(Playlist, PlaylistAdmin)
# admin.site.register(PlaylistTrack) #// This will display the Playlist Tracks