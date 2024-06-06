from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . views import home, detail_artikel, about, contact
from . authentication import akun_login, akun_registrasi, akun_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('artikel/<slug:slug>', detail_artikel, name="detail_artikel"),
    path('dashboard/', include('berita.urls'), name="dashboard"),
    path('authentication/login', akun_login, name="akun_login"),
    path('authentication/registrasi', akun_registrasi, name="akun_registrasi"),
    path('authentication/logout', akun_logout, name="akun_logout"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("__reload__/", include("django_browser_reload.urls"))
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)