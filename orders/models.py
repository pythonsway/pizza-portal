from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f'{self.name} (Price: {self.price})'


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Pizza(Item):
    REGULAR = 'Regular'
    SICILIAN = 'Sicilian'
    CRUST_CHOICES = (
        (REGULAR, 'Regular'),
        (SICILIAN, 'Sicilian')
    )
    S = 'Small'
    L = 'Large'
    SIZE_CHOICES = (
        (S, 'Small'),
        (L, 'Large')
    )
    TOPPINGS_NUM = (
    (0, 'Cheese'),
    (1, '1 topping'),
    (2, '2 toppings'),
    (3, '3 toppings'),
    (6, 'Special'),
    )
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pizzas')
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, default=S)
    crust = models.CharField(max_length=8, choices=CRUST_CHOICES, default=REGULAR)
    toppings_num = models.PositiveIntegerField(choices=TOPPINGS_NUM, default=0)

    def get_absolute_url(self):
        return reverse('pizza-detail', args=[str(self.id)])

    def __str__(self):
        return f'Pizza {self.crust} {self.name} {self.size}'


class Sub(Item):
    S = 'Small'
    L = 'Large'
    SIZE_CHOICES = (
        (S, 'Small'),
        (L, 'Large')
    )
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, default=S)

    def get_absolute_url(self):
        return reverse('sub-detail', args=[str(self.id)])

    def __str__(self):
        return f'Sub {self.name} {self.size}'


class Pasta(Item):
    def get_absolute_url(self):
        return reverse('pasta-detail', args=[str(self.id)])

    def __str__(self):
        return f'Pasta {self.name}'


class Salad(Item):
    def get_absolute_url(self):
        return reverse('salad-detail', args=[str(self.id)])

    def __str__(self):
        return f'Salad {self.name}'


class Dinner(Item):
    S = 'Small'
    L = 'Large'
    SIZE_CHOICES = (
        (S, 'Small'),
        (L, 'Large')
    )
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, default=S)

    class Meta:
        verbose_name = 'Dinner Platter'
        verbose_name_plural = 'Dinner Platters'
        
    def get_absolute_url(self):
        return reverse('dinner-detail', args=[str(self.id)])

    def __str__(self):
        return f'Dinner plate {self.name} {self.size}'


class Order(models.Model):
    ORDERED = 'Ordered'
    SHIPPED = 'Shipped'
    STATUS_CHOCIES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )
    order_time = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(decimal_places=2, max_digits=5)
    address = models.TextField(max_length=80)
    message = models.TextField(max_length=100, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOCIES, default=ORDERED)
    delivered = models.BooleanField(default=False)
    # items = models.ManyToManyField(Item, through='OrderItem')

    class Meta:
        ordering = ['order_time']

    def get_absolute_url(self):
        return reverse('ordered', args=[str(self.id)])
        
    def __str__(self):
        return f'Order #{self.pk}'


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    toppings = models.ManyToManyField(Topping, blank=True) 
    extra = models.BooleanField('Extra Cheese', help_text='Price: +0.50', default=False)
    subtotal = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f'{self.item} for {self.order}'
