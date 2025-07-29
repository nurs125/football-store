from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    # Получаем все категории из базы данных
    categories = Category.objects.all()
    # Отдаем их в шаблон category_list.html для отображения
    return render(request, 'category_list.html', {'categories': categories})

def product_list(request, pk):
    # Получаем категорию по её ID (pk) или возвращаем 404, если не найдена
    category = get_object_or_404(Category, pk=pk)
    # Фильтруем товары, чтобы получить только те, что относятся к категории
    products = Product.objects.filter(category=category)
    # Отдаем категорию и товары в шаблон product_list.html для отображения
    return render(request, 'product_list.html', {'category': category, 'products': products})


from django.shortcuts import redirect
from django.views.decorators.http import require_POST

@require_POST
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})  # Получаем корзину из сессии или создаём новую
    cart[product_id] = cart.get(product_id, 0) + 1  # Увеличиваем количество товара на 1
    request.session['cart'] = cart  # Сохраняем корзину обратно в сессию
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Возвращаемся на предыдущую страницу


def cart_detail(request):
    cart = request.session.get('cart', {})
    products = []
    total_price = 0

    # Получаем объекты товаров и вычисляем общую цену
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        products.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity,
        })
        total_price += product.price * quantity

    return render(request, 'cart_detail.html', {
        'products': products,
        'total_price': total_price,
    })


from django.views.decorators.http import require_POST

@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart_detail')

@require_POST
def update_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    if quantity > 0:
        cart[str(product_id)] = quantity
    else:
        cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart_detail')
