from django.core.management.base import BaseCommand
from django.utils import timezone

from CurrencyAPI.models import Currency

class Command(BaseCommand):
    help = 'Update Currency'

    def add_arguments(self, parser):
        parser.add_argument('currency_id', type=int, help='Currency ID')
        parser.add_argument('new_rate', type=float, help='New rate')

    def handle(self, *args, **kwargs):
        currency_id = kwargs['currency_id']
        new_rate = kwargs['new_rate']

        currency = Currency.objects.get(pk=currency_id)
        currency.rate = new_rate
        currency.save()



        