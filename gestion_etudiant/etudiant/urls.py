from django.urls import path
from .views import *

urlpatterns = [
    
    path("",  list_etudiant, name="list_etudiant"),
    path("detail_etudiant/<int:id>/",  detail_etudiant, name="detail_etudiant"),
    path("ajouter_etudiant",  ajouter_etudiant, name="ajouter_etudiant"),
    path("modifier_etudiant/<int:id>/",  modifier_etudiant, name="modifier_etudiant"),
    path("supprimer_etudiant/<int:id>/",  supprimer_etudiant, name="supprimer_etudiant"),
]
