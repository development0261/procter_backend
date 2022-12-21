# Generated by Django 3.2.7 on 2022-12-20 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Placement_site', '0004_auto_20221122_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_details',
            name='exam_date',
        ),
        migrations.RemoveField(
            model_name='exam_details',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='subject_details',
            name='exam_form',
        ),
        migrations.RemoveField(
            model_name='subject_details',
            name='exam_hours',
        ),
        migrations.AddField(
            model_name='exam_details',
            name='exam_form_advanced',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exam_details',
            name='exam_form_beginner',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exam_details',
            name='exam_form_intermediate',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exam_details',
            name='exam_hours_advanced',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 20, 10, 57, 19, 120409), max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='exam_details',
            name='exam_hours_beginner',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 20, 10, 57, 19, 120409), max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='exam_details',
            name='exam_hours_intermediate',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 12, 20, 10, 57, 19, 120409), max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 20, 10, 57, 19, 118409), null=True),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 12, 20, 10, 57, 19, 118409), null=True),
        ),
    ]