# Generated by Django 4.0.1 on 2022-01-21 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nomenclature', '0002_product_remains'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
