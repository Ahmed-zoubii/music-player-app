# Generated by Django 5.1.4 on 2025-03-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_alter_song_favorite_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='path_to_file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
