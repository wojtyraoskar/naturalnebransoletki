from django.shortcuts import render, redirect, get_object_or_404
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models import Product
from .cart import Cart
from .forms import CheckoutForm
from .models import Order, OrderItem
from .models import NewsletterSubscriber

from django.http import JsonResponse


def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'shop/home.html', {'products': products})


def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'cart_item_count': len(cart),
        })

    return JsonResponse({
        'success': True,
        'name': product.name,
        'price': float(product.price),
        'quantity': 1,
        'cart_item_count': len(cart),
        })

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('view_cart')

def view_cart(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})


stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            line_items = []
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                product=item['product'],
                    price=item['product'].price,
                    quantity=item['quantity']
                )
                line_items.append({
                    'price_data': {
                        'currency': 'pln',
                        'unit_amount': int(item['product'].price * 100),  # in grosze
                        'product_data': {
                            'name': item['product'].name,
                        },
                    },
                    'quantity': item['quantity'],
                })

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri('/order-confirmation/'),
                cancel_url=request.build_absolute_uri('/cart/'),
                customer_email=order.email,
                metadata={'order_id': order.id},
            )

            cart.clear()
            return redirect(checkout_session.url, code=303)
    else:
        form = CheckoutForm()

    return render(request, 'shop/checkout.html', {'form': form, 'cart': cart})


def order_confirmation(request):
    return render(request, 'shop/order_confirmation.html')

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
                messages.success(request, 'Dziękujemy za zapisanie się do newslettera!')
            else:
                messages.info(request, 'Ten adres e-mail już jest zapisany.')
        else:
            messages.error(request, 'Proszę podać poprawny adres e-mail.')
    return redirect('/#newsletter')
def contact(request):
    return render(request, 'shop/contact.html')

def about(request):
    return render(request, 'shop/about.html')
