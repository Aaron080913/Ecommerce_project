# Generated by Django 5.0.6 on 2024-07-15 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_profile_old_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='city',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='state',
            new_name='postcode',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='zipcode',
            new_name='town',
        ),
    ]
