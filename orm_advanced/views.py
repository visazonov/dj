from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from orm_advanced.models import Order


def list_orders(request):
    # orders = Order.objects.all()   # получили все заказы
    orders = Order.objects.filter(
        positions__product__price__gte=600
    )  # все заказы где есть продукт c ценой >=600 (gte это >=; lte <=; gt>; lt <)
    context = {"orders": orders}
    return render(request, "orders.html", context)
