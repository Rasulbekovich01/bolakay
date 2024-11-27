from django.urls import path
from .views import index, add, detail

urlpatterns=[
    path('', index),
    path('add/', add),
    path('detail/<int:pk>/', detail),
]


