# Generated by Django 3.0 on 2019-12-24 04:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191224_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 24, 10, 8, 26, 781985), verbose_name='date published'),
        ),
    ]
