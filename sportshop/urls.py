from django.contrib import admin
from django.urls import path
from store import views  # Импортируем наши views из приложения store

urlpatterns = [
    path('admin/', admin.site.urls),

    # Главная страница — список категорий
    path('', views.category_list, name='category_list'),

    # Динамический URL для отображения товаров конкретной категории по её ID (pk)
    path('category/<int:pk>/', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


    path('cart/', views.cart_detail, name='cart_detail'),


    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),

]


