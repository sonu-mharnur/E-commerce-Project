# Generated by Django 4.1.6 on 2023-08-21 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SizeVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='color_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.colorvariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.quantityvariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.sizevariant'),
        ),
    ]
