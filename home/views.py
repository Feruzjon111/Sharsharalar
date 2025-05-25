from django.shortcuts import render, get_object_or_404
from .models import Sharshara

def bosh_sahifa(request):
    return render(request, 'home.html')

def sharshara_royxati(request):
    sharsharalar = Sharshara.objects.all()
    return render(request, 'list.html', {'sharsharalar': sharsharalar})

def sharshara_detali(request, pk):
    sharshara = get_object_or_404(Sharshara, pk=pk)
    return render(request, 'detail.html', {'sharshara': sharshara})
