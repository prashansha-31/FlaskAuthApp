# 🔐 Flask Authentication System

A secure Flask-based Authentication System with complete server-side validation.

This project implements user registration, login, password hashing, session management, and proper backend validation to fix registration bugs that allowed empty field submission.

---

## 📌 Project Overview

This web application allows users to:

- Register an account
- Login securely
- Access a protected dashboard
- Logout safely

The system ensures that users cannot register with invalid or empty inputs through proper server-side validation.

---

## 🚀 Features

✔ User Registration  
✔ User Login  
✔ Secure Password Hashing using bcrypt  
✔ Session Management  
✔ Logout Functionality  
✔ Flash Messages for Errors  
✔ Unique Email Validation  
✔ Password Length Enforcement  
✔ SQLite Database Integration  
✔ Bootstrap Responsive UI  
✔ Ready for Cloud Deployment (Render Compatible)  

---

## 🛠 Problem Statement

The original application had a major validation flaw:

Users were able to register even when:
- Name field was empty
- Email field was empty
- Password field was empty

This occurred because validation was not implemented on the backend.

---

## ✅ Solution Implemented

Proper **server-side validation** was added inside the `/register` route in Flask.

The application now enforces:

1. Name cannot be empty
2. Email cannot be empty
3. Password cannot be empty
4. Password must contain at least 6 characters
5. Email must be unique in the database
6. Proper error messages using Flask flash system

⚠ HTML `required` attribute alone is NOT secure — validation must always be done on the server side.

---

## 🔐 Security Implementation

- Passwords are hashed using **bcrypt**
- Raw passwords are never stored in the database
- Session-based authentication system
- Protected dashboard route
- Secure logout process

---

## 🗂 Project Structure

FlaskAuthApp/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
    ├── base.html
    ├── index.html
    ├── register.html
    ├── login.html
    ├── dashboard.html

---

## ⚙ Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- bcrypt
- Bootstrap 5
- Gunicorn (for deployment)

---

## 💻 How To Run Locally

### 1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/FlaskAuthApp.git  
cd FlaskAuthApp  

### 2️⃣ Install Dependencies

pip install -r requirements.txt  

### 3️⃣ Run The Application

python app.py  

Open in browser:  
http://127.0.0.1:5000  

---

## 🌍 Deployment Instructions (Render)

Build Command:

pip install -r requirements.txt  

Start Command:

gunicorn app:app  

Make sure the repository is public before deploying.

---

## 🔗 Project Links

GitHub Repository:  
https://github.com/prashansha-31/FlaskAuth_App
Live Deployment (Render):  
(Add your Render link here after deployment)

---

## 👩‍💻 Submitted By

Name: **Prashansha Maheshwari**  
Roll Number: **35**  
University Roll Number: **2415500347**  
Section: **2E**

---

## 📌 Final Conclusion

This project successfully resolves the registration validation bug by implementing proper backend validation in Flask.

The system now:

- Prevents invalid input submissions
- Ensures secure password storage
- Restricts duplicate registrations
- Protects routes using session management
- Displays meaningful user feedback

The application follows good development practices and is fully ready for deployment.
