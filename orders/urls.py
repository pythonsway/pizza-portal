"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.OrderItemListView.as_view(), name='cart'),
    # path('cart/delete/<int:pk>', views.DeleteOrderItem.as_view(), name='delete-item'),
    path('cart/delete/<int:pk>', views.orderitem_delete, name='delete-item'),
    path('cart/checkout/', views.OrderCreate.as_view(), name='checkout'),
    path('cart/ordered/<int:pk>', views.OrderDetailView.as_view(), name='ordered'),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    # path('ajax/load-toppings/', views.load_toppings, name='load-toppings'),
    # path('pizza/<int:pk>', views.PizzaDetailView.as_view(), name='pizza-detail'),
    path('pizza/<int:pk>', views.new_pizza, name='pizza-detail'),
    path('sub/<int:pk>', views.new_sub, name='sub-detail'),
    path('pasta/<int:pk>', views.new_pasta, name='pasta-detail'),
    path('salad/<int:pk>', views.new_salad, name='salad-detail'),
    path('dinner/<int:pk>', views.new_dinner, name='dinner-detail'),
]
