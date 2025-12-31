Task Manager Web App

A scalable web application with authentication and a dashboard.  
Built with React.js (frontend), FastAPI (backend), and MySQL (database).

---

## Features

- User authentication (signup/login/logout) with JWT
- Password hashing using bcrypt
- Dashboard with CRUD-enabled tasks
- Search and filter tasks
- Protected routes (dashboard accessible only to logged-in users)
- Responsive UI using TailwindCSS / Material UI / Bootstrap
- MySQL database integration

---

## Folder Structure

task-manager-project/
├── frontend/
│ ├── src/
│ │ ├── main.jsx
│ │ ├── App.jsx
│ │ ├── api.js
│ │ ├── components/ (Tasks.jsx, Header.jsx)
│ │ └── assets/ (CSS/images)
│ ├── package.json
│ └── vite.config.js
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── routes/ (auth.py, tasks.py)
│ └── requirements.txt
└── README.md

yaml
Copy code

---

Setup Instructions

Backend (FastAPI)

1. Navigate to backend folder:

```bash
cd backend
Create virtual environment:

bash
Copy code
python -m venv venv
Activate virtual environment:

Windows:

bash
Copy code
venv\Scripts\activate
Mac/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the server:

bash
Copy code
uvicorn main:app --reload
Backend runs at http://127.0.0.1:8000

Frontend (React)
Navigate to frontend folder:

bash
Copy code
cd frontend
Install dependencies:

bash
Copy code
npm install
Run the app:

bash
Copy code
npm run dev
Frontend runs at http://localhost:5173

API Endpoints
POST /signup → Register a new user

POST /login → Login and get JWT

GET /tasks → List all tasks (protected)

POST /tasks → Create a task (protected)

PUT /tasks/{id} → Update a task (protected)

DELETE /tasks/{id} → Delete a task (protected)

GET /profile → Get user profile (protected)

PUT /profile → Update user profile (protected)

All protected routes require JWT token in headers.

Scalability Notes
Modular backend structure (routes/, models/)

Environment variables for JWT secret and database credentials

Easy to add more entities (notes, posts, etc.)

Frontend components are reusable and modular

Ready for deployment on AWS / Heroku / Vercel

Postman Collection
Include your Postman collection: TaskManager.postman_collection.json

Author
SARANYA DHEVE B

Logs & Proof of Working

This section contains execution proof screenshots demonstrating that the frontend, backend, and database are properly connected and functioning.

Backend Server Running (FastAPI)

Backend started successfully using Uvicorn.

APIs tested using browser/Postman.

SCREENSHOTS:

logs/backend.png 
logs/backend 2.png


MySQL Database Connection Proof

MySQL server connected successfully.

Task data created from frontend is stored in MySQL database.

SCREENSHOTS:

logs/database.png
logs/database 2.png


Authentication & CRUD Flow

User registration and login tested.

JWT token generated and used for protected routes.

Tasks can be created, updated, deleted, and fetched.

SCREENSHOTS:

logs/frontend.png
logs/frontend 2.png

Project Status

✔ Frontend–Backend integration completed
✔ MySQL database connected and verified
✔ Authentication implemented using JWT
✔ CRUD operations working correctly
✔ Project ready for evaluation

Notes for Evaluators

All screenshots are available inside the logs/ folder.

The project follows modular structure for scalability.

Security best practices like password hashing and token validation are implemented.


