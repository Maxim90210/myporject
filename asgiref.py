from django.urls import path
from asgiref.sync import sync_to_async
from . import views

urlpatterns = [
    path('', sync_to_async(views.index), name='index'),
    path('<str:short_id>/', sync_to_async(views.redirect_url), name='redirect_url'),
]
