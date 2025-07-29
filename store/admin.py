from django.contrib import admin
from .models import Category, Product

# Регистрируем модель Category, чтобы видеть и редактировать категории в админке
admin.site.register(Category)

# Регистрируем модель Product, чтобы управлять товарами через админку
admin.site.register(Product)
