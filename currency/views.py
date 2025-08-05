from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from currency.models import Currency
from currency.serializers import CurrencySerializers


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializers


class CurrencyRetrieveAPIView(RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializers

