# Generated by Django 2.1.2 on 2018-12-18 13:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hoursCalc', '0004_auto_20181210_1539'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HoursDay',
            new_name='Shift',
        ),
        migrations.AlterModelOptions(
            name='shift',
            options={'ordering': ['date']},
        ),
    ]