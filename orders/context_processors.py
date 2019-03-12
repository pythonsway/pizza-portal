from django.db.models import Count, Sum

from .models import OrderItem


# pass 'orderitem_list' to all pages
def get_orderitems(request):
    orderitem_list = []
    total = 0
    if request.user.is_authenticated: 
        orderitem_list = OrderItem.objects.filter(user=request.user, order__isnull=True)
        total = orderitem_list.aggregate(Sum('subtotal'))
    return {'orderitem_list_c': orderitem_list, 'total': total}
