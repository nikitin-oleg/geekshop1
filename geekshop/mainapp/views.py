from django.shortcuts import render
import datetime
from .models import ProductCategory, Product, Contacts


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)




def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = Contacts.objects.all()
    content = {
        'title': title,
        'visit_date': visit_date,
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', content)
