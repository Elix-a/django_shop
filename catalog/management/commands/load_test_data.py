from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур, предварительно удаляя старые'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Удаление старых данных...'))
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING('Загрузка категорий...'))
        call_command('loaddata', 'categories.json')

        self.stdout.write(self.style.WARNING('Загрузка продуктов...'))
        call_command('loaddata', 'products.json')

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены!'))
