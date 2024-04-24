from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_api),
    path('login/', views.login_api),
    path('logout/', views.logout_api),
]