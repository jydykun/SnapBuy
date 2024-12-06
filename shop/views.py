from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm
from .models import Product, Cart, CartItem
from .utils.context import context_home



def index(request):
    products = Product.objects.all()
    c = {"products":products} #context_home()
    return render(request, "shop/index.html", c)

@login_required()
def dashboard(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.user != user:
        return HttpResponse("Wa kay access")

    c = {"user":user}
    return render(request, "shop/dashboard/dashboard.html", c)


############### CART SYSTEM VIEWS ###############
def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user = request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)

    cart_item, created = CartItem.objects.get_or_create(
        cart = cart,
        product = product
    )

    cart_item.quantity += quantity
    cart_item.save()

    return cart_item

def add_to_cart_view(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        cart_item = add_to_cart(request, product_id, quantity)
        return JsonResponse({"success": True, "quantity": cart_item.quantity})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

def test(request):
    test = request.POST.get("key", 100)
    items = request.session.get("cart")
    return HttpResponse(items["1"]["name"])







############### AUTHENTICATION ###############

def login(request):
    # This is a backup logic if the authentication checking in
    # in the template doesn't work
    user = request.user

    if user.is_authenticated:
        return redirect("shop:dashboard", username=user.username)

    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, "Login Successful")
            return redirect("shop:dashboard", username=user.username)
    else:
        form = CustomAuthenticationForm()

    c = {"form":form }    
    return render(request, "shop/auth/login.html", c)

def logout(request):
    auth_logout(request)
    messages.success(request, "You’re now logged out. Have a great day!")
    return redirect("shop:login")

def signup(request):
    if request.user.is_authenticated:
        return redirect("shop:index")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect("shop:index")
    else:
        form = UserCreationForm()

    c = {"form":form}
    return render(request, "shop/auth/signup.html", c)
