from django.urls import path
from .views import login, logout, signup

from .import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
