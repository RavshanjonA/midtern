from django.db.models import Count, Avg
from rest_framework.serializers import ModelSerializer

from apps.befitpro.models import User, Service, Product, Review


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name', 'avatar')

class ServiceSerializer(ModelSerializer):
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation["review"] = instance.reviews.all().aggregate(Avg("grade"), Count("grade"))
        # representation["pruducts"] = ProductSerializer(instance.products.all(), many=True)
        representation["pruducts"]   = Product.objects.filter(service=instance).values_list('name', flat=True)

        return representation
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


