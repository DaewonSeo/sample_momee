from django.shortcuts import render, HttpResponseRedirect
from app.models import Product, Blog
from app.forms import BlogForm


def home(request):

    item = Product.objects.order_by('?')[0]
    blog = Blog.objects.order_by('?')[0]
    content = {

        'item': item,
        'blog': blog,


    }

    return render(request, 'app/home.html', content)


def product(request):
    items = Product.objects.all()
    content = {
        'items': items

    }

    return render(request, 'app/product.html', content)


def blog(request):

    datas = Blog.objects.all()
    content = {
        'datas': datas
    }

    return render(request, 'app/blog.html', content)


def write(request):

    user = request.user.last_name

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.author = user
            form.save()

            return HttpResponseRedirect('/blog/')

    else:
        form = BlogForm()

    content = {'form': form}

    return render(request, 'app/write.html', content)

