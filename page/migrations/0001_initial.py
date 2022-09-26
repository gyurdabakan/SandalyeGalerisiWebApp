# Generated by Django 4.1 on 2022-08-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Carousel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "cover_image",
                    models.ImageField(blank=True, null=True, upload_to="carousel"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Taslak"),
                            ("published", "Yayinlandi"),
                            ("deleted", "Silindi"),
                        ],
                        default="draft",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(default="", max_length=200)),
                ("content", models.TextField()),
                (
                    "cover_image",
                    models.ImageField(blank=True, null=True, upload_to="page"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Taslak"),
                            ("published", "Yayinlandi"),
                            ("deleted", "Silindi"),
                        ],
                        default="draft",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]