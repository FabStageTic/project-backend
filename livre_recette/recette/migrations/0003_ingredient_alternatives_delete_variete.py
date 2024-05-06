# Generated by Django 5.0.4 on 2024-05-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0002_remove_ingredient_variete_variete'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='alternatives',
            field=models.ManyToManyField(blank=True, related_name='alternative_to', to='recette.ingredient'),
        ),
        migrations.DeleteModel(
            name='Variete',
        ),
    ]
