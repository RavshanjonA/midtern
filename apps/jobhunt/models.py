from django.db.models import Model, ForeignKey, CASCADE
from rest_framework.fields import CharField


class Company(Model):
    name = CharField(max_length=96)
    #company fields

    class Meta:
        db_table='company'
        verbose_name_plural = 'companies'
class Resume(Model):
    full_name = CharField(max_length=96)
    #user fields
    class Meta:
        db_table = 'resume'
class Vacancy(Model):
    company = ForeignKey('jobhunt.Company', CASCADE, 'vacancies')
    postion = CharField(max_length=56)
    #vacanvy fields
    class Meta:
        db_table = 'vacacy'
        verbose_name_plural = 'Vacancies'
