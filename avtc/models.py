from django.db import models
from django.urls import reverse

# Defines path for artist profile images, {0}, {1} refers to items in the .format()


def profile_image_directory_path(instance, filename):
    return 'profile/{0}/'.format(filename)

# path for art images


def art_image_directory_path(instance, filename):
    return 'art/{0}/'.format(filename)

# User model for Artist


class Artist(models.Model):
    name = models.CharField(max_length=50)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to=profile_image_directory_path)
    bio = models.CharField(max_length=500)
    instagram = models.URLField(
        max_length=500, default="https://www.instagram.com/avtckenosha/")
    slug = models.CharField(max_length=100, blank=False,
                            unique=True, primary_key=True)

    def __str__(self):
        return self.name


# Model for Art


class Art(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE,
        related_name='art_pieces'
    )

    title = models.CharField(max_length=100, default='untitled')
    art_image = models.ImageField(
        null=True, blank=True, upload_to=art_image_directory_path)

    slug = models.CharField(max_length=100, blank=False,
                            unique=True, primary_key=True)

    def __str__(self):
        return self.title
