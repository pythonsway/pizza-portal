# Generated by Django 2.1.5 on 2019-02-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190210_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='extra',
            field=models.BooleanField(default=False, help_text='Price: +0.50', verbose_name='Extra Cheese'),
        ),
    ]
