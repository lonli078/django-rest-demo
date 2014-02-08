# -*- coding: utf-8 -*-
from .models import OriginationPoint
from .serializers import OriginationPointSerializer
from rest_framework import generics


class OpListGenericView(generics.ListCreateAPIView):
    queryset = OriginationPoint.objects.all()
    serializer_class = OriginationPointSerializer


class OpDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OriginationPoint.objects.all()
    serializer_class = OriginationPointSerializer