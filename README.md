# 📚 Library Management System — Machine Test

A Django REST Framework project implementing Author, Book, and Borrower management with JWT authentication.

---

## 🚀 Features
- CRUD APIs for Authors, Books, and Borrowers
- Borrowing logic ensures `available_copies > 0`
- JWT authentication for secured endpoints
- Optional admin panel and simple HTML frontend

---

## 🛠️ Installation

```bash
# clone repo
git clone https://github.com/<your-username>/library-management-test.git
cd library-management-test

# create venv
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# install dependencies
pip install -r requirements.txt

# migrate DB
python manage.py migrate

# create admin user
python manage.py createsuperuser
