from django.db.models import Model, ForeignKey, CASCADE
from rest_framework.fields import CharField


class Company(Model):
    name = CharField(max_length=96)
    #company fields
class Resume(Model):
    full_name = CharField(max_length=96)
    #user fields
class Vacancy(Model):
    company = ForeignKey('jobhunt.Company', CASCADE, 'vacancies')
    postion = CharField(max_length=56)
    #vacanvy fields

