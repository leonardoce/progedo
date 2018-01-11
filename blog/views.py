from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from blog.models import Post, Category


def ciao(request):
    return HttpResponse("ciao")


def index(request):
    object_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, "blog/index.html", {
        'object_list': object_list,
        'category_list': category_list})


def category(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    object_list = Post.objects.filter(category=cat)
    category_list = Category.objects.all()
    return render(request, "blog/category.html", {
        'category': cat,
        'object_list': object_list,
        'category_list': category_list})