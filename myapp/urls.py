from django.urls import path
from . import views

urlpatterns = [
    path('show_home_page/', views.show_home_page, name = "home_page"),
    path('category/<int:cid>/', views.show_category, name = "show_category"),
    path('', views.home, name = "home"),
]