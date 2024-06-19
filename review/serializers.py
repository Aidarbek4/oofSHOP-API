from rest_framework import serializers
from . import models as m


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Review
        fields = '__all__'
