from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from berita.serializers import CategorySerializer, ArticleSerializer, BiodataSerializer
from berita.models import Kategori, Artikel
from pengguna.models import Biodata

@api_view(["GET"])
def author_api_list(request):
    biodata = Biodata.objects.all()
    serializer = Biodata(biodata, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def author_api_detail(request, biodata_id):
    try:
        author = Biodata.objects.get(id=biodata_id)
        serializer = CategorySerializer(author, many=False)
        return Response(serializer.data)
    except:
        return Response("category couldn't be found", status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def category_api_list(request):
    categories = Kategori.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def category_api_detail(request, category_id):
    try:
        category = Kategori.objects.get(id=category_id)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    except:
        return Response("category couldn't be found", status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def article_api_list(request):
    articles = Artikel.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def article_api_detail(request, article_id):
    try:
        article = Artikel.objects.get(id=article_id)
        serializer = CategorySerializer(article, many=False)
        return Response(serializer.data)
    except:
        return Response("category couldn't be found", status=status.HTTP_404_NOT_FOUND)