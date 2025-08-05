from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя валюты")
    code = models.CharField(max_length=3, verbose_name="Код валюты")
    rate = models.DecimalField(max_digits=4, decimal_places=4,
                               verbose_name="Курс валюты к рублю")  # max 4 знака после запятой

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"
