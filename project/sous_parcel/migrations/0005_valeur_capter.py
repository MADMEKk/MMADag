# Generated by Django 4.1.7 on 2023-04-16 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sous_parcel', '0004_capteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='valeur_capter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FloatField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('capteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value', to='sous_parcel.capteur')),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
    ]
