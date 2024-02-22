from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>',
         views.category_dishes, name='category_dishes'),
    path('bestsellers/', views.bestsellers, name='bestsellers'),
    path('news/', views.news, name='news')
]
