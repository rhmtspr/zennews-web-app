from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def akun_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    template_name = "pages/login.html"
    message = ""
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            message = 'Failed to login'
    context = {
        'message': message,
    }

    return render(request, template_name, context)
    
def akun_registrasi(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    message = ""
    template_name = "pages/registrasi.html"

    if request.method == "POST":
        username = request.POST.get("username")
        nama_depan = request.POST.get("nama_depan")
        nama_belakang = request.POST.get("nama_belakang")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            check_user = User.objects.filter(username=username)

            if check_user.count() == 0:
                new_user = User.objects.create(
                    username=username,
                    first_name=nama_depan,
                    last_name=nama_belakang,
                    email=email,
                    is_active=True
                )

                new_user.set_password(password1)
                new_user.save()
                return redirect("/")
            else:
                message = "username has already been taken"
        else:
            message = "password isn't matched"

    context = {
            "message": message
        }
    
    return render(request, template_name, context)


def akun_logout(request):
    logout(request)
    return redirect("/")