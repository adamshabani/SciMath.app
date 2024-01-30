from django.urls import path
from django.contrib import admin
from .views import Quiz,RandomQuestion,QuizQuestion

App_name = 'QuizApp'

urlpatterns = [
    path('',Quiz.as_view(), name='quiz'),
    path('r/<str:topics>/',RandomQuestion.as_view(), name='random'),
    path('q/<str:topics>/',QuizQuestion.as_view(), name='questions'),
      
]
