from django.shortcuts import render
from django.views import generic
from .models import TypeFood, Name
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

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

def restaurant(request):
    return render(request, 'restaurant.html')

def NameRestaurant(request):
    try:
        selected_name = Name.objects.get(name_text = request.POST['name'])
    except (KeyError, Name.DoesNotExist):
        return render(request, 'restaurant.html', {
            'error_message': "Not found.",
        })
    context = {
        'Name':selected_name.name_text,
        'Type': selected_name.typefood,
    }
    return render(request, 'reviews.html',context)
