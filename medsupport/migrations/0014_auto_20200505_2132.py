# Generated by Django 3.0.4 on 2020-05-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medsupport', '0013_auto_20200504_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='comment',
            field=models.CharField(blank=True, default='Поки не додато жодного коментаря', max_length=100, verbose_name='Короткий коментар від затверджувача'),
        ),
    ]
