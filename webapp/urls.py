from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views


urlpatterns = [
    path('',views.TaskList.as_view()),
    path('update/<int:pk>',views.TaskUpdateDelete.as_view()),
    path('check',views.checkLoginStatus.as_view()),
    
]