# Generated by Django 4.2.3 on 2024-10-13 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_task_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='frequency',
            field=models.CharField(choices=[(datetime.timedelta(days=1), 'DAILY'), (datetime.timedelta(days=7), 'WEEKLY'), (datetime.timedelta(days=30), 'MONTHLY')], default=datetime.timedelta(days=7), max_length=20),
            preserve_default=False,
        ),
    ]
