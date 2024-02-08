# Generated by Django 5.0.2 on 2024-02-08 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notification', '0001_initial'),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.reservation'),
        ),
    ]