from django.contrib import admin

from apps.befitpro.models import User, Service, Product, Review

admin.site.register([User, Service, Product, Review])
