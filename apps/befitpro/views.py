from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from apps.befitpro.models import Service
from apps.befitpro.serializers import ServiceSerializer


class ServiceAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset =  super().get_queryset()
        id = self.kwargs.get('id')
        if id:
            queryset = queryset.filter(id=id)

        return queryset

