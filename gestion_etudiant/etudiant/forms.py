from django import forms
from django.forms import ModelForm
from .models import Etudiant

class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'age', 'metiers', 'email', 'est_inscrit']
        widgets = {
            'nom': forms.TextInput(attrs={
                'placeholder': 'Entrez le nom de l\'étudiant',
                'class': 'form-control'
            }),
            'prenom': forms.TextInput(attrs={
                'placeholder': 'Entrez le prénom',
                'class': 'form-control'
            }),
            'age': forms.NumberInput(attrs={ 
                'placeholder': 'Entrez son âge',
                'class': 'form-control'
            }),
            'metiers': forms.TextInput(attrs={
                'placeholder': 'Choisissez le métier',
                'class': 'form-control'
            }),
            
            'email': forms.TextInput(attrs={
                'placeholder': 'Choisissez le mail',
                'class': 'form-control'
            }),
            'est_inscrit': forms.CheckboxInput(attrs={ 
                'class': 'form-check-input'
            }),
        }
