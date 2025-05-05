## 📚 LIbary-Management-System (LMS)

This is a **Library Management System** built using the Django framework. The system allows users to manage books, categories, and users, as well as issue and return books.

## ✨ Features

- 📂 **Category Management**: View a list of book categories.
- 📖 **Book Management**: View books in a category and detailed information about each book.
- 👤 **User Management**: View a list of users and the books they have issued.
- 📝 **Issue Books**: Issue books to users and update the available copies.
- 🔄 **Return Books**: Return issued books and update the available copies.

## 🏗️ Project Structure

```
LMS/
├── LMS/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── library/
│   ├── migrations/
│   ├── templates/
│   │   ├── book_detail.html
│   │   ├── books_in_category.html
│   │   ├── issue_book.html
│   │   ├── list_categories.html
│   │   ├── list_users.html
│   │   ├── nav.html
│   │   ├── return_book.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── manage.py
```

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd LMS
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser at `http://127.0.0.1:8000/`.

## 🗂️ Models

### 📘 Book
- `title`: Title of the book.
- `author`: Author of the book.
- `category`: Foreign key to the `Category` model.
- `published_date`: Date the book was published.
- `copies_available`: Number of available copies.

### 🏷️ Category
- `name`: Name of the category.

### 👤 User
- `username`: Unique username of the user.
- `email`: Email address of the user.
- `pho_num`: Phone number of the user (optional).

### 🔖 Issue_book
- `book`: Foreign key to the `Book` model.
- `user`: Foreign key to the `User` model.
- `issue_date`: Date the book was issued.
- `return_date`: Date the book was returned (optional).

## 🌐 Views

- 🗂️ `list_categories`: Displays a list of all categories.
- 📚 `books_in_category`: Displays books in a specific category.
- 📖 `book_detail`: Displays details of a specific book.
- 📝 `issue_book`: Allows issuing a book to a user.
- 🔄 `return_book`: Allows returning an issued book.
- 👥 `list_users`: Displays a list of users and their issued books.

## 🖼️ Templates

- `list_categories.html`: Displays the list of categories.
- `books_in_category.html`: Displays books in a category.
- `book_detail.html`: Displays details of a book.
- `issue_book.html`: Form to issue a book.
- `return_book.html`: Form to return a book.
- `list_users.html`: Displays users and their issued books.
- `nav.html`: Navigation bar included in all templates.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
