from django.shortcuts import render, redirect
from django.views import generic
from .models import TypeFood, Restaurant,Review,Menu
from django.db.models import Avg
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


# Create your views here.
def Homepage(request):
    return render(request, 'homepage.html')

def type(request):
    typefood = TypeFood.objects.all()
    return render(request, 'type.html', {'typefood':typefood})

def detail_restaurant(request,name_id):
    typefood = get_object_or_404(TypeFood, pk=name_id)
    return render(request, 'detail.html', {'typefood': typefood})

def menu(request,name_id):
    name = get_object_or_404(Restaurant, pk=name_id)
    return render(request, 'menu.html', {'name': name})

def restaurant(request):
    return render(request, 'restaurant.html')

def search (request):
    keyword = (request.POST['name'])
    namekeword = Restaurant.objects.values_list("id", "name_text").filter(name_text__startswith = keyword)
    count = len(namekeword)
    context = {'lstname':namekeword,'count':count,'key':keyword}
    return  render(request,'search.html',context)

def NameRes(request,name_id):
    name = get_object_or_404(Restaurant, pk=name_id)
    reviews = Review.objects.values_list("restaurant_id", "review_text", "point").filter(restaurant_id = name.id)
    context = {'name': name, 'reviews' : reviews}
    return render(request, 'reviews.html', context)

def AddReview(request):
    name_restuarant = str(request.POST['namerestuarant'])
    points = int(request.POST['point'])
    review_detail = str(request.POST['review_detail'])
    name = Review(restaurant_id=name_restuarant,point=points,review_date=timezone.now(),review_text=review_detail)
    name.save()
    return redirect('SoiHiso:NameRes',name_restuarant )

def popular(request):
    names = Restaurant.objects.values_list("id", "name_text")
    length_names = len(names) + 1
    avg_star = [0] * length_names
    get_avg = [0] * length_names
    for id in range(1,length_names):
        avg_star[id] =  Review.objects.values_list("restaurant_id", "point").filter(restaurant_id = id)
    context = {'names': names}
    return render(request, 'popular.html', context)