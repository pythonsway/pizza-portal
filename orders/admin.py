from django.contrib import admin

from .models import Pizza, Topping, Sub, Pasta, Salad, Dinner, OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('order_time', 'total', 'delivered')
    list_editable = ('delivered',)
    list_filter = ('order_time', 'status')
    search_fields = ('user', 'message', 'address')


@admin.register(OrderItem)
class ToppingAdmin(admin.ModelAdmin):
    filter_horizontal = ('toppings',)

    # filter fields based on item
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if hasattr(obj.item, 'pizza'):
            fields.remove('extra')
        elif hasattr(obj.item, 'sub'):
            fields.remove('toppings')
        else:
            fields.remove('extra')
            fields.remove('toppings')
        return fields


# titles
admin.site.site_header = "Pizza Admin"
admin.site.site_title = "Pizza Admin Portal"
admin.site.index_title = "Welcome to Pizza Portal"


# Menu
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner)


# Instead @admin.register decorator 
# admin.site.register(OrderItem)

# admin.site.register(Pizza, ToppingAdmin)
# admin.site.register(Order, OrderAdmin)
