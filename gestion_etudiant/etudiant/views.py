from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms import *


# Create your views here.

def index(request):  
    return render(request, 'gestion_etudiant/index.html')


def list_etudiant(request):
    etudiants = Etudiant.objects.all().order_by('-created_at')
    return render(request, 'gestion_etudiant/list_etudiant.html', {'etudiants': etudiants})

def detail_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    return render(request, 'gestion_etudiant/detail_etudiant.html', {'etudiant': etudiant})


def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_etudiant')
    else:
        form = EtudiantForm()
    return render(request, 'gestion_etudiant/ajouter_etudiant.html', {'form': form})



def modifier_etudiant(request, id):
    etudiant =Etudiant.objects.get(id=id)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('list_etudiant')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'gestion_etudiant/modifier_etudiant.html', {'form': form})

def supprimer_etudiant(request, id):
    etudiant = Etudiant.objects.get(id= id)
    etudiant.delete()
    return redirect('list_etudiant')

def contact(request):
    return render(request , 'gestion_etudiant/contact.html')

def blog_cours(request):
    return render(request , 'gestion_etudiant/blog_cours.html')