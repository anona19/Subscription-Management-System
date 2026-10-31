# Subscription Management System

A web-based Subscription Management System built using Django. The application helps manage customers, products, subscription plans, subscriptions, invoices, payments, discounts, taxes, and reports.

## Features

- User authentication (Login and Logout)
- Dashboard
- Customer management
- Product management
- Subscription plan management
- Quotations
- Subscription management
- Invoice management
- Payment management
- Discount management
- Tax management
- Reports
- Settings
- Django Admin Panel
- SQLite Database

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap Icons
- SQLite
- JavaScript

## Project Structure

```text
Subscription-Management-System/
│
├── brightloop/          # Django project configuration
├── core/                # Main Django application
│   ├── models.py        # Database models
│   ├── views.py         # Application views
│   ├── urls.py          # Application URLs
│   └── admin.py         # Django admin configuration
│
├── templates/           # HTML templates
│   ├── login.html
│   ├── dashboard.html
│   ├── customers.html
│   ├── products.html
│   ├── plans.html
│   ├── subscriptions.html
│   ├── invoices.html
│   ├── payments.html
│   └── ...
│
├── static/              # Static files
│   └── css/
│       └── style.css
│
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
└── README.md
```

## Installation

### 1. Clone or download the project

Open the project folder in Visual Studio Code.

### 2. Create and activate a virtual environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

Enter a username, email address, and password when prompted.

### 6. Start the Django development server

```bash
python manage.py runserver
```

The application will run at:

```text
http://127.0.0.1:8000/
```

## Django Admin Panel

The Django Admin Panel is available at:

```text
http://127.0.0.1:8000/admin/
```

From the admin panel, administrators can manage:

- Customers
- Products
- Plans
- Subscriptions
- Invoices
- Payments
- Discounts
- Taxes

## Important

Do not open the HTML files directly using Live Server.

Use Django's development server instead:

```bash
python manage.py runserver
```

Then access the application through:

```text
http://127.0.0.1:8000/
```

## Current Development Status

The Django backend, database, authentication system, dashboard, and static CSS integration are configured.

The next development stage is connecting the frontend forms and pages directly to the Django database so users can add, view, edit, and delete records from the application interface.