from rest_framework import viewsets
from rest_framework.response import Response

from productions.api import serializers
from productions import models

class ProductionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductionsSerializer
    queryset = models.Productions.objects.all()
