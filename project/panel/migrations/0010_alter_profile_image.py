# Generated by Django 4.1.7 on 2023-06-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
