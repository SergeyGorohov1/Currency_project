from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from currency.models import Currency


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()


class CurrencyRetrieveAPIView(RetrieveAPIView):
    queryset = Currency.objects.all()

