# Generated by Django 4.2.11 on 2024-06-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos_fournisseurs/'),
        ),
    ]
