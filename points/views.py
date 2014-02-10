# -*- coding: utf-8 -*-
from .models import OriginationPoint
from .serializers import OriginationPointSerializer
from rest_framework import generics
from rest_framework.settings import api_settings
from rest_framework import filters
from .filters import OriginationPointFilter


class OpListGenericView(generics.ListCreateAPIView):
    model = OriginationPoint
    serializer_class = OriginationPointSerializer
    filter_class = OriginationPointFilter

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    parser_classes = api_settings.DEFAULT_PARSER_CLASSES
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    content_negotiation_class = api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS
    paginate_by = api_settings.PAGINATE_BY
    paginate_by_param = api_settings.PAGINATE_BY_PARAM
    max_paginate_by = api_settings.MAX_PAGINATE_BY
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, )

    ordering = ('id', 'login',)
    search_fields = ('password',)
    filter_fields = ('name',)

    def get_queryset(self):
        return OriginationPoint.objects.all()

    def pre_save(self, obj):
        """
        Placeholder method for calling before saving an object.

        May be used to set attributes on the object that are implicit
        in either the request, or the url.
        """
        pass

    def post_save(self, obj, created=False):
        """
        Placeholder method for calling after saving an object.
        """
        pass


class OpDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OriginationPoint
    serializer_class = OriginationPointSerializer

    def get_queryset(self):
        return OriginationPoint.objects.all()

    def get_object(self, queryset=None):
        return super(OpDetailGenericView, self).get_object(queryset=None)

    def pre_save(self, obj):
        """
        Placeholder method for calling before saving an object.

        May be used to set attributes on the object that are implicit
        in either the request, or the url.
        """
        pass

    def post_save(self, obj, created=False):
        """
        Placeholder method for calling after saving an object.
        """
        pass

    def pre_delete(self, obj):
        """
        Placeholder method for calling before deleting an object.
        """
        pass

    def post_delete(self, obj):
        """
        Placeholder method for calling after deleting an object.
        """
        pass