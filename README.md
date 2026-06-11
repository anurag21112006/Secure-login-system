# Secure Login System

A secure web application built with Flask, SQLite, and bcrypt that provides user registration, login authentication, session management, and protection against common web attacks such as SQL injection.

## Features

- User Registration
- User Login Authentication
- Password Hashing using bcrypt
- Session Management
- Logout Functionality
- SQL Injection Protection
- Responsive User Interface

## Technologies Used

- Python
- Flask
- SQLite
- bcrypt
- HTML
- CSS

## Project Structure

```text
Secure_Login_System/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd Secure_Login_System
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Security Features

- Passwords are securely hashed using bcrypt.
- SQL Injection attacks are prevented using parameterized queries.
- User sessions are protected using Flask session management.
- Unauthorized users cannot access protected pages.

## Future Improvements

- Two-Factor Authentication (2FA)
- Email Verification
- Password Reset Functionality
- Account Lockout Protection
- User Profile Management

## Author

Anurag Upadhyay
