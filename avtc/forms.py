from django import forms
from .models import Artist, Art


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name', 'profile_image', 'bio',
                  'instagram', 'slug', 'art_pieces')


class ArtForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = ('title', 'art_image', 'artist', 'slug')
