from rest_framework import serializers
from .models import OriginationPoint


class OriginationPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = OriginationPoint