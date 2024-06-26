# Generated by Django 5.0.6 on 2024-06-02 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "category_name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Модель",
                    ),
                ),
                (
                    "category_description",
                    models.CharField(
                        blank=True,
                        help_text="Введите описание категории",
                        max_length=100,
                        null=True,
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
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
                    "product_name",
                    models.CharField(
                        help_text="Введите наименование",
                        max_length=100,
                        verbose_name="Модель",
                    ),
                ),
                (
                    "product_description",
                    models.CharField(
                        help_text="Введите описание",
                        max_length=100,
                        verbose_name="Описание",
                    ),
                ),
                (
                    "product_image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="images/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "product_purchase_price",
                    models.IntegerField(
                        help_text="Введите цену", verbose_name="Цена за покупку"
                    ),
                ),
                (
                    "date_creation",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "date_change",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего изменения"
                    ),
                ),
                (
                    "product_category",
                    models.ForeignKey(
                        help_text="Введите категорию",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ("product_name",),
            },
        ),
    ]
