from django.shortcuts import render
from django.views import generic
from .models import TypeFood, Name
from django.shortcuts import get_object_or_404, render
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

# def NameRestaurant(request):
#     try:
#         selected_name = Name.objects.get(name_text = request.POST['name'])
#     except (KeyError, Name.DoesNotExist):
#         return render(request, 'restaurant.html', {
#             'error_message': "Not found.",
#         })
#     context = {
#         'Name':selected_name.name_text,
#         'Type': selected_name.typefood,
#     }
#     return render(request, 'reviews.html',context)

def search (request):
    keyword = (request.POST['name'])
    namekeword = Name.objects.values_list("id", "name_text").filter(name_text__startswith = keyword)
    count = len(namekeword)
    context = {'lstname':namekeword,'count':count,'key':keyword}
    return  render(request,'search.html',context)

# def NameRes(request,name_id):
#     name = get_object_or_404(Name, pk=name_id)
#     selected_name = name.name_set.get(pk=request.POST['name'])
#     context = {
#         'Name': selected_name.name_text,
#         'Type': selected_name.typefood,
#     }
#     return render(request, 'reviews.html', context)

def NameRes(request,name_id):
    name = get_object_or_404(Name, pk=name_id)
    return render(request, 'reviews.html', {'name': name})

