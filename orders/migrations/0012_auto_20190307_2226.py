# Generated by Django 2.1.5 on 2019-03-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20190307_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(max_length=80),
        ),
    ]
