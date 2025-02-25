import stripe

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .models import Item

def buy_item(request, id):
    """View для получения id сессии"""
    item = Item.objects.get(id=id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )

    return JsonResponse({'session_id': session.id})


def item_detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, 'item_detail.html', context)