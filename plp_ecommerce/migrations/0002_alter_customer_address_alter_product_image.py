# Generated by Django 5.0.6 on 2024-06-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plp_ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_details/'),
        ),
    ]
