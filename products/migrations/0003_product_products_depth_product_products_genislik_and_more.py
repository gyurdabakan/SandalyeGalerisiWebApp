# Generated by Django 4.1 on 2022-08-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_remove_product_products_depth_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="products_depth",
            field=models.PositiveIntegerField(default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="products_genislik",
            field=models.PositiveIntegerField(default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="products_high",
            field=models.PositiveIntegerField(default=15),
            preserve_default=False,
        ),
    ]
