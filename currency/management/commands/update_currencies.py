from django.core.management.base import BaseCommand
import requests
from currency.models import Currency


class Command(BaseCommand):
    help = "Update currencies"

    def handle(self, *args, **options):
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        if response.status_code == 200:
            currencies = response.json()["Valute"]
            for code in currencies:
                currency = Currency.objects.filter(code=code, name=currencies[code]["Name"]).first()
                if currency:
                    currency.rate = currencies[code]["Value"]
                    currency.save()
                    self.stdout.write(
                        self.style.SUCCESS(f"Валюта {code} обновлена")
                    )
                else:
                    Currency.objects.create(code=code, name=currencies[code]["Name"], rate=currencies[code]["Value"])
                    self.stdout.write(
                        self.style.SUCCESS(f"Валюта {code} добавлена в БД")
                    )

        else:
            self.stdout.write(
                self.style.ERROR(f"Запрос вернул код ответа: {response.status_code}. Ответ: {response.json()}")
            )
