from rest_framework import serializers
from .models import OriginationPoint
from django.utils.timezone import now


class OriginationPointSerializer(serializers.ModelSerializer):
    login_password = serializers.Field(source='login_password')
    now = serializers.SerializerMethodField('get_now')

    def get_now(self, obj):
        return now()

    def validate_login(self, attrs, source):
        if len(attrs[source]) < 4:
            raise serializers.ValidationError("min length is 4")
        return attrs

    def validate(self, attrs):
        """
        Validate after all names validations
        """
        if attrs['login'] == attrs['password']:
            raise serializers.ValidationError("login and password can not be the same.")
        return attrs

    class Meta:
        model = OriginationPoint
        fields = ('id', 'name', 'login', 'password', 'description',
                  'login_password', 'now',)
        read_only_fields = ('description',)