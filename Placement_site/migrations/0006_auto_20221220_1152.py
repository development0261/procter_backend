# Generated by Django 3.2.7 on 2022-12-20 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Placement_site', '0005_auto_20221220_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_details',
            name='exam_hours_advanced',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 20, 11, 52, 20, 139686), max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='exam_details',
            name='exam_hours_beginner',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 20, 11, 52, 20, 139686), max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='exam_details',
            name='exam_hours_intermediate',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 20, 11, 52, 20, 139686), max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 20, 11, 52, 20, 137687), null=True),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 12, 20, 11, 52, 20, 136666), null=True),
        ),
    ]
