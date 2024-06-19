from rest_framework import serializers
from . import models as m


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Category
        fields = '__all__'
