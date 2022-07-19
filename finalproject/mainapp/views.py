from django.shortcuts import render
from .models import Post


def get_post_by_category(category_name):
    post = Post.objects.filter(category__name=category_name).select_related('category').order_by('-data')
    return post


def index_page(request):
    context = {
        'posts': Post.objects.all().order_by('-data')
    }
    return render(request, 'index.html', context)


def post_page(request, post_id):
    context = {
        'post': Post.objects.get(id=post_id)
    }
    return render(request, 'post.html', context)


def design_page(request):
    context = {
        'posts': get_post_by_category('Дизайн')
    }
    return render(request, 'design.html', context)


def web_dev_page(request):
    context = {
        'posts': get_post_by_category('Веб-разработка')
    }
    return render(request, 'web_dev.html', context)


def mobile_dev_page(request):
    context = {
        'posts': get_post_by_category('Мобильная разработка')
    }
    return render(request, 'mobile_dev.html', context)


def marketing_page(request):
    context = {
        'posts': get_post_by_category('Маркетинг')
    }
    return render(request, 'marketing.html', context)


def registration_page(request):
    return render(request, 'registration.html')


def signin_page(request):
    return render(request, 'base.html')


def help_page(request):
    return render(request, 'help.html')
