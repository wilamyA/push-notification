from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import PromocoesForm
from .models import *

# Create your views here.
def index(request):
    return render(request , 'index.html')


def promocoes(request, pk):
    return render(request , 'promotions.html')


def promocoes_model_form(request):
    if request.method == "GET":
        form = PromocoesForm
        context = {'form' : form} 
        return render(request , 'promotions.html', context=context)
    else:
        form = PromocoesForm(request.POST)
        if form.is_valid():
            promocao = form.save()
            form = PromocoesForm
        context = {'form' : form} 
        print(Promocoes.objects.all())
        return render(request , 'promotions.html', context=context)
