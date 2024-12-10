from .models import Cart

def cart_total_quantity(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_key = request.session.session_key
        if not session_key:
            return {'cart_total_quantity': 0}
        cart = Cart.objects.filter(session_key=session_key).first()

    total_quantity = sum(item.quantity for item in cart.cartitem_set.all()) if cart else 0
    return {'cart_total_quantity': total_quantity}
