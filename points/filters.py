import django_filters
from .models import OriginationPoint


class OriginationPointFilter(django_filters.FilterSet):
    password = django_filters.CharFilter(name='password', lookup_type='icontains')
    login = django_filters.CharFilter(name='login', lookup_type='icontains')

    class Meta:
        model = OriginationPoint
        fields = ['login', 'password']