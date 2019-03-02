from django.urls import path
from . import views

app_name = 'SoiHiso'
urlpatterns = [
    path('',views.Homepage, name='homepage'),
    path('SoiHiso/<int:name_id>/', views.detail_restaurant, name='detail'),
    path('typefood/', views.type, name='typefood'),
    path('<int:name_id>/menu/', views.menu, name='menu'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('search/', views.search, name='search'),
    path('popular/', views.popular, name='popular'),
    path('<int:name_id>/NameRes/', views.NameRes, name='NameRes'),
    path('reviews/', views.AddReview, name='review')



]

