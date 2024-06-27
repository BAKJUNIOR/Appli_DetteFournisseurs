from django import forms
from Model.models import Fournisseur, Categorie


class FournisseurForm(forms.ModelForm):
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all())

    class Meta:
        model = Fournisseur
        fields = ['nom', 'adresse', 'email', 'telephone', 'categorie', 'remarque', 'photo']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Fournisseur.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email existe déjà.")
        return email

    def clean_nom(self):
        nom = self.cleaned_data.get('nom')
        if Fournisseur.objects.filter(nom=nom).exists():
            raise forms.ValidationError("Un fournisseur avec ce nom existe déjà.")
        return nom
