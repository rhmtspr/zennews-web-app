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

@api_view(["GET", "PUT", "POST"])
def category_api_detail(request, category_id):
    try:
        category = Kategori.objects.get(id=category_id)
    except:
        return Response("category couldn't be found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass

@api_view(["POST"])
def category_api_add(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def article_api_list(request):
    token_key = "9dc5c51e926d990d6ca268a03153114fa73d4f313135fd2e7336157f8915e72e"
    token = request.headers.get("token")

    if token == None:
        return Response("message: input token", status=status.HTTP_401_UNAUTHORIZED)
    
    if token != token_key:
        return Response("message: input the right token", status=status.HTTP_401_UNAUTHORIZED)

    articles = Artikel.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    data = {
        "count": articles.count(),
        "rows": serializer.data
    }
    return Response(data)


@api_view(["GET", "PUT", "DELETE"])
def article_api_detail(request, article_id):
    try:
        article = Artikel.objects.get(id=article_id)
    except:
        return Response("category couldn't be found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ArticleSerializer(article, many=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def article_api_add(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)