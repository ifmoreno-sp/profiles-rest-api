from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile) #This tells the django admin to register our profile model with the admin site, so it is accesible in the admin interface
