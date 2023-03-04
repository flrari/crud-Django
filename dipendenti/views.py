from .models import Dipendenti
from .forms import AddDipendenti
from .serializers import DipendentiSerializers
from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
def getAll(request):
    dipendenti = Dipendenti.objects.all()
    return render(request, "index.html", {'dipendenti': dipendenti})
       
def addDipendenti(request):
    add = AddDipendenti()
    if request.method == 'POST':
        add = AddDipendenti(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, "addDipendenti.html", {'add': add})

def aggiornaDipendente(request, id):
    id = int(id)
    try:
        dipendenti = Dipendenti.objects.get(id = id)
    except Dipendenti.DoesNotExist:
        return redirect('index')
    uploadForm = AddDipendenti(request.POST or None, instance = dipendenti)
    if uploadForm.is_valid():
       uploadForm.save()
       return redirect('index')
    return render(request, 'aggiornaDipendente.html', {'uploadForm': uploadForm})

def delete(request, id):
    id = int(id)
    try:
        dipendenti = Dipendenti.objects.get(id = id)
    except Dipendenti.DoesNotExist:
        return redirect('index')
    dipendenti.delete()
    return redirect('index')