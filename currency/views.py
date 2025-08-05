from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from currency.models import Currency
from currency.paginators import CurrencyPagination
from currency.serializers import CurrencySerializers


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all().order_by('name')
    serializer_class = CurrencySerializers
    pagination_class = CurrencyPagination



class CurrencyRetrieveAPIView(RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializers

