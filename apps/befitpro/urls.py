from django.urls import path

from apps.befitpro.views import ServiceAPIView

urlpatterns = [
    path('service/<id>', ServiceAPIView.as_view(), name='home'),
]
