from django.contrib import admin
from .models import (
    Customer,
    Product,
    Plan,
    Subscription,
    Invoice,
    Payment,
    Discount,
    Tax
)


# =========================
# CUSTOMER
# =========================
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company', 'created_at')
    search_fields = ('name', 'email', 'phone')


# =========================
# PRODUCT
# =========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)


# =========================
# PLAN
# =========================
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'billing_cycle')
    search_fields = ('name',)


# =========================
# SUBSCRIPTION
# =========================
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'plan',
        'start_date',
        'next_billing_date',
        'status'
    )

    list_filter = ('status', 'plan')
    search_fields = ('customer__name', 'plan__name')


# =========================
# INVOICE
# =========================
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_number',
        'customer',
        'amount',
        'issue_date',
        'due_date',
        'status'
    )

    list_filter = ('status',)
    search_fields = ('invoice_number', 'customer__name')


# =========================
# PAYMENT
# =========================
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'invoice',
        'amount',
        'payment_date',
        'payment_method'
    )

    search_fields = ('invoice__invoice_number',)


# =========================
# DISCOUNT
# =========================
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'active')
    search_fields = ('name',)


# =========================
# TAX
# =========================
@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    search_fields = ('name',)