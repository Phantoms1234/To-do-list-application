# Generated by Django 4.2.3 on 2024-10-12 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_end_date_alter_task_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='frequency',
            field=models.CharField(blank=True, choices=[(datetime.timedelta(days=1), 'DAILY'), (datetime.timedelta(days=7), 'WEEKLY'), (datetime.timedelta(days=30), 'MONTHLY')], max_length=20, null=True),
        ),
    ]
