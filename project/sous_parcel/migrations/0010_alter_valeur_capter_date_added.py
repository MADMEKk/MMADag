# Generated by Django 4.1.7 on 2023-04-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sous_parcel', '0009_alter_valeur_capter_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valeur_capter',
            name='date_added',
            field=models.DateField(),
        ),
    ]
