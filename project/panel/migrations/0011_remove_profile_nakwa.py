# Generated by Django 4.1.7 on 2023-06-07 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0010_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='nakwa',
        ),
    ]
