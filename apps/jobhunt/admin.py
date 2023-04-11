from django.contrib import admin

from apps.jobhunt.models import Company, Resume, Vacancy

admin.site.register([Company, Resume, Vacancy])
