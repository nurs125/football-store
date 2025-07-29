from django.db import models

class Category(models.Model):
    # Модель Категории хранит название категории товаров
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        # Метод возвращает читаемое имя категории для админки и других интерфейсов
        return self.name

class Product(models.Model):
    # Модель Товара хранит информацию о конкретном товаре
    category = models.ForeignKey(
        Category,  # Связываем товар с моделью Category
        on_delete=models.CASCADE,  # При удалении категории удаляются все связанные товары
        related_name='products',  # Позволяет из категории получить список товаров через category.products.all()
        verbose_name="Категория"
    )
    name = models.CharField(max_length=150, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание товара")

    def __str__(self):
        # Возвращаем имя товара
        return self.name
