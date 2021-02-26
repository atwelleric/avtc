from django.contrib import admin
from .models import Artist, Art


# class ArtistAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(Artist)
admin.site.register(Art)
