# Generated by Django 5.0.7 on 2024-07-23 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Provider",
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
                ("name", models.CharField(max_length=150, verbose_name="Название")),
                ("email", models.EmailField(max_length=254, verbose_name="email")),
                ("country", models.CharField(max_length=150, verbose_name="Страна")),
                ("city", models.CharField(max_length=150, verbose_name="Город")),
                ("street", models.CharField(max_length=150, verbose_name="Улица")),
                (
                    "house_number",
                    models.CharField(max_length=10, verbose_name="Номер дома"),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="clients",
                        to="providers.provider",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Поставщик",
                "verbose_name_plural": "Поставщики",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название продукта"),
                ),
                (
                    "model",
                    models.CharField(max_length=150, verbose_name="Модель продукта"),
                ),
                ("release_date", models.DateField(verbose_name="Дата релиза")),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="providers.provider",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
