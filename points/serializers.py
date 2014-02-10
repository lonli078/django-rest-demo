from rest_framework import serializers
from .models import OriginationPoint
from .models import TerminationPoint
from .models import RelationPoints
from django.utils.timezone import now


class TerminationPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerminationPoint


class RelationPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationPoints


class RelationsPointsField(serializers.RelatedField):
    def to_native(self, value):
        return 'op:{0}   tp:{1}'.format(value.op.name, value.tp.name)


class OriginationPointSerializer(serializers.ModelSerializer):
    login_password = serializers.Field(source='login_password')
    now = serializers.SerializerMethodField('get_now')
    #relationpoints_set = RelationsPointsField(many=True)

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
                  'login_password', 'now', 'relationpoints_set',)
        read_only_fields = ('description',)


