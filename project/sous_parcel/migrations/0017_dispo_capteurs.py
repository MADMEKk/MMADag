# Generated by Django 4.1.7 on 2023-05-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sous_parcel', '0016_capteur_latitude_capteur_longitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='dispo_capteurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=500)),
                ('img', models.CharField(max_length=500)),
            ],
        ),
    ]