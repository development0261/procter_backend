# Generated by Django 4.1.5 on 2023-02-16 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Placement_site', '0002_alter_user_settings_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_settings',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 16, 13, 4, 13, 655876), null=True),
        ),
    ]
