#Djangoの path 関数と、
from django.urls import path
#blog アプリの全ての ビューをインポート
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
