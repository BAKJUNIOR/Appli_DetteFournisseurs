from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FournisseurForm
from Model.models import Categorie, Fournisseur  # Assurez-vous d'importer le modèle Categorie correctement


def Ajouter_fournisseur(request):
    categories = Categorie.objects.all()  # Récupère toutes les catégories

    if request.method == 'POST':
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fournisseur enregistré avec succès.')
            return redirect('Gestn_fournisseurs:Ajouter_fournisseur')
        else:
            messages.error(request, 'Erreur lors de l\'enregistrement du fournisseur. Veuillez corriger les erreurs.')
    else:
        form = FournisseurForm()

    return render(request, 'Ajouter_fournisseur.html', {'form': form, 'categories': categories})


def Liste_fournisseurs(request):
    fournisseurs_list = Fournisseur.objects.all()
    paginator = Paginator(fournisseurs_list, 5)  # 10 éléments par page

    page_number = request.GET.get('page')
    try:
        fournisseurs = paginator.page(page_number)
    except PageNotAnInteger:
        fournisseurs = paginator.page(1)
    except EmptyPage:
        fournisseurs = paginator.page(paginator.num_pages)

    return render(request, 'Liste_fournisseurs.html', {'fournisseurs': fournisseurs})


