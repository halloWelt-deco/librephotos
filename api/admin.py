from django.contrib import admin

from .models import AlbumAuto, AlbumUser, Face, Person, Photo, TripUser

# Register your models here.

admin.site.register(Photo)
admin.site.register(Person)
admin.site.register(Face)
admin.site.register(AlbumAuto)
admin.site.register(AlbumUser)
admin.site.register(TripUser)
