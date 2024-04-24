from django.urls import path
from . import views

urlpatterns = [
    path('tests/', views.TestList.as_view()),
    path('tests/<int:pk>/', views.TestDetail.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('answers/<int:pk>/', views.AnswerDetail.as_view()),
]
