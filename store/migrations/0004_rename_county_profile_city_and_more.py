# Generated by Django 5.0.6 on 2024-07-14 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_name_alter_product_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='county',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='postcode',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='town',
            new_name='zipcode',
        ),
    ]
