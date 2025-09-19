# 🛍️E-Commerce Backend Project

A RESTful backend for an e-commerce platform, built with **Django** and **Django REST Framework (DRF)**. This backend supports products, reviews, orders, payments, and user management with JWT authentication.

---

## 🛠 Tools & Technologies

- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (default, can switch to PostgreSQL)  
- **Authentication:** JWT (SimpleJWT)  
- **API Documentation:** drf-spectacular (Swagger/OpenAPI)  
- **Filtering & Pagination:** Django Filter, DRF Pagination  
- **Python Version:** 3.12  
- **Frontend:** Can be integrated separately (not included)  

---

## Getting Started

### 1. Clone the repository

git clone <repo-url>
cd ecommerce_backend_project
2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Install dependencies


pip install -r requirements.txt
4. Run migrations

python manage.py migrate
5. Create a superuser 

python manage.py createsuperuser
6. Start the server


python manage.py runserver
Server will run at:
http://127.0.0.1:8000/

🔗 API Endpoints
Authentication
Endpoint	Method	Description
/api/auth/register/	POST	Register a new user
/api/auth/login/	POST	Obtain JWT access & refresh tokens

## Users
Endpoint	Method	Description
/api/users/	GET	List all users

## Products
Endpoint	Method	Description
/api/products/	GET	List all products
/api/products/<id>/	GET	Product details

## Orders
Endpoint	Method	Description
/api/orders/	GET/POST	List/Create orders
/api/orders/<id>/	GET/PUT/DELETE	Order details
/api/orders/items/	GET/POST	List/Create order items
/api/orders/items/<id>/	GET/PUT/DELETE	Order item details
/api/orders/addresses/	GET/POST	List/Create addresses
/api/orders/addresses/<id>/	GET/PUT/DELETE	Address details

## Payments
Endpoint	Method	Description
/api/payments/	GET/POST	List/Create payments
/api/payments/<id>/	GET/PUT/DELETE	Payment details

## Reviews
Endpoint	Method	Description
/api/reviews/	GET	List all reviews

📄 API Documentation
Swagger UI available at:

http://127.0.0.1:8000/api/swagger/
Redoc available at:

http://127.0.0.1:8000/api/redoc/

## Features
User registration & authentication (JWT)

CRUD operations for products, orders, addresses, payments, and reviews

Pagination, filtering, and sorting for products & orders

Swagger/OpenAPI documentation

Background tasks (Celery) integrated