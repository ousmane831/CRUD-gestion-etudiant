from django.urls import path
from .views import *

urlpatterns = [
    
    path("",  index, name="index"),
    path("list_etudiant/",  list_etudiant, name="list_etudiant"),
    path("detail_etudiant/<int:id>/",  detail_etudiant, name="detail_etudiant"),
    path("ajouter_etudiant/",  ajouter_etudiant, name="ajouter_etudiant"),
    path("modifier_etudiant/<int:id>/",  modifier_etudiant, name="modifier_etudiant"),
    path("supprimer_etudiant/<int:id>/",  supprimer_etudiant, name="supprimer_etudiant"),
    path("contact/",contact, name="contact"),
    path("blog_cours/",blog_cours, name="blog_cours"),
]
