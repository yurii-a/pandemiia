# Generated by Django 3.0.4 on 2020-04-30 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medsupport', '0009_solution_solution_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solution_types', to='medsupport.SolutionType', verbose_name='Тип рішення'),
        ),
    ]
