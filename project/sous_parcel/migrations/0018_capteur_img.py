# Generated by Django 4.1.7 on 2023-05-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sous_parcel', '0017_dispo_capteurs'),
    ]

    operations = [
        migrations.AddField(
            model_name='capteur',
            name='img',
            field=models.CharField(default='icon-sun-cloud.png', max_length=500),
            preserve_default=False,
        ),
    ]
