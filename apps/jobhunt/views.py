from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.jobhunt.models import Company, Resume, Vacancy


class HomeAPIView(APIView):
    def get(self, request):
        data = {}
        data['companies']  = Company.objects.count()
        data['resumes']  = Resume.objects.count()
        data['vacancies']  = Vacancy.objects.count()
        return Response(data=data)
