from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Создает группы и назначает права'

    def handle(self, *args, **kwargs):
        # Получаем права
        try:
            unpublish_perm = Permission.objects.get(codename='can_unpublish_product')
            delete_perm = Permission.objects.get(codename='delete_product')
        except Permission.DoesNotExist:
            self.stdout.write(self.style.ERROR('Права не найдены. Выполните миграции.'))
            return

        # Создаем группу "Модератор продуктов"
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Назначаем права
        moderator_group.permissions.add(unpublish_perm, delete_perm)

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана и настроена!'))
        else:
            self.stdout.write(self.style.SUCCESS('Права для группы "Модератор продуктов" обновлены!'))
