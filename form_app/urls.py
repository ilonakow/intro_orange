from django.urls import path

from form_app import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
]