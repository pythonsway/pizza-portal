from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views.generic import (
    UpdateView, ListView, DetailView, DeleteView, CreateView)
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy

from .forms import (
    SignUpForm, UserInformationUpdateForm,
    OrderPizzaForm, OrderSubForm, OrderOtherForm)
from .models import (
    Pizza, Topping, Sub, Pasta, Salad, Dinner, Order, OrderItem)

import decimal


def index(request):
    return render(request, 'orders/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user


def menu(request):
    pizzas_Sreg = Pizza.objects.filter(
        crust__contains='Regular').filter(size__contains='Small')
    pizzas_Lreg = Pizza.objects.filter(
        crust__contains='Regular').filter(size__contains='Large')
    pizzas_reg = zip(pizzas_Sreg, pizzas_Lreg)
    pizzas_Ssic = Pizza.objects.filter(
        crust__contains='Sicilian').filter(size__contains='Small')
    pizzas_Lsic = Pizza.objects.filter(
        crust__contains='Sicilian').filter(size__contains='Large')
    pizzas_sic = zip(pizzas_Ssic, pizzas_Lsic)
    toppings = Topping.objects.all()
    subs_S = Sub.objects.filter(size__contains='Small')
    subs_L = Sub.objects.filter(size__contains='Large')
    subs = zip(subs_S, subs_L)
    pastas = Pasta.objects.all()
    salads = Salad.objects.all()
    dinners_S = Dinner.objects.filter(size__contains='Small')
    dinners_L = Dinner.objects.filter(size__contains='Large')
    dinners = zip(dinners_S, dinners_L)

    context = {
        'pizzas_reg': pizzas_reg,
        'pizzas_sic': pizzas_sic,
        'toppings': toppings,
        'subs': subs,
        'pastas': pastas,
        'salads': salads,
        'dinners': dinners,
    }

    return render(request, 'orders/menu.html', context)


@login_required
def new_pizza(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == 'POST':
        form = OrderPizzaForm(request.POST, pizza=pizza)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.item = pizza
            order_item.user = request.user
            order_item.subtotal = (pizza.price * order_item.quantity)
            # order_item.toppings_num = pizza.toppings_num
            order_item.save()
            # for i in range(pizza.toppings_num):
            #     name = f'topping{i + 1}'
            #     t = request.POST.get(name)
            #     order_item.toppings.add(t)
            form.save_m2m()
            messages.success(request, f'{pizza.name} added to cart')
            return redirect('menu')
    else:
        form = OrderPizzaForm(pizza=pizza)
    return render(request, 'orders/item.html', {'form': form, 'title': pizza})


# def load_toppings(request):
#     topping_id = request.GET.get('topping1')
#     toppings = Topping.objects.exclude(name__in=topping_id)
#     return render(request, 'orders/topping_dropdown_list.html', {'toppings': toppings})


@login_required
def new_sub(request, pk):
    sub = get_object_or_404(Sub, pk=pk)
    if request.method == 'POST':
        form = OrderSubForm(request.POST)
        if form.is_valid():
            EXTRA_COST = decimal.Decimal('0.0')
            order_item = form.save(commit=False)
            order_item.item = sub
            order_item.user = request.user
            if order_item.extra:
                EXTRA_COST = decimal.Decimal('0.5')
            order_item.subtotal = (
                (sub.price + EXTRA_COST) * order_item.quantity)
            order_item.save()
            messages.success(request, f'{sub.name} added to cart')
            return redirect('menu')
    else:
        form = OrderSubForm()
    return render(request, 'orders/item.html', {'form': form, 'title': sub})


@login_required
def new_pasta(request, pk):
    pasta = get_object_or_404(Pasta, pk=pk)
    if request.method == 'POST':
        form = OrderOtherForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.item = pasta
            order_item.user = request.user
            order_item.subtotal = (pasta.price * order_item.quantity)
            order_item.save()
            messages.success(request, f'{pasta.name} added to cart')
            return redirect('menu')
    else:
        form = OrderOtherForm()
    return render(request, 'orders/item.html', {'form': form, 'title': pasta})


@login_required
def new_salad(request, pk):
    salad = get_object_or_404(Salad, pk=pk)
    if request.method == 'POST':
        form = OrderOtherForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.item = salad
            order_item.user = request.user
            order_item.subtotal = (salad.price * order_item.quantity)
            order_item.save()
            messages.success(request, f'{salad.name} added to cart')
            return redirect('menu')
    else:
        form = OrderOtherForm()
    return render(request, 'orders/item.html', {'form': form, 'title': salad})


@login_required
def new_dinner(request, pk):
    dinner = get_object_or_404(Dinner, pk=pk)
    if request.method == 'POST':
        form = OrderOtherForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.item = dinner
            order_item.user = request.user
            order_item.subtotal = (dinner.price * order_item.quantity)
            order_item.save()
            messages.success(request, f'{dinner.name} added to cart')
            return redirect('menu')
    else:
        form = OrderOtherForm()
    return render(request, 'orders/item.html', {'form': form, 'title': dinner})


# class PizzaDetailView(DetailView):
#     model = Pizza

# @method_decorator(login_required, name='dispatch')
# class PizzaUpdateView(UpdateView):
#     model = Pizza
#     template_name = 'orders/item.html'
#     context_object_name = 'item'
#     fields = ('name', 'price', 'size', 'crust', 'toppings')


class MenuListView(ListView):
    model = Pizza
    context_object_name = 'pizzas'
    template_name = 'orders/menu.html'


# # without context processor
# class OrderItemListView(LoginRequiredMixin, ListView):
#     model = OrderItem

#     def get_queryset(self):
#         return OrderItem.objects.filter(user=self.request.user, order__isnull=True)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['total'] = OrderItem.objects.filter(
#             user=self.request.user, order__isnull=True).aggregate(Sum('subtotal'))
#         return context

# class DeleteOrderItem(LoginRequiredMixin, DeleteView):
#     model = OrderItem
#     success_url = reverse_lazy('cart')

#     def delete(self, request, *args, **kwargs):
#         obj = self.get_object()
#         messages.success(self.request, 'Item deleted')
#         return super(DeleteOrderItem, self).delete(request, *args, **kwargs)


class OrderItemListView(LoginRequiredMixin, ListView):
    model = OrderItem


# AJAX
def orderitem_delete(request, pk):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    data = {}
    if request.method == 'POST':
        orderitem.delete()
        data['orderitem_list'] = render_to_string(
            'orders/includes/partial_orderitem_list.html', request=request)
    return JsonResponse(data)


# SuccessMessageMixin ???????????????????????????????????????????????????
class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['address', 'message']
    # form_class = OrderForm
    # success_url = reverse_lazy('ordered')

    def form_valid(self, form):
        user_orderitems = OrderItem.objects.filter(
            user=self.request.user, order__isnull=True)
        self.object = form.save(commit=False)
        form.instance.total = user_orderitems.aggregate(Sum('subtotal'))[
            'subtotal__sum']
        self.object.save()
        user_orderitems.update(order=self.object)
        # form.instance.items.set(OrderItem.objects.filter(user=self.request.user))
        messages.success(self.request, 'Order placed')
        return super().form_valid(form)

    # def get_form_kwargs(self):
    #     kwargs = super(OrderCreate, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs


class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['name']


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order


class OrdersListView(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(orderitem__user=self.request.user)
