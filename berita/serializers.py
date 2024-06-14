from rest_framework import serializers
from django.contrib.auth.models import User
from berita.models import Kategori, Artikel
from pengguna.models import Biodata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

class BiodataSerializer(serializers.ModelSerializer):
    user = UserSerializer
    
    class Meta:
        model = Biodata
        fields = ["user", "alamat", "telpon", "foto"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ["id", "nama"]

class ArticleSerializer(serializers.ModelSerializer):
    kategori = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    category_detail = CategorySerializer(source="kategori", read_only=True)
    author_detail = UserSerializer(source="author", read_only=True)

    class Meta:
        model = Artikel
        fields = ["id", "judul", "isi", "kategori", "category_detail", "author", "author_detail", "thumbnail", "created_at", "slug"]
        read_only_fields = ["category_detail", "author_detail"]