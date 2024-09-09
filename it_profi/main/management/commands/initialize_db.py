from datetime import datetime

from django.core.management.base import BaseCommand
from main.models import Problem, Order, Article

PROBLEMS_NAME = ['Компьютер не включается', 'Компьютер зависает', 'Компьютер отключается', 'Компьютер сильно шумит',
                 'Необходима чистка от вирусов', 'Другая неполадка']


class Command(BaseCommand):
    help = u'Тестовая инициализация БД'

    def handle(self, *args, **options):
        try:
            for prob in PROBLEMS_NAME:
                problem_object = Problem.objects.create(problem=prob, is_active=True)
                problem_object.save()
            # order_1 = Order.objects.create(client='Иванов Иван Иванович', phone='+71111111111', problem='Компьютер не включается', date=datetime.now, set_active=True)
            # order_1.save()

            # order_2 = Order.objects.create(client='Петрова Марина Викторовна', phone='+72222222222', problem=1, date=datetime.now)
            # order_2.save()

            print('База успешно инициализирована!')
        except:
            print('Ошибка при добавлении в БД')