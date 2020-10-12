from django.shortcuts import render, redirect
from .models import Products, Category, Evaluations, ImageUsers, TextSite, ImageProducts
from .forms import EvaluationsForm


def catalog(request):
    category = Category.objects.all()
    title = 'Каталог'
    return render(request, 'main/catalog.html', {'category': category, 'title': title })


def get_category(request, category_id):
    product = Products.objects.filter(category_id=category_id, is_published=True)
    category = Category.objects.get(pk=category_id)
    return render(request, 'main/category.html', {'product': product, 'category': category})


def get_product(request, product_id):
    product = Products.objects.get(pk=product_id)
    images = ImageProducts.objects.filter(contact=product_id)
    return render(request, 'main/product.html', {'product': product, 'images': images})


def add(request):
    title = 'Оценка'
    if request.method == 'POST':
        form = EvaluationsForm(request.POST)
        files = request.FILES.getlist('photos')

        if form.is_valid():
            id = form.save().pk
            contact = Evaluations.objects.get(pk=id)
            for f in files:
                fl = ImageUsers(contact=contact, photo=f)
                fl.save()
            return redirect('add')
    else:
        form = EvaluationsForm()
    return render(request, 'main/add.html', {'form': form, 'title': title})


def index(request):
    title = 'Главная'
    ts = TextSite.objects.all()
    return render(request, 'main/index.html', {'title': title, 'ts': ts})