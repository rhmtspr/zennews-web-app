from django.shortcuts import redirect, render
from berita.models import Kategori, Artikel, Comment
from berita.forms import CommentForm

def home(request):
    template_name = "pages/index.html"
    kategori = request.GET.get("kategori")

    if kategori == None:
        data_artikel = Artikel.objects.all()
        menu_aktif = "ALL"
    else:
        get_kategori = Kategori.objects.filter(nama=kategori)
        if get_kategori.count() != 0:
            data_artikel = Artikel.objects.filter(kategori=get_kategori[0])
            menu_aktif = kategori
        else:
            menu_aktif = "ALL"
            data_artikel = []

    data_kategori = Kategori.objects.all()

    context = {
        "title": "Home",
        "data_artikel": data_artikel,
        "data_kategori": data_kategori,
        "menu_aktif": menu_aktif
    }

    return render(request, template_name, context)

def article_detail(request, slug):
    template_name = "pages/article_detail.html"
    article = Artikel.objects.get(slug=slug)
    comments = Comment.objects.filter(article=article)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect("article_detail", slug=slug)
    else:
        form = CommentForm()

    context = {
        "title": article.judul,
        "article": article,
        "form": form,
        "comments": comments
    }

    return render(request, template_name, context)

def about(request):
    template_name = "pages/about.html"
    context = {
        "title": "Welcome to the about page",
    }

    return render(request, template_name, context)

def contact(request):
    template_name = "pages/contact.html"
    context = {
        "title": "Welcome to the contact page",
    }

    return render(request, template_name, context)