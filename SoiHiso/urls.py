from django.urls import path
from . import views

app_name = 'SoiHiso'
urlpatterns = [
    path('',views.Homepage, name='homepage'),
    path('SoiHiso/<int:pk>/',  views.DetailView.as_view(), name='detail'),
    path('typefood/', views.Type.as_view(), name='typefood'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('<int:name_id>/menu/', views.menu, name='menu'),
    path('search/', views.search, name='search'),
    path('<int:name_id>/NameRes/', views.NameRes, name='NameRes'),
    path('reviews/', views.AddReview, name='review')



]

