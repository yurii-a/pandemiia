# Generated by Django 3.0.4 on 2020-03-25 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medsupport', '0014_auto_20200326_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitalmodel',
            old_name='full_name',
            new_name='contact_person',
        ),
    ]
