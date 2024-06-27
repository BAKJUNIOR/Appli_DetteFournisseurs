from django.urls import path

from Gestn_fournisseurs.views import Liste_fournisseurs, Ajouter_fournisseur

app_name = 'Gestn_fournisseurs'


urlpatterns = [
    path('Ajouter_fournisseur/', Ajouter_fournisseur, name='Ajouter_fournisseur'),
    path('Liste_fournisseurs/', Liste_fournisseurs, name='Liste_fournisseurs'),

]
