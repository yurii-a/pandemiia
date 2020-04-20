# Generated by Django 3.0.4 on 2020-04-20 10:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=200, verbose_name='ПІБ контактної особи')),
                ('position', models.CharField(blank=True, max_length=200, verbose_name='Посада')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='Телефонний номер має бути в форматі +380123456789', regex='^\\+?3?8?(0\\d{9})$')], verbose_name='Контактний телефон')),
            ],
            options={
                'verbose_name': 'Контактна особа',
                'verbose_name_plural': 'Контактні особи',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Назва медзакладу')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Опис')),
                ('region', models.IntegerField(choices=[(0, '----'), (1, 'Вінницька область'), (2, 'Волинська область'), (3, 'Дніпропетровська область'), (4, 'Донецька область'), (5, 'Житомирська область'), (6, 'Закарпатська область'), (7, 'Запорізька область'), (8, 'Івано-Франківська область'), (9, 'Київська область'), (10, 'Кіровоградська область'), (11, 'Луганська область'), (12, 'Львівська область'), (13, 'Миколаївська область'), (14, 'Одеська область'), (15, 'Полтавська область'), (16, 'Рівненська область'), (17, 'Сумська область'), (18, 'Тернопільська область'), (19, 'Харківська область'), (20, 'Херсонська область'), (21, 'Хмельницька область'), (22, 'Черкаська область'), (23, 'Чернівецька область'), (24, 'Чернігівська область'), (25, 'м. Київ')], default=0, verbose_name='Область')),
                ('city', models.CharField(max_length=50, verbose_name='Місто')),
                ('zip_code', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(message='Поштовий індекс має бути в форматі 01234', regex='^\\d{5}$')], verbose_name='Поштовий індекс')),
                ('line1', models.CharField(max_length=100, verbose_name='Повний адрес')),
                ('company_code', models.IntegerField(blank=True, null=True, verbose_name='Код ЄДРПОУ')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Електронна адреса установи')),
                ('geo_lat', models.CharField(blank=True, max_length=50, null=True, verbose_name='Геопозиція: широта (lat)')),
                ('geo_lng', models.CharField(blank=True, max_length=50, null=True, verbose_name='Геопозиція: довгота (lng)')),
            ],
            options={
                'verbose_name': 'Медичний заклад',
                'verbose_name_plural': 'Медичні заклади',
            },
        ),
        migrations.CreateModel(
            name='HospitalCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Категорія закладів')),
            ],
            options={
                'verbose_name': 'Категорія закладів',
                'verbose_name_plural': 'Категорії закладів',
            },
        ),
        migrations.CreateModel(
            name='SolutionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Категорія рішень')),
            ],
            options={
                'verbose_name': 'Категорія рішень',
                'verbose_name_plural': 'Категорії рішень',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва товару')),
                ('description', models.CharField(max_length=1000, verbose_name='Опис')),
                ('main_image', models.ImageField(blank=True, upload_to='article_images', verbose_name='Головне зображення')),
                ('attachment', models.FileField(blank=True, upload_to='article_attachment', verbose_name='Прикріплений файл')),
                ('instruction', models.TextField(blank=True, max_length=1000, verbose_name='Інструкція')),
                ('materials', models.CharField(blank=True, max_length=200, verbose_name='Матеріали, з яких можна виготовляти')),
                ('tools', models.CharField(blank=True, max_length=200, verbose_name='Засоби для виготовлення')),
                ('approved_by', models.CharField(blank=True, max_length=200, verbose_name='Ким затверджено')),
                ('categories', models.ManyToManyField(to='medsupport.SolutionCategory', verbose_name='Категорії')),
            ],
            options={
                'verbose_name': 'Рішення',
                'verbose_name_plural': 'Рішення',
            },
        ),
        migrations.CreateModel(
            name='PhoneContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=13, verbose_name='Контактний телефон')),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medsupport.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_needed', models.PositiveIntegerField(default=0, verbose_name='Скільки ще потрібно')),
                ('quantity_received', models.PositiveIntegerField(default=0, verbose_name='Скільки вже отримано')),
                ('units', models.CharField(choices=[('pieces', 'шт'), ('packs', 'уп'), ('vials', 'фл')], default='pieces', max_length=255, verbose_name='Одиниці вимірювання')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата створення')),
                ('edited', models.DateTimeField(auto_now=True, null=True, verbose_name='Востаннє відредаговано')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medsupport.Hospital', verbose_name='Лікарня')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medsupport.Solution')),
            ],
            options={
                'verbose_name': 'Потреба',
                'verbose_name_plural': 'Потреби',
            },
        ),
        migrations.AddField(
            model_name='hospital',
            name='categories',
            field=models.ManyToManyField(to='medsupport.HospitalCategory'),
        ),
    ]
