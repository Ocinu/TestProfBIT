import random
from django.core.management.base import BaseCommand

from Nomenclature.models import Product


class Command(BaseCommand):
    help = 'Change product'

    def add_arguments(self, parser):
        parser.add_argument('product_name', type=str, help='Product name')

    def handle(self, *args, **options):
        try:
            product = Product.objects.get(name=options['product_name'])
            product.price = random.randint(1, 9999)
            product.status = random.choice(['In stock', 'Out of stock'])
            product.remains = random.randint(1, 999)
            product.save(update_fields=['price', 'status', 'remains'])
            self.stdout.write('Successful')
        except Exception as e:
            self.stdout.write(f'{e}')

