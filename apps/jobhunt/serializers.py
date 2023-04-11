from rest_framework.serializers import ModelSerializer, Serializer

from apps.jobhunt.models import Resume, Company, Vacancy


class ResumeSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class VacanySerializer(ModelSerializer):
    class Meta:
        model =  Vacancy
        fields = "__all__"



