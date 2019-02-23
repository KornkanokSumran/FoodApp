from django.shortcuts import render
from django.views import generic
from .models import TypeFood, Name,Review
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect ,HttpResponse
from django.template import loader

# Create your views here.
def Homepage(request):
    return render(request, 'homepage.html')

class Type(generic.ListView):
    template_name = 'type.html'
    context_object_name = 'latest_typefood_list'

    def get_queryset(self):
        return TypeFood.objects.all()

class DetailView(generic.DetailView):
    model = TypeFood
    template_name = 'detail.html'

def menu(request,name_id):
    name = get_object_or_404(Name, pk=name_id)
    return render(request, 'menu.html', {'name': name})

def restaurant(request):
    return render(request, 'restaurant.html')

def search (request):
    keyword = (request.POST['name'])
    namekeword = Name.objects.values_list("id", "name_text").filter(name_text__startswith = keyword)
    count = len(namekeword)
    context = {'lstname':namekeword,'count':count,'key':keyword}
    return  render(request,'search.html',context)

def NameRes(request,name_id):
    name = get_object_or_404(Name, pk=name_id)
    review = Review.objects.values_list("restaurant_id", "review_text").filter(restaurant_id = name.id)
    context = {'name': name, 'review' : review}
    return render(request, 'reviews.html', context)

def AddReview(request):
    name_restuarant = str(request.POST['namerestuarant'])
    points = int(request.POST['point'])
    review_detail = str(request.POST['review_detail'])
    name = Review(restaurant_id=name_restuarant,point=points,review_date=timezone.now(),review_text=review_detail)
    name.save()
    return render(request,'reviews.html')



