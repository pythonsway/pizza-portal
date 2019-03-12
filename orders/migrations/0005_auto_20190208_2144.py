# Generated by Django 2.1.5 on 2019-02-08 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190206_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='toppings',
            field=models.ManyToManyField(blank=True, null=True, to='orders.Topping'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='toppings_num',
            field=models.PositiveIntegerField(choices=[(0, 'Cheese'), (1, '1 topping'), (2, '2 toppings'), (3, '3 toppings'), (6, 'Special')], default=0),
        ),
    ]
