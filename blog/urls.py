#Djangoの path 関数と、
from django.urls import path
#blog アプリの全ての ビューをインポート
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    #編集画面のurlパターンを定義 必ず、名前とビュー出の関数名同じにする！！
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
