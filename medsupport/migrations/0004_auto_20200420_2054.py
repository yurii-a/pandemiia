# Generated by Django 3.0.4 on 2020-04-20 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medsupport', '0003_auto_20200420_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solutionimage',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='medsupport.Solution', verbose_name='Рішення'),
        ),
    ]
