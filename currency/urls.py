from django.urls import path
from currency.views import CurrencyListAPIView, CurrencyRetrieveAPIView

urlpatterns = [
    path("currencies/", CurrencyListAPIView.as_view()),
    path("currency/<int:pk>/", CurrencyRetrieveAPIView.as_view())
]
