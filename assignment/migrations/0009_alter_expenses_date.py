# Generated by Django 4.1.2 on 2023-03-15 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0008_alter_accounts_goal_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 15)),
        ),
    ]