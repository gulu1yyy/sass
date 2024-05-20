from django.urls import path
from .views import account
urlpatterns = [
    path('register/', account.register, name='register')
]