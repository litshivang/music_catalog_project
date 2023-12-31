# Generated by Django 4.2.4 on 2023-12-10 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='playlists.playlist')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracks.track')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
