import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
date = datetime.datetime.now()

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nama

    class Meta:
        verbose_name_plural = '1. Kategori'

class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    isi = RichTextUploadingField(
        config_name='special',
        external_plugin_resources=[(
            'youtube',
            # 'https://minio.umkt.ac.id/simpelv2-static/ckeditor_plugins/youtube/youtube/', ini punya saya
            'http://localhost:8000/static/ckeditor_plugins/youtube/youtube/',
            'plugin.js',
            )],
            blank=True,
            null=True
    )
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    thumbnail = models.ImageField(upload_to='artikel', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.judul
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{date.year}-{date.month}-{date.day}-{self.judul}")
        super(Artikel, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "2. Article"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    article = models.ForeignKey(Artikel, on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "3. Comment"