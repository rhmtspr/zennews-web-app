from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from berita.models import Kategori, Artikel
from berita.forms import ArtikelForm
from django.contrib.auth.models import User

# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    template_name = "dashboard/index.html"
    context = {
        "title": "halaman dashboard"
    }

    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/authentication/logout')
def kategori(request):
    template_name = "dashboard/snippets/kategori.html"
    kategori_item = Kategori.objects.all()
    context = {
        "title": "halaman kategori",
        "kategori": kategori_item
    }

    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/authentication/logout')
def kategori_add(request):
    template_name = "dashboard/snippets/kategori_add.html"
    if request.method == "POST":
        nama_kategori = request.POST.get("nama_kategori")
        Kategori.objects.create(
                nama = nama_kategori
            )
        return redirect(kategori)
            

    context = {
        "title": "tambah Kategori",
    }

    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/authentication/logout')
def kategori_update(request, id_kategori):
    template_name = "dashboard/snippets/kategori_update.html"
    try:
        kategori_input = Kategori.objects.get(id=id_kategori)
    except:
        pass
    if request.method == "POST":
        nama_kategori = request.POST.get("nama_kategori")
        kategori_input.nama = nama_kategori
        kategori_input.save()
        return redirect(kategori)

    context = {
        "title": "update kategori",
        "kategori": kategori_input
    }

    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/authentication/logout')
def kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
    except:
        pass
    return redirect(kategori)

@login_required
def artikel(request):
    template_name = 'dashboard/snippets/artikel.html'
    if request.user.groups.filter(name='Operator'):
        artikel = Artikel.objects.all()
    else:
        artikel = Artikel.objects.filter(author=request.user)
    context = {
        'title': 'Artikel',
        'artikel': artikel
    }
    return render(request, template_name, context)

@login_required
def artikel_add(request):
    template_name = "dashboard/snippets/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel)
        else:
            print(forms.error_class)
    forms = ArtikelForm
    context = {
        "title": "tambah artikel",
        "forms": forms
    }

    return render(request, template_name, context)

@login_required
def artikel_detail(request, id_artikel):
    template_name = "dashboard/snippets/artikel_detail.html"
    artikel = Artikel.objects.get(id=id_artikel)
    context = {
        "title": artikel.judul,
        "artikel": artikel
    }

    return render(request, template_name, context)

@login_required
def artikel_update(request, id_artikel):
    template_name = "dashboard/snippets/artikel_forms.html"
    artikel_input = Artikel.objects.get(id=id_artikel)
    if request.user.groups.filter(name='Operator'):
        pass
    else:
        if artikel_input.author != request.user:
            return redirect('/')

    if request.method == "POST":
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel)
    forms = ArtikelForm(instance=artikel_input)
    context = {
        "title": "tambah artikel",
        "forms": forms
    }

    return render(request, template_name, context)

@login_required
def artikel_delete(request, id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
        if request.user.groups.filter(name='Operator'):
            pass
        else:
            if artikel.author != request.user:
                return redirect("/")
            artikel.detele()
    except:
        pass
    return redirect(artikel)

@login_required
@user_passes_test(is_operator, login_url='/authentication/logout')
def authors(request):
    authors = User.objects.filter(groups__isnull=True)

    context = {
        "authors": authors
    }

    return render(request, "dashboard/snippets/authors.html", context)

@login_required
@user_passes_test(is_operator, login_url='/authentication/logout')
def delete_author(request, author_id):
    author = User.objects.get(id=author_id)
    author.delete()

    return redirect(author)