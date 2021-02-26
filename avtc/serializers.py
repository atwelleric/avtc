from rest_framework import serializers
from .models import Artist, Art


class ArtistSerializer(serializers.ModelSerializer):
    # art_pieces = serializers.SlugRelatedField(
    #     queryset=Art.objects.all(),
    #     source='art',
    #     slug_field='slug',
    # )
    # art_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Art.objects.all(),
    #     source='art',
    # )
    # artist_url = serializers.ModelSerializer.serializer_url_field(
    #     view_name='artist_detail',
    # )

    class Meta:
        model = Artist
        fields = ('name', 'profile_image', 'bio',
                  'instagram', 'art_pieces', 'slug', 'job_title', 'specialty_one', 'specialty_two', 'specialty_three')


class ArtistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'profile_image', 'bio',
                  'instagram', 'art_pieces', 'slug', 'job_title', 'specialty_one', 'specialty_two', 'specialty_three')
        slug_field = 'slug'


class ArtSerializer(serializers.ModelSerializer):
    # artist = serializers.HyperlinkedRelatedField(
    #     view_name='artist_detail',
    #     read_only=True
    # )
    artist_id = serializers.SlugRelatedField(
        queryset=Artist.objects.all(),
        source='artist',
        slug_field='slug',
    )

    class Meta:
        model = Art
        fields = ('artist_id',
                  'art_image', 'title', 'slug')
