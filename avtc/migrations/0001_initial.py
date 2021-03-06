# Generated by Django 3.1.7 on 2021-02-25 23:24

import avtc.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=avtc.models.profile_image_directory_path)),
                ('bio', models.CharField(max_length=500)),
                ('instagram', models.URLField(default='https://www.instagram.com/avtckenosha/', max_length=500)),
                ('slug', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='untitled', max_length=100)),
                ('art_image', models.ImageField(blank=True, null=True, upload_to=avtc.models.art_image_directory_path)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_pieces', to='avtc.artist')),
            ],
        ),
    ]
