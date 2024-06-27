from django.db import models
from django.utils import timezone


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    remarque = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Facture(models.Model):
    STATUTS_PAIEMENT = [
        ('payee', 'Payée'),
        ('en_attente', 'En attente'),
        ('retard', 'Retard'),
    ]

    numero_facture = models.CharField(max_length=50)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_emission = models.DateField()
    delai_reglement = models.IntegerField(default=0)
    date_echeance = models.DateField(blank=True, null=True)
    statut_paiement = models.CharField(max_length=20, choices=STATUTS_PAIEMENT, default='en_attente')
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    total_paiements_recus = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.numero_facture

    def save(self, *args, **kwargs):
        if self.date_emission and self.delai_reglement:
            self.date_echeance = self.date_emission + timezone.timedelta(days=self.delai_reglement)
        super(Facture, self).save(*args, **kwargs)

    def calculer_montant_du(self):
        return self.montant - self.total_paiements_recus


class ModePaiement(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Paiement(models.Model):
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()
    mode_paiement = models.ForeignKey(ModePaiement, on_delete=models.CASCADE)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    reference = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.reference} - {self.montant_paye}"

    def save(self, *args, **kwargs):
        super(Paiement, self).save(*args, **kwargs)
        self.facture.total_paiements_recus += self.montant_paye
        self.facture.save()
