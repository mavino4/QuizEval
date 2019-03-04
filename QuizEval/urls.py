from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name= "QuizEval"),
    path('<int:q_id>/<str:asdf>/', views.quiz_id, name = "Get Quiz ID")
]

