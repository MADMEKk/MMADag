# Generated by Django 4.1.7 on 2023-05-03 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='location',
            field=models.JSONField(default={1: {'lat': '1', 'long': '1'}}),
            preserve_default=False,
        ),
    ]
