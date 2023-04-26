from django.db.models import Count, Avg
from rest_framework.serializers import ModelSerializer

from apps.befitpro.models import User, Service, Product, Review


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'avatar')


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'discount', 'service', 'get_logo')
    def get_get_logo(self, product):
        return product.get_logo.url

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'grade', 'grade_count')



class ServiceSerializer(ModelSerializer):
    products = ProductSerializer(many=True )
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Service
        fields = ('name', 'logo', 'products', 'reviews')




