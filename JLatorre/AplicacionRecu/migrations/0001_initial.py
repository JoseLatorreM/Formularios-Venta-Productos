# Generated by Django 4.2.5 on 2023-12-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=30)),
                ('Producto', models.CharField(max_length=20)),
                ('Valor_Costo', models.CharField(max_length=10)),
                ('Utilidad', models.CharField(max_length=10)),
                ('Valor_Venta', models.CharField(max_length=30)),
                ('Cantidad', models.CharField(max_length=20)),
                ('Total', models.CharField(max_length=10)),
            ],
        ),
    ]