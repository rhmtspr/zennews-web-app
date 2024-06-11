from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . views import home, article_detail, about, contact
from . authentication import akun_login, akun_registrasi, akun_logout
from berita.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('artikel/<slug:slug>', article_detail, name="article_detail"),
    path('dashboard/', include('berita.urls'), name="dashboard"),

    path("api/categories/list", category_api_list),
    path("api/categories/detail/<int:category_id>", category_api_detail),
    path("api/articles/list", article_api_list),
    path("api/articles/detail/<int:article_id>", article_api_detail),
    path("api/authors/list", author_api_list),
    path("api/authors/detail/<int:author_id>", author_api_detail),

    path('authentication/login', akun_login, name="akun_login"),
    path('authentication/registrasi', akun_registrasi, name="akun_registrasi"),
    path('authentication/logout', akun_logout, name="akun_logout"),
    
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path("__reload__/", include("django_browser_reload.urls"))
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)