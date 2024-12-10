from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm
from .models import Product, Cart, CartItem, TestModel
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

def add_to_cart(request, product_id):
    # Get the product ID
    product = Product.objects.get(id=product_id)

    # Save the authenticated user to the database
    # Else create a session for anonymous user
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # Get the session_key
        session_key = request.session.session_key
        # If none create the session
        if not session_key:
            session_key = request.session.create()
        # Save the session to the database
        cart, created = Cart.objects.get_or_create(session_key=session_key)

    cart_item, created = CartItem.objects.get_or_create(
        cart = cart,
        product = product
    )
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()

    total_quantity = sum(item.quantity for item in cart.cartitem_set.all())
    return JsonResponse({"total_quantity": total_quantity})
        


def test(request):
    post = request.session.create()
    return HttpResponse(post)







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
