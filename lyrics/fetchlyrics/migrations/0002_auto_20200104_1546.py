# Generated by Django 3.0.2 on 2020-01-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetchlyrics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='artist',
            field=models.CharField(default='No artist', max_length=40),
        ),
        migrations.AddField(
            model_name='playlist',
            name='title',
            field=models.CharField(default='No song title', max_length=40),
        ),
    ]