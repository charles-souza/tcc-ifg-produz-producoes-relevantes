from rest_framework import serializers
from rest_framework.fields import FileField, ListField

from productions import models

class ProductionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Productions
        fields = '__all__'