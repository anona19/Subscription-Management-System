from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(request, "login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "login.html")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def customers(request):
    customers = Customer.objects.all().order_by("-created_at")

    return render(request, "customers.html", {
        "customers": customers
    })


@login_required
def products(request):
    return render(request, "products.html")


@login_required
def plans(request):
    return render(request, "plans.html")


@login_required
def quotations(request):
    return render(request, "quotations.html")


@login_required
def subscriptions(request):
    return render(request, "subscriptions.html")


@login_required
def invoices(request):
    return render(request, "invoices.html")


@login_required
def payments(request):
    return render(request, "payments.html")


@login_required
def discounts(request):
    return render(request, "discounts.html")


@login_required
def taxes(request):
    return render(request, "taxes.html")


@login_required
def reports(request):
    return render(request, "reports.html")


@login_required
def settings(request):
    return render(request, "settings.html")


def logout_view(request):
    logout(request)
    return redirect("login")