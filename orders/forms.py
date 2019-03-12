from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import (
    Pizza, Topping, Sub, Pasta, Salad, Dinner, Order, OrderItem)


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=64, required=True,
                            widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserInformationUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class OrderPizzaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pizza = kwargs.pop('pizza')
        super(OrderPizzaForm, self).__init__(*args, **kwargs)
        if pizza.toppings_num == 0:
            self.fields['toppings'].disabled = True

        self.fields['toppings_num'] = forms.CharField(
            widget=forms.HiddenInput(),
            initial=pizza.toppings_num,
            label='')

    class Meta:
        model = OrderItem
        fields = ['quantity', 'toppings']


class OrderSubForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity', 'extra']


class OrderOtherForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']
