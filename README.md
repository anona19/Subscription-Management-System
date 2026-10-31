<<<<<<< HEAD
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
=======
# Brightloop Software
## Subscription Management System

**A Full-Stack Web Application for Subscription Lifecycle and Business Management**

---

## 1. Project Overview

The **Brightloop Software Subscription Management System** is a web-based application designed to simplify and centralize subscription business operations.

The platform aims to provide a unified environment for managing customers, products, subscription plans, subscriptions, invoices, payments, and administrative activities.

It is designed to help software businesses organize their subscription operations, monitor customer activity, maintain billing records, and manage their services through an intuitive administrative dashboard.

The application follows a role-based access control approach, providing separate access privileges for customers and administrators.

### Project Objectives

- Centralize subscription-related business operations.
- Simplify customer registration and account management.
- Organize software products and subscription plans.
- Support subscription lifecycle management.
- Maintain structured billing and invoice records.
- Provide administrative control over users and business data.
- Improve operational efficiency through a centralized dashboard.
- Implement secure authentication and role-based authorization.

---

## 2. Technology Stack

The project is designed using the following technologies.

### Frontend Technologies

| Technology | Purpose |
|---|---|
| HTML5 | Structure and content of web pages |
| CSS3 | Styling, layouts, and responsive design |
| Bootstrap 5.3+ | Responsive UI components and styling |
| JavaScript | Client-side interactions and dynamic functionality |
| Chart.js | Dashboard charts and graphical data representation (planned) |

### Backend Technologies

| Technology | Purpose |
|---|---|
| Python | Core backend programming language |
| Django 5+ | Backend web framework |
| Django ORM | Database operations and object-relational mapping |
| Django Authentication | User authentication and session management |
| Django Forms | Form handling and server-side validation |
| Django Admin | Administrative interface |
| Django REST Framework | REST API development (optional/planned) |

### Database Technologies

| Technology | Purpose |
|---|---|
| SQLite | Local development database |
| PostgreSQL | Recommended production database |

### Additional Technologies

| Technology | Purpose |
|---|---|
| Celery | Background task processing (planned) |
| Redis | Message broker and task coordination (planned) |
| Git | Version control |
| GitHub | Source code hosting and collaboration |
| Visual Studio Code | Development environment |

---

## 3. System Architecture

The application follows a Model-View-Template (MVT) architecture provided by Django.

### Architecture Components

**1. Model Layer**
- Defines database structures.
- Manages customer, product, subscription, and billing-related data.
- Handles database interactions through Django ORM.

**2. View Layer**
- Processes incoming HTTP requests.
- Implements application logic.
- Performs authentication and authorization checks.
- Returns appropriate responses.

**3. Template Layer**
- Displays the user interface.
- Uses HTML, CSS, Bootstrap, and JavaScript.
- Presents application data dynamically.

### Application Flow

Browser → Django URL Routing → Views → Models / Database → Templates → Browser

---

## 4. Application Modules

The project is organized into separate Django applications to maintain modularity and simplify future development.

### 4.1 Accounts Management

Responsible for user accounts and authentication.

Key functionality:
- Custom user model.
- Email-based login.
- Customer registration.
- Administrator account management.
- Role-based access control.
- Secure session management.
- Server-side permission validation.

### 4.2 Customer Management

Designed to manage customer information.

Planned functionality:
- Customer registration.
- Customer profile management.
- Customer information records.
- Customer subscription history.
- Customer account status.

### 4.3 Product Management

Designed to organize software products offered by Brightloop Software.

Planned functionality:
- Add new products.
- View product information.
- Update product details.
- Manage product availability.
- Organize products by category.

### 4.4 Subscription Plan Management

Designed to manage the subscription packages available to customers.

Planned functionality:
- Create subscription plans.
- Configure pricing.
- Define billing intervals.
- Manage plan features.
- Update and deactivate plans.

### 4.5 Subscription Management

Designed to handle the subscription lifecycle.

Planned functionality:
- Create subscriptions.
- Assign plans to customers.
- Track subscription status.
- Monitor subscription start and end dates.
- Manage renewals.
- Handle cancellations.
- Maintain subscription history.

### 4.6 Billing and Invoice Management

Designed to organize billing information and invoice records.

Planned functionality:
- Generate invoices.
- Maintain invoice records.
- Track payment status.
- Monitor outstanding amounts.
- View billing history.
- Organize invoice information.

### 4.7 Dashboard and Administration

Provides a centralized interface for administrative operations.

Planned functionality:
- Dashboard overview.
- Customer statistics.
- Product and plan summaries.
- Subscription statistics.
- Invoice summaries.
- Administrative account management.
- Navigation between management modules.

---

## 5. User Roles and Access Control

The application uses role-based access control to separate customer and administrator privileges.

### Administrator

The administrator is responsible for managing the platform.

Responsibilities:
- Manage administrative accounts.
- Access administrative functionality.
- Oversee customer and business records.
- Manage application resources.

### Customer

Customers have access to customer-facing functionality.

Responsibilities:
- Register an account.
- Log in securely.
- Access their account.
- View their permitted information.

**Security consideration:** Access restrictions are enforced on the server side rather than relying only on frontend visibility.

---

## 6. Project Directory Structure

The Django project follows a modular application structure.

```text
brightloop_subscription_management/
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── products/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── subscriptions/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── billing/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── dashboard/
│   ├── views.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

*Note: This represents the intended project organization. Individual files and application functionality may vary as development progresses.*

---

## 7. Installation and Setup

Follow these instructions to run the project locally.

### Prerequisites

Install the following before starting:

- Python 3.10 or later.
- pip (Python package manager).
- Visual Studio Code.
- Git (optional).

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd brightloop_subscription_management
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

For production, configure a secure secret key, disable debug mode, and set the permitted hosts.

### Step 6: Apply Database Migrations

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

### Step 7: Create an Administrator Account
>>>>>>> cdb47b06423e19b6b46dde1b09c4730834ea8bdc

```bash
python manage.py createsuperuser
```

<<<<<<< HEAD
Enter a username, email address, and password when prompted.

### 6. Start the Django development server
=======
Follow the instructions to configure the administrator account.

### Step 8: Start the Development Server
>>>>>>> cdb47b06423e19b6b46dde1b09c4730834ea8bdc

```bash
python manage.py runserver
```

<<<<<<< HEAD
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
=======
The application will be available at:

**Main Application:**
http://127.0.0.1:8000/

**Django Administration:**
http://127.0.0.1:8000/admin/

---

## 8. Security Features

Security is an important consideration in the application architecture.

The project incorporates or is designed to incorporate:

- Django's built-in authentication system.
- Custom email-based user authentication.
- Password hashing.
- Session-based authentication.
- CSRF protection.
- Server-side form validation.
- Role-based access control.
- Administrator-only account creation.
- Customer-only public registration.
- Server-side ownership and permission checks.
- Environment-based secret configuration.

---

## 9. Development Status

The project is being developed incrementally.

### Phase 1 – Project Foundation

- [x] Django project initialization.
- [x] Modular application structure.
- [x] Custom user model.
- [x] Email-based authentication foundation.
- [x] Customer-only public registration.
- [x] Administrator-only staff account creation.
- [x] Server-side role and ownership checks.
- [x] Initial application configuration.

### Phase 2 – Business Management

- [ ] Complete customer management.
- [ ] Product management operations.
- [ ] Subscription plan management.
- [ ] Subscription lifecycle functionality.
- [ ] Invoice management.

### Phase 3 – Dashboard and Interface

- [ ] Complete administrative dashboard.
- [ ] Functional sidebar navigation.
- [ ] Customer and administrator profile pages.
- [ ] Complete logout functionality.
- [ ] Dashboard statistics and visualizations.
- [ ] Responsive interface improvements.

### Phase 4 – Advanced Features

- [ ] Payment gateway integration.
- [ ] Automated invoice generation.
- [ ] Subscription renewal automation.
- [ ] Email notifications.
- [ ] Background task processing.
- [ ] REST API integration.
- [ ] Advanced analytics and reporting.

---

## 10. Future Enhancements

Potential improvements include:

1. Integration with payment providers such as Razorpay or Stripe.
2. Automated subscription renewal and expiry notifications.
3. PDF invoice generation.
4. Customer self-service subscription management.
5. Advanced revenue and subscription analytics.
6. Email notifications for billing events.
7. API support for third-party integrations.
8. Automated background processing using Celery and Redis.
9. PostgreSQL deployment for production environments.
10. Comprehensive automated testing.

---

## 11. Testing

The application should be tested across the following areas as development progresses:

- User registration and login.
- Authentication and authorization.
- Administrator and customer permissions.
- Form validation.
- Database operations.
- Customer and product management.
- Subscription lifecycle operations.
- Invoice generation and payment status.
- Navigation and interface functionality.
- Security and unauthorized access handling.

Django's testing framework can be used to develop automated unit and integration tests.

---

## 12. Version Control

Git is used for source code management.

Recommended commands:

```bash
git init
git add .
git commit -m "Initial project setup"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

Ensure that sensitive files such as `.env`, virtual environments, and local database files are excluded from version control when appropriate.

---

## 13. Deployment Considerations

For production deployment, the following improvements are recommended:

- PostgreSQL database configuration.
- Production-grade WSGI or ASGI server.
- HTTPS configuration.
- Secure environment variables.
- Static file collection and serving.
- `DEBUG=False`.
- Proper `ALLOWED_HOSTS` configuration.
- Database backup strategy.
- Application logging and monitoring.
- Automated testing before deployment.

---

## 14. Project Information

| Attribute | Details |
|---|---|
| Project Name | Brightloop Software |
| Application | Subscription Management System |
| Project Type | Full-Stack Web Application |
| Backend | Python, Django 5+ |
| Frontend | HTML5, CSS3, Bootstrap, JavaScript |
| Database | SQLite / PostgreSQL |
| Architecture | Django MVT |
| Development Environment | Visual Studio Code |
| Version Control | Git and GitHub |

---

## 15. License

This project is developed for educational and software development purposes.

A formal open-source license can be added if the project is intended for public distribution.

---

**Brightloop Software – Subscription Management System**

*Centralizing subscription operations through a structured, scalable, and user-friendly web application.*
>>>>>>> cdb47b06423e19b6b46dde1b09c4730834ea8bdc
