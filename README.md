# FastAPI JWT Authentication System with MongoDB

This project is a user authentication and authorization system built using FastAPI, JWT, and MongoDB. It includes secure login, logout, and user CRUD endpoints, with support for role-based access control (RBAC) and JWT-based authentication. 

## Project Features

### Must-Have Requirements
1. **Login and Logout Endpoints**: Supports JWT token generation upon login and token invalidation for logout.
2. **Secure User CRUD Endpoints**: CRUD operations on users, secured by JWT authentication and RBAC for sensitive endpoints.
3. **Readable, Modular Code**: The code is structured to promote readability and maintainability.
4. **No ODM Library**: Direct database operations are performed using `pymongo` without ODM libraries like Beanie or ODMantic.
5. **Script for Initial User Creation**: A Python script creates initial users with a hashed password in the database.

### Good-to-Have Features
1. **Logging Support**: Configurable logging for tracking API requests and application events.
2. **Pydantic Models**: Predefined models for User and Token with Pydantic, ensuring clear documentation in FastAPI’s Swagger UI.
3. **MongoDB Atlas**: The system is designed to connect with MongoDB Atlas, an online managed MongoDB service.
4. **Scalable Code Structure**: Modular and scalable backend structure to accommodate future extensions and enhancements.

### Bonus Features
1. **Role-Based Access Control (RBAC)**: Admin-only access for specific endpoints to control user access based on roles.
2. **Serverless Deployment Ready**: The project is structured to be deployed on serverless services for scalability and cost-efficiency.

## Project Structure

```plaintext
project/
│
├── app/
│   ├── main.py                  # Entry point for the FastAPI application
│   ├── config.py                # Configuration settings
│   ├── models/
│   │   ├── user.py              # Pydantic models for User and Token
│   ├── crud/
│   │   ├── user_crud.py         # CRUD operations for user management
│   ├── routes/
│   │   ├── auth.py              # Routes for login, logout, and user registration
│   │   ├── user.py              # Routes for user CRUD operations
│   ├── utils/
│   │   ├── auth_utils.py        # JWT token management and RBAC helper functions
│   │   ├── logging_config.py    # Logging configuration
│   └── scripts/
│       ├── create_user.py       # Script to create an initial user in MongoDB
│
├── .env                         # Environment variables (e.g., MongoDB URI, JWT secret key)
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Installation Guide

### Prerequisites

- **Python 3.8+**
- **MongoDB Atlas Account** or local MongoDB setup

### Environment Configuration

1. Clone the repository and navigate to the project folder.
2. Set up a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Configure environment variables by creating a `.env` file in the root directory:

    ```plaintext
    MONGO_URI="your_mongodb_uri_here"
    JWT_SECRET_KEY="your_jwt_secret_key_here"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

4. Connect to MongoDB Atlas or a local MongoDB instance by updating `MONGO_URI` in `.env`.

### Running the Application

To start the FastAPI server, run:

```bash
uvicorn app.main:app --reload
```

## Script for Initial User Creation

To create an initial user in MongoDB, execute the script in `scripts/create_user.py` with the desired username, email, password, and role.

```bash
python app/scripts/create_user.py
```

## API Endpoints

### Authentication Routes (`/auth`)
- **POST /auth/login**: Authenticate user credentials, return a JWT token.
- **POST /auth/logout**: Invalidate the JWT token (logic can be extended for token blacklisting).

### User CRUD Routes (`/users`)
- **GET /users/**: Retrieve all users (admin-only).
- **POST /users/**: Create a new user (admin-only).
- **PUT /users/{id}**: Update user information (admin-only).
- **DELETE /users/{id}**: Delete a user (admin-only).

### JWT Authentication and Role-Based Access Control (RBAC)

- **JWT Authentication**: Users must authenticate to receive a token for accessing protected endpoints.
- **Role-Based Access Control**: Admin roles are required for certain CRUD operations on users. Regular users cannot access restricted endpoints.

## Logging

- Configured to log API requests and application events.
- Log files or streams can be adjusted in `logging_config.py`.

## Deployment Guide (Optional)

To deploy this application on a serverless platform like **Vercel** or **Deta**, ensure the following:
- Configure environment variables on the platform.
- Update `MONGO_URI` to a secure database service, such as MongoDB Atlas.
  
Refer to the deployment platform’s documentation for additional steps.

## Checklist of Implemented Features

### Must-Have Features
- [x] Login and logout endpoints
- [x] Secure endpoints for user CRUD operations
- [x] Readable code with modular design
- [x] No ODM library usage
- [x] Script for initial user creation

### Good-to-Have Features
- [x] Logging support
- [x] Pydantic models for User and Token
- [x] MongoDB Atlas compatibility
- [x] Scalable code structure

### Bonus Features
- [x] Role-Based Access Control (RBAC)