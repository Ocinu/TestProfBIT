import random
import string
from django.core.management.base import BaseCommand

from Nomenclature.models import Category, Product


def get_name() -> str:
    return ''.join(random.choice(string.ascii_letters) for i in range(8))


def get_category_list(count: int) -> list:
    category_list = []
    while len(category_list) < count:
        name = get_name()
        if name not in category_list:
            category_list.append(name)
    return category_list


class Command(BaseCommand):
    help = 'Fill DB'

    def add_arguments(self, parser):
        parser.add_argument('category_amount', type=int, help='Number of category')
        parser.add_argument('product_amount', type=int, help='Number of products in category')

    def handle(self, *args, **options):
        category_list = get_category_list(options['category_amount'])
        records = 0
        for category_name in category_list:
            count = 0
            category_instance = Category.objects.get_or_create(name=category_name)
            while count < options['product_amount']:
                try:
                    Product.objects.create(
                        name=get_name(),
                        category=category_instance[0],
                        price=random.randint(1, 9999),
                        status=random.choice(['In stock', 'Out of stock']),
                        remains=random.randint(1, 999)
                    )
                    count += 1
                    records += 1
                except Exception as e:
                    self.stdout.write(f'{e}')
        self.stdout.write(f"Created {records} records")
