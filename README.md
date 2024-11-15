# Gas Utility Service Management System

A Django-based web application designed to streamline customer service operations for gas utility companies. This system allows customers to conveniently submit, track, and manage their service requests while enabling customer support representatives to handle queries efficiently.

---

## Features

### For Customers:
- **Online Service Requests**: Submit requests for various services, provide detailed descriptions, and upload attachments.
- **Request Tracking**: Monitor the status of submitted service requests, including timestamps for submission and resolution.
- **Account Management**: Access and manage personal account details.

### For Customer Support Representatives:
- **Request Management**: View and update the status of service requests to provide timely support.
- **Support Tools**: Tools to manage customer interactions and ensure quality service.

---

## Tech Stack
- **Backend**: Django (Python-based web framework)
- **Database**: Configured with Django ORM for seamless data handling.
- **Frontend**: HTML, CSS, JavaScript (template-driven UI)
- **Additional Tools**: Support for file uploads and robust request handling.

---

## Setup Instructions

### Prerequisites:
- Python 3.x
- Django (install via `pip install django`)

### Steps:
1. Clone this repository:
   ```
   git clone <repository_url>
   cd gas-utility-service
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the development server:
   ```
   python manage.py runserver
   ```
5. Access the application at `http://127.0.0.1:8000`.

---

## Folder Structure
The project follows Django's recommended codebase structure:
- **`/gas_utility`**: Contains settings, URLs, and WSGI configuration.
- **`/services`**: App for handling service requests, including models, views, and templates.
- **`/templates`**: HTML files for rendering UI.
- **`/static`**: Static assets like CSS, JS, and images.

---

## Challenges & Highlights
- **Optimized Code Structure**: Emphasis on clean and modular coding practices to ensure scalability and maintainability.
- **Robust Request Tracking**: Implementation of user-friendly interfaces for tracking and managing service requests.

---

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

