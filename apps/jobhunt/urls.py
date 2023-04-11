from django.urls import path

from apps.jobhunt.views import HomeAPIView

urlpatterns = [
    path('v1/home/', HomeAPIView.as_view(), name='home'),
]
