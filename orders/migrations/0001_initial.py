# Generated by Django 2.1.5 on 2019-01-27 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('address', models.CharField(max_length=100)),
                ('message', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('Ordered', 'Ordered'), ('Shipped', 'Shipped')], default='Ordered', max_length=16)),
                ('delivered', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['order_time'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Item')),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Small', max_length=8)),
            ],
            options={
                'verbose_name': 'Dinner Platter',
                'verbose_name_plural': 'Dinner Platters',
            },
            bases=('orders.item',),
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Item')),
            ],
            bases=('orders.item',),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Item')),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Small', max_length=8)),
                ('crust', models.CharField(choices=[('Regular', 'Regular'), ('Sicilian', 'Sicilian')], default='Regular', max_length=8)),
                ('toppings_num', models.IntegerField(choices=[(0, 'Cheese'), (1, '1 topping'), (2, '2 toppings'), (3, '3 toppings'), (6, 'Special')], default=0)),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
            bases=('orders.item',),
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Item')),
            ],
            bases=('orders.item',),
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Item')),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Large', 'Large')], default='Small', max_length=8)),
                ('extra', models.BooleanField(default=False)),
            ],
            bases=('orders.item',),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Item'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='orders.OrderItem', to='orders.Item'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
