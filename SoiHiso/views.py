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
