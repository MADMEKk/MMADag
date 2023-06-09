# Generated by Django 4.1.7 on 2023-04-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sous_parcel', '0015_remove_sous_parcel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='capteur',
            name='latitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capteur',
            name='longitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sous_parcel',
            name='latitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sous_parcel',
            name='longitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
