from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, ImageField, IntegerField, ForeignKey, CASCADE, TextField

from apps.befitpro.utils import service_logo_upload_path, avatar_upload_path


class User(Model):
    first_name = CharField(max_length=28)
    last_name = CharField(max_length=28)
    avatar = ImageField(upload_to=avatar_upload_path)

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name


class Service(Model):
    name = CharField(max_length=56)
    logo = ImageField(upload_to=service_logo_upload_path)

    class Meta:
        db_table = 'service'

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=56)
    price = IntegerField()
    discount = IntegerField(null=True, blank=True)
    service = ForeignKey('befitpro.Service', CASCADE, 'products')

    @property
    def get_logo(self):
        return self.service.logo

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class Review(Model):
    service = ForeignKey('befitpro.Service', CASCADE, 'reviews')
    user = ForeignKey('befitpro.User', CASCADE, 'reviews')
    text = TextField()
    grade = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        db_table = 'review'
        unique_together = ['service', 'user']

    def grade_count(self):
        return self.__class__.objects.filter(grade=self.grade).count()

    def __str__(self):
        return self.user.first_name
