from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=100,
        verbose_name="Модель",
        help_text="Введите наименование категории",
    )
    category_description = models.CharField(
        max_length=100,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE,
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    product_name = models.CharField(
        max_length=100, verbose_name="Модель", help_text="Введите наименование"
    )
    product_description = models.CharField(
        max_length=100, verbose_name="Описание", help_text="Введите описание"
    )
    product_image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE,
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию",
    )
    product_purchase_price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену"
    )
    date_creation = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    date_change = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return f"{self.product_name} {self.product_description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("product_name",)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version',
                                verbose_name='наименование')
    version_no = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    active_version = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
