from django.urls import path
from . import views

urlpatterns = [
    path('tests/start/', views.StartTest.as_view()),
    path('tests/display/', views.DisplayQuestion.as_view()),
    path('tests/finish/', views.FinishTest.as_view()),
]