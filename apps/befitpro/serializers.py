from rest_framework.serializers import ModelSerializer

from apps.befitpro.models import User, Service, Product, Review


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'avatar')

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'logo')

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'discount', 'service', 'get_logo')


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'grade', 'grade_count')


