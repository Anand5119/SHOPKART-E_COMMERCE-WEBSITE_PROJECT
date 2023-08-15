from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from shop.form import customUserForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    hot = products.objects.filter(hotProducts=True)
    return render(request, 'shop/index.html', {"hot": hot})


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            name = request.POST.get("username")
            Password = request.POST.get("password")
            user = authenticate(request, username=name, password=Password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(
                    request, "Invalid Username or Password")
                return redirect('/login')
        return render(request, 'shop/login.html')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(
            request, "Logged out Successfully")
    return redirect("/")


def register(request):
    form = customUserForm()
    if request.method == "POST":
        form = customUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registration success!!! You can Login and Enjoy now")
            return redirect('/login')
    return render(request, 'shop/register.html', {"form": form})


def Collections(request):
    Catagory = catagory.objects.filter(status=False)
    return render(request, 'shop/collection.html', {'Catagory': Catagory})


def colectionItem(request, name):
    if (catagory.objects.filter(status=False, name=name)):
        Product = products.objects.filter(category__name=name)
        return render(request, 'shop/products/index.html', {'product': Product, "category_name": name})
    else:
        messages.error(request, "no Such catagory found")
        return redirect(Collections)


def productDetails(request, cname, pname):
    if (catagory.objects.filter(status=0, name=cname)):
        if (products.objects.filter(status=0, name=pname)):
            productDetail = products.objects.filter(
                status=0, name=pname).first()
            return render(request, 'shop/products/product_details.html', {'productDetail': productDetail, "category_name": cname, "product_name": pname})
        else:
            messages.error(request, "No Such product found")
            return redirect(colectionItem, cname)
    else:
        messages.error(request, "No Such catagory found")
        return redirect(Collections)
