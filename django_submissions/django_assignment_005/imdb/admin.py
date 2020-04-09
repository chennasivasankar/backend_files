from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Rating)
admin.site.register(Actor)
admin.site.register(Director)