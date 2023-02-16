# Generated by Django 4.1.5 on 2023-02-16 08:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Placement_site', '0003_alter_user_settings_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamInstructions',
            fields=[
                ('instruction_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('instruction', models.CharField(blank=True, max_length=2024)),
                ('isactive', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Exam Instructions',
                'verbose_name_plural': 'Exam Instructions',
            },
        ),
        migrations.CreateModel(
            name='Interview_Language',
            fields=[
                ('interview_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('language', models.CharField(blank=True, max_length=20, null=True)),
                ('isactive', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Interview Language',
                'verbose_name_plural': 'Interview Language',
            },
        ),
        migrations.AlterField(
            model_name='user_settings',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 16, 14, 10, 58, 756644), null=True),
        ),
        migrations.CreateModel(
            name='Language_Settings',
            fields=[
                ('Language_Settings_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('beginner_level', models.URLField(blank=True, null=True)),
                ('beginner_level_hours', models.TimeField(blank=True, default=datetime.datetime(2023, 2, 16, 14, 10, 58, 758644), max_length=10, null=True)),
                ('intermediate_level', models.URLField(blank=True, null=True)),
                ('intermediate_level_hours', models.TimeField(blank=True, default=datetime.datetime(2023, 2, 16, 14, 10, 58, 758644), max_length=10, null=True)),
                ('advanced_level', models.URLField(blank=True, null=True)),
                ('advanced_level_hours', models.TimeField(blank=True, default=datetime.datetime(2023, 2, 16, 14, 10, 58, 758644), max_length=10, null=True)),
                ('isactive', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('interview_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Placement_site.interview_language')),
            ],
            options={
                'verbose_name': 'Language Settings',
                'verbose_name_plural': 'Language Settings',
            },
        ),
    ]
