from typing_extensions import Required
from django.db import models
from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name','description')