# Generated by Django 4.2.5 on 2023-12-05 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacionRecu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='Cantidad',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='compra',
            name='Total',
            field=models.DecimalField(decimal_places=2, max_digits=30),
        ),
        migrations.AlterField(
            model_name='compra',
            name='Utilidad',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='compra',
            name='Valor_Costo',
            field=models.DecimalField(decimal_places=2, max_digits=30),
        ),
        migrations.AlterField(
            model_name='compra',
            name='Valor_Venta',
            field=models.DecimalField(decimal_places=2, max_digits=30),
        ),
    ]