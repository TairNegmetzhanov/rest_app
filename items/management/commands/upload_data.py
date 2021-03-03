import json
from django.core.management.base import BaseCommand, CommandError
from items.models import Item as Good


class Command(BaseCommand):
    help = 'Upload data from file'

    def handle(self, *args, **options):
        with open('data/foodboxes.json', mode='r', encoding='utf-8') as file:
            goods = json.load(file)
            for each_good in goods:
                print(each_good.get("title"))
                Good.objects.update_or_create(
                    title=each_good.get('title'),
                    description=each_good.get('description'),
                    image=each_good.get('image'),
                    weight=each_good.get('weight_grams'),
                    price=each_good.get('price'),
                )
