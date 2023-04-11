from django.db.models import Count, Avg
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from apps.befitpro.models import Service, Review
from apps.befitpro.serializers import ServiceSerializer, ReviewSerializer


class ServiceAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset =  super().get_queryset()
        id = self.kwargs.get('id')
        if id:
            queryset = queryset.filter(id=id)

        # queryset.prefetch_related('reviews').annotate(grade_count=Count('reviews'),
        #                                                grade_avg=Avg('reviews'))
        return queryset

class ReviewAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.kwargs.get('id')
        if id:
            queryset = queryset.filter(id=id)

        return queryset
