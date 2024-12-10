from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/<str:username>", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("add_to_cart/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.view_cart, name="view_cart"),

    path("test/", views.test, name="test")
    
]