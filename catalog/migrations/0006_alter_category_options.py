# Generated by Django 5.0.6 on 2024-09-07 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_options_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "permissions": [("can_edit_category_name", "Can edit category name")],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
    ]
