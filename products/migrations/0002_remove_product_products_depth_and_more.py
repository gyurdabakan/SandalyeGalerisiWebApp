# Generated by Django 4.1 on 2022-08-08 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="products_depth",),
        migrations.RemoveField(model_name="product", name="products_high",),
        migrations.RemoveField(model_name="product", name="products_width",),
    ]
