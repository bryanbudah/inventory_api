Inventory Management API
📦 Project Overview
The Inventory Management API is a backend system built using Django and Django REST Framework (DRF). It allows authenticated users to manage inventory items for a store by performing full CRUD (Create, Read, Update, Delete) operations. The system also tracks inventory changes, enforces user-level permissions, and supports filtering, sorting, and pagination.

This project simulates a real-world inventory management scenario and is designed as a Backend Engineering Capstone Project.

🎯 Key Features
User authentication using token-based authentication
Inventory item management (CRUD)
Inventory change tracking (audit logs)
User-based permissions (users manage only their own items)
Inventory filtering and sorting
Pagination for large datasets
RESTful API design
Ready for deployment (Heroku / PythonAnywhere)
🛠️ Tech Stack
Backend Framework: Django
API Framework: Django REST Framework (DRF)
Authentication: Token Authentication
Database: SQLite (Development), PostgreSQL (Production)
Deployment: Heroku / PythonAnywhere
📂 Project Structure
inventory_api/
│
├── inventory_api/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── inventory/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   └── urls.py
│
├── manage.py
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/bryanbudah/inventory-management-api.git
cd inventory-management-api
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Development Server
python manage.py runserver
Server will be available at:

http://127.0.0.1:8000/
1️⃣ Get JWT Access Token

Method: POST

URL: http://127.0.0.1:8000/api/token/

Headers:

Content-Type: application/json

Body (raw JSON):

{ "username": "enzo", "password": "password123" }

Response example:

{ "refresh": "your_refresh_token_here", "access": "your_access_token_here" }

Copy the access token for the next requests.

2️⃣ List All Inventory Items

Method: GET

URL: http://127.0.0.1:8000/api/items/

Headers:

Authorization: Bearer <access_token>

3️⃣ Create a New Inventory Item

Method: POST

URL: http://127.0.0.1:8000/api/items/

Headers:

Authorization: Bearer <access_token> Content-Type: application/json

Body (raw JSON):

{ "name": "Laptop", "description": "High-end gaming laptop", "quantity": 5, "price": 2500.00, "category": "Electronics" }

4️⃣ Retrieve a Single Item

Method: GET

URL: http://127.0.0.1:8000/api/items//

Headers:

Authorization: Bearer <access_token>

Replace with the actual item ID.

5️⃣ Update an Item

Method: PUT or PATCH

URL: http://127.0.0.1:8000/api/items//

Headers:

Authorization: Bearer <access_token> Content-Type: application/json

Body example (PUT – full update):

{ "name": "Laptop", "description": "Updated description", "quantity": 10, "price": 2400.00, "category": "Electronics" }

Body example (PATCH – partial update):

{ "quantity": 8 }

6️⃣ Delete an Item

Method: DELETE

URL: http://127.0.0.1:8000/api/items//

Headers:

Authorization: Bearer <access_token>

7️⃣ Inventory Report

Method: GET

URL: http://127.0.0.1:8000/api/report/

Headers:

Authorization: Bearer <access_token>

🔐 Authentication
The API uses Token Authentication.

Obtain Auth Token
POST /api/auth/
Request Body:

{
  "username": "enzo",
  "password": "password123"
}
Response:

{
  "token": "your_auth_token"
}
Include the token in request headers:

Authorization: Token your_auth_token
📦 Inventory Item Model
Field	Type	Description
id	Integer	Unique identifier
owner	User	Owner of the item
name	String	Item name
description	Text	Item description
quantity	Integer	Stock quantity
price	Decimal	Item price
category	String	Item category
date_added	DateTime	When item was created
last_updated	DateTime	Last update time
🔁 Inventory Change Log
Tracks changes to inventory quantity.

Field	Description
item	Inventory item
changed_by	User
previous_quantity	Quantity before change
new_quantity	Quantity after change
timestamp	Change time
🔗 API Endpoints
Inventory Items
Method	Endpoint	Description
GET	/api/items/	View all inventory items
POST	/api/items/	Create inventory item
GET	/api/items/{id}/	Retrieve item
PUT	/api/items/{id}/	Update item
DELETE	/api/items/{id}/	Delete item
Inventory Logs
Method	Endpoint	Description
GET	/api/logs/	View inventory change history
🔍 Filtering, Searching & Sorting
Filter by Category
GET /api/items/?category=Electronics
Low Stock Filter
GET /api/items/?low_stock=5
Search
GET /api/items/?search=phone
Sorting
GET /api/items/?ordering=price
📄 Pagination
Default page size: 10 items per page

GET /api/items/?page=2
🔐 Permissions & Security
Only authenticated users can access the API
Users can only manage inventory items they own
Unauthorized access returns proper HTTP status codes
🚀 Deployment
Supported Platforms
PythonAnywhere
Production Checklist
Set DEBUG = False
Configure ALLOWED_HOSTS
Use PostgreSQL
Set environment variables
Use gunicorn as WSGI server
🧪 Testing
You can test the API using:

Postman
cURL
Django REST Framework Browsable API
🌱 Future Enhancements (Stretch Goals)
Low stock alerts via email
Supplier management
Inventory reports
Barcode scanning support
Multi-store inventory
Automated stock reordering
👨‍💻 Author
Backend Engineering Capstone Project Developed using Django & Django REST Framework

📜 License
This project is licensed for educational purposes.

inventory_api/ ├── inventory_api/ # Django project folder │ ├── init.py │ ├── settings.py │ ├── urls.py │ ├── wsgi.py │ └── asgi.py ├── inventory/ # Django app for inventory │ ├── init.py │ ├── models.py │ ├── serializers.py │ ├── views.py │ ├── urls.py │ └── admin.py ├── manage.py ├── requirements.txt └── README.md