# Generated by Django 5.0.6 on 2024-05-12 10:23

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main', verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('source', models.CharField(max_length=50, verbose_name='Источник')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Статьи',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField(max_length=30, verbose_name='Проблема, неполадка ПК')),
            ],
            options={
                'verbose_name': 'Неисправность',
                'verbose_name_plural': 'Проблемы и неисправности ПК',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=40, verbose_name='Клиент')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата заказа')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.problem')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
