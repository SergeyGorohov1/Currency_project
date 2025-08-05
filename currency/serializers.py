from rest_framework.serializers import ModelSerializer

from currency.models import Currency


class CurrencySerializers(ModelSerializer):
    class Meta:
        model = Currency
        exclude = ("id",)
