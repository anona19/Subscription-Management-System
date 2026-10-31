from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("customers/", views.customers, name="customers"),
    path("products/", views.products, name="products"),
    path("plans/", views.plans, name="plans"),
    path("quotations/", views.quotations, name="quotations"),
    path("subscriptions/", views.subscriptions, name="subscriptions"),
    path("invoices/", views.invoices, name="invoices"),
    path("payments/", views.payments, name="payments"),
    path("discounts/", views.discounts, name="discounts"),
    path("taxes/", views.taxes, name="taxes"),
    path("reports/", views.reports, name="reports"),
    path("settings/", views.settings, name="settings"),

    path("logout/", views.logout_view, name="logout"),
]